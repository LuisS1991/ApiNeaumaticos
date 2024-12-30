import reflex as rx
from ApiNeaumaticos.templates import template
from ApiNeaumaticos.Auth import require_login, LoginState
from ApiNeaumaticos.States.UserState import UserState
from ApiNeaumaticos.Componentes.Alerta import create_notification


def create_section_heading(text):
    """Create a section heading with specific styling."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        color="#374151",
        as_="h2",
    )


def create_form_label(label_text):
    """Create a form label with specific styling."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.5rem",
        color="#374151",
    )


def create_styled_input(input_id, input_name, input_type, default_value, onChange):
    """Create a styled input field with customizable attributes."""
    return rx.el.input(
        type=input_type,
        id=input_id,
        name=input_name,
        value=default_value,
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
        on_change=onChange,
    )


def create_password_input():
    """Create a styled password input field."""
    return rx.el.input(
        type="password",
        id="password",
        name="password",
        placeholder="Enter new password",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
    )


def create_submit_button():
    """Create a styled submit button for form submission."""
    return rx.el.button(
        " Update Information ",
        type="submit",
        background_color="#3B82F6",
        _focus={
            "outline-style": "none",
            "box-shadow": "0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow)",
            "--ring-color": "#3B82F6",
            "--ring-offset-width": "2px",
        },
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
    )


def create_account_form():
    """Create a form for account information update."""
    return rx.form(
        rx.box(
            create_form_label(label_text="Name"),
            create_styled_input(
                input_id="username",
                input_name="username",
                input_type="text",
                default_value=UserState.userName,
                onChange=UserState.set_userName,
            ),
            margin_bottom="1rem",
        ),
        rx.box(
            create_form_label(label_text="Email"),
            create_styled_input(
                input_id="email",
                input_name="email",
                input_type="email",
                default_value=UserState.email,
                onChange=UserState.set_email,
            ),
            margin_bottom="1rem",
        ),
        rx.box(
            create_form_label(label_text="New Password"),
            create_password_input(),
            margin_bottom="1.5rem",
        ),
        create_submit_button(),
        on_submit=UserState.handle_submit,
    )


def create_delete_account_button():
    """Create a styled button for account deletion."""
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.el.button(
                " Delete Account ",
                background_color="#EF4444",
                _focus={
                    "outline-style": "none",
                    "box-shadow": "0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow)",
                    "--ring-offset-width": "2px",
                    "--ring-color": "#EF4444",
                },
                _hover={"background-color": "#DC2626"},
                padding_left="1rem",
                padding_right="1rem",
                padding_top="0.5rem",
                padding_bottom="0.5rem",
                border_radius="0.375rem",
                color="#ffffff",
            )
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Revoke access"),
            rx.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
                size="2",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Revoke access",
                        color_scheme="red",
                        variant="solid",
                        on_click=UserState.deleteUser,
                    ),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            style={"max_width": 450},
        ),
    )


def create_delete_account_section():
    """Create a section for account deletion with warning and button."""
    return rx.box(
        create_section_heading(text="Delete Account"),
        rx.text(
            "Warning: This action cannot be undone. All your data will be permanently deleted.",
            margin_bottom="1rem",
            color="#4B5563",
        ),
        create_delete_account_button(),
        background_color="#ffffff",
        margin_top="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_account_management_page():
    """Create the main account management page layout."""
    return rx.box(
        rx.heading(
            "Account Management",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#1F2937",
            as_="h1",
        ),
        rx.box(
            create_section_heading(text="Personal Information"),
            create_account_form(),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        create_delete_account_section(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def render_account_management_app():
    """Render the complete account management application with styling and layout."""
    return rx.fragment(
        rx.box(
            rx.cond(
                UserState.show,
                create_notification(
                    bg_color="#10B981",
                    icon_alt="Success icon",
                    icon_tag="circle-alert",
                    message="Information updated successfully!",
                    eventClose=UserState.CloseAlert
                ),
            ),
            create_account_management_page(),
            background_color="#F3F4F6",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
    )


@template(
    route="/config", title="Api Neumaticos", description="", on_load=UserState.onLoad
)
@require_login
def Configuracion() -> rx.Component:
    return render_account_management_app()
