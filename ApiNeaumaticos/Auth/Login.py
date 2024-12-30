"""Login state and authentication logic."""

from __future__ import annotations

import reflex as rx
from sqlmodel import select

from . import routes
from .Local_Auth import LocalAuthState
from .User import LocalUser


class LoginState(LocalAuthState):
    """Handle login form submission and redirect to proper routes after authentication."""

    # Usar LocalStorage para almacenar el nombre de usuario
    username: str = rx.LocalStorage("", sync=True)
    userId: str = rx.LocalStorage("", sync=True)
    error_message: str = ""
    redirect_to: str = "/dashboard"

    def on_submit(self, form_data) -> rx.event.EventSpec:
        """Handle login form on_submit.

        Args:
            form_data: A dict of form fields and values.
        """
        self.error_message = ""
        email = form_data["email"]
        password = form_data["password"]
        with rx.session() as session:
            user = session.exec(
                select(LocalUser).where(LocalUser.email == email)
            ).one_or_none()
        if user is not None and not user.enabled:
            self.error_message = "This account is disabled."
            return rx.set_value("password", "")
        if (
            user is not None
            and user.id is not None
            and user.enabled
            and password
            and user.verify(password)
        ):
            # mark the user as logged in
            self._login(user.id)
            self.username = user.username
            self.userId = user.id
        else:
            self.error_message = "There was a problem logging in, please try again."
            return rx.set_value("password", "")
        self.error_message = ""
        return LoginState.redir()  # type: ignore

    def redir(self) -> rx.event.EventSpec | None:
        """Redirect to the redirect_to route if logged in, or to the login page if not."""
        if not self.is_hydrated:
            # wait until after hydration to ensure auth_token is known
            return LoginState.redir()  # type: ignore
        page = self.router.page.path
        if not self.is_authenticated and page != routes.LOGIN_ROUTE:
            self.redirect_to = self.router.page.raw_path
            return rx.redirect(routes.LOGIN_ROUTE)
        elif self.is_authenticated and page == routes.LOGIN_ROUTE:
            return rx.redirect(self.redirect_to or "/")


def require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    """Decorator to require authentication before rendering a page.

    If the user is not authenticated, then redirect to the login page.

    Args:
        page: The page to wrap.

    Returns:
        The wrapped page component.
    """

    def protected_page():
        return rx.fragment(
            rx.cond(
                LoginState.is_hydrated & LoginState.is_authenticated,  # type: ignore
                page(),
                rx.center(
                    # When this text mounts, it will redirect to the login page
                    rx.text("Loading...", on_mount=LoginState.redir),
                ),
            )
        )

    protected_page.__name__ = page.__name__
    return protected_page
