import reflex as rx
from ApiNeaumaticos.Auth import LoginState, routes


def create_label(label_text):
    """Create a styled label element with the given text."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="700",
        margin_bottom="0.5rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_label_message_error():
    """Create a styled label element with the given text."""
    return rx.el.label(
        LoginState.error_message,
        display="block",
        font_weight="700",
        margin_bottom="0.5rem",
        color="#e74c3c",
        font_size="0.875rem",
        line_height="1.25rem",
        text_align="center",
    )


def create_input_icon(icon_tag):
    """Create an icon element for use within an input field."""
    return rx.icon(
        tag=icon_tag,
        position="absolute",
        height="1.25rem",
        left="0.75rem",
        color="#9CA3AF",
        top="0.75rem",
        width="1.25rem",
    )


def create_input_field(input_id, placeholder_text, input_type):
    """Create a styled input field with the given id, placeholder, and type."""
    return rx.el.input(
        id=input_id,
        placeholder=placeholder_text,
        type=input_type,
        border_width="2px",
        border_color="#E5E7EB",
        _focus={"border-color": "#3B82F6"},
        outline_style="none",
        padding_left="2.5rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        width="100%",
    )


def create_input_with_icon(icon_tag, input_id, placeholder_text, input_type):
    """Create an input field with an associated icon."""
    return rx.box(
        create_input_icon(icon_tag=icon_tag),
        create_input_field(
            input_id=input_id,
            placeholder_text=placeholder_text,
            input_type=input_type,
        ),
        position="relative",
    )


def create_login_header():
    """Create the header section for the login form."""
    return rx.box(
        rx.center(
            rx.image("/Icon.png", width="25%"),
        ),
        rx.heading(
            "TireAPI",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#1F2937",
            as_="h1",
        ),
        rx.text(
            "Log in to your account",
            margin_top="0.5rem",
            color="#4B5563",
        ),
        margin_bottom="2rem",
        text_align="center",
    )


def create_remember_me_checkbox():
    """Create a 'Remember me' checkbox with label."""
    return rx.flex(
        rx.el.input(
            id="remember-me",
            type="checkbox",
            border_color="#D1D5DB",
            _focus={"--ring-color": "#3B82F6"},
            height="1rem",
            border_radius="0.25rem",
            color="#3B82F6",
            width="1rem",
        ),
        rx.el.label(
            "Remember me",
            display="block",
            margin_left="0.5rem",
            color="#374151",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        display="flex",
        align_items="center",
    )


def create_login_options():
    """Create the 'Remember me' checkbox and 'Forgot password' link."""
    return rx.flex(
        create_remember_me_checkbox(),
        rx.el.a(
            "Forgot password?",
            href="#",
            _hover={"color": "#1D4ED8"},
            color="#3B82F6",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_bottom="1.5rem",
    )


def create_login_button():
    """Create a styled 'Log In' submit button."""
    return rx.el.button(
        "Log In",
        type="submit",
        background_color="#3B82F6",
        _focus={
            "outline-style": "none",
            "box-shadow": "0 0 0 3px rgba(59, 130, 246, 0.5)",
        },
        font_weight="700",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        width="100%",
    )


def create_login_form():
    """Create the complete login form with email and password fields."""
    return rx.form(
        rx.box(
            create_label(label_text="Email Address"),
            create_input_with_icon(
                icon_tag="mail",
                input_id="email",
                placeholder_text="you@example.com",
                input_type="text",
            ),
            margin_bottom="1.5rem",
        ),
        rx.box(
            create_label(label_text="Password"),
            create_input_with_icon(
                icon_tag="lock",
                input_id="password",
                placeholder_text="••••••••",
                input_type="password",
            ),
            margin_bottom="1.5rem",
        ),
        create_login_options(),
        create_login_button(),
        on_submit=LoginState.on_submit,
    )


def create_signup_link():
    """Create a 'Sign up' link for users without an account."""
    return rx.box(
        rx.text(
            "Don't have an account? ",
            rx.el.a(
                "Sign up",
                href=routes.REGISTER_ROUTE,
                _hover={"color": "#1D4ED8"},
                color="#3B82F6",
            ),
            color="#4B5563",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        margin_top="2rem",
        text_align="center",
    )


def create_login_page():
    """Create the entire login page layout."""
    return rx.box(
        rx.box(
            create_login_header(),
            create_login_form(),
            create_signup_link(),
            create_label_message_error(),
            background_color="#ffffff",
            max_width="28rem",
            padding="2rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            width="100%",
        ),
        class_name="font-inter",
        background_color="#F3F4F6",
        display="flex",
        align_items="center",
        justify_content="center",
        min_height="100vh",
    )


def create_page_with_styles():
    """Create the complete page with necessary stylesheets and fonts."""
    return rx.fragment(
        create_login_page(),
    )


@rx.page("/login", "Login Api")
def Login() -> rx.Component:
    return create_page_with_styles()
