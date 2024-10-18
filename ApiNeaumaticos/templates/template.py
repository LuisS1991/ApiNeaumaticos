from __future__ import annotations
from typing import Callable
import reflex as rx
from ApiNeaumaticos.Auth import LoginState


# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


##### create_app_layout #####
def create_api_management_link(url):
    """Creates the API management link for the sidebar."""
    return rx.el.a(
        create_icon(icon_tag="key"),
        " Gestión de API ",
        href=url,
        background_color="#DBEAFE",
        display="flex",
        align_items="center",
        padding_left="1.25rem",
        padding_right="1.25rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        color="#374151",
    )


def create_icon(icon_tag):
    """Creates an icon element with specific styling."""
    return rx.icon(
        tag=icon_tag,
        height="1.25rem",
        margin_right="0.75rem",
        width="1.25rem",
    )


def create_button_exit():
    return rx.el.button(
        create_icon("log-out"),
        "Logout",
        background_color="#EF4444",
        _hover={"background-color": "#DC2626"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        display="flex",
        gap="5px",
        on_click=LoginState.do_logout,
    )


def create_stylesheet_link(stylesheet_url):
    """Creates a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_sidebar_link(icon_tag, link_text, url):
    """Creates a sidebar link with an icon and text."""
    return rx.el.a(
        create_icon(icon_tag=icon_tag),
        link_text,
        href=url,
        display="flex",
        _hover={"background-color": "#F3F4F6"},
        align_items="center",
        padding_left="1.25rem",
        padding_right="1.25rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        color="#374151",
    )


def create_sidebar_list_item(icon_tag, link_text, url):
    """Creates a list item for the sidebar with a link."""
    return rx.el.li(
        create_sidebar_link(icon_tag=icon_tag, link_text=link_text, url=url),
        margin_bottom="0.5rem",
    )


def create_sidebar():
    """Creates the complete sidebar for the application."""
    return rx.box(
        rx.box(
            rx.flex(
                rx.image("/Icon.png", width="25%"),
                rx.spacer(),
                rx.center(
                    rx.heading(
                        "TireAPI",
                        font_weight="700",
                        font_size="1.5rem",
                        line_height="2rem",
                        color="#1F2937",
                        as_="h1",
                    ),
                ),
                rx.spacer(),
            ),
            padding="1.25rem",
        ),
        rx.list(
            rx.el.li(
                create_api_management_link(url="/dashboard"),
                margin_bottom="0.5rem",
            ),
            create_sidebar_list_item(
                icon_tag="settings", link_text=" Configuración ", url="/config"
            ),
            margin_top="1.5rem",
        ),
        rx.center(create_button_exit()),
        background_color="#ffffff",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        width="16rem",
    )


def create_app_layout(page_content):
    """Creates the overall layout of the application, including styles and structure."""
    return rx.fragment(
        rx.el.style(
            """
            @font-face {
                font-family: 'LucideIcons';
                src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
            }
            """
        ),
        rx.box(
            rx.flex(
                create_sidebar(),
                rx.box(
                    page_content,
                    flex="1 1 0%",
                    overflow_y="auto",
                    padding="2rem",
                ),
                display="flex",
                height="100vh",
            ),
            class_name="font-inter",
            background_color="#F3F4F6",
        ),
    )


def template(
    route: str | None = None,
    title: str | None = None,
    image: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:

        all_meta = [*default_meta, *(meta or [])]

        @rx.page(
            route=route,
            title=title,
            image=image,
            description=description,
            meta=all_meta,  # type: ignore
            script_tags=script_tags,
            on_load=on_load,
        )
        def templated_page():
            return create_app_layout(page_content())

        return templated_page  # type: ignore

    return decorator


"""
 rx.desktop_only(
        rx.text("Desktop View"),
    ),
    rx.tablet_only(
        rx.text("Tablet View"),
    ),
    rx.mobile_only(
        rx.text("Mobile View"),
    ),
    rx.mobile_and_tablet(
        rx.text("Visible on Mobile and Tablet"),
    ),
    rx.tablet_and_desktop(
        rx.text("Visible on Desktop and Tablet"),
    ),
"""
