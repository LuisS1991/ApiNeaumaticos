import reflex as rx
from ApiNeaumaticos.templates import template
from ApiNeaumaticos.Auth import require_login, LoginState
from ApiNeaumaticos.Componentes.VisorClaves import create_dashboard_page
from ApiNeaumaticos.States.DashboardState import DashboardState
from ApiNeaumaticos.Componentes.Alerta import create_notification

def create_select_option(option_text):
    """Creates an option element for a select dropdown."""
    return rx.el.option(option_text)


def create_api_selector():
    """Creates the API selection dropdown section."""
    return rx.box(
        create_section_heading(heading_text="Seleccionar API"),
        rx.el.select(
            create_select_option(option_text="Seleccione una API"),
            create_select_option(option_text="API de Neumáticos"),
            border_width="1px",
            border_color="#D1D5DB",
            padding="0.5rem",
            border_radius="0.375rem",
            width="100%",
        ),
        background_color="#ffffff",
        margin_bottom="1.5rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_form_label(label_text):
    """Creates a label for form inputs with specific styling."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.5rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_readonly_input(input_id, input_type, input_value):
    """Creates a readonly input field with specific styling."""
    return rx.el.input(
        id=input_id,
        type=input_type,
        value=input_value,
        readonly=True,
        border_width="1px",
        border_color="#D1D5DB",
        padding="0.5rem",
        border_radius="0.375rem",
        width="100%",
    )


def create_labeled_input(label_text, input_id, input_type, input_value):
    """Creates a labeled input field with specific styling."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_readonly_input(
            input_id=input_id,
            input_type=input_type,
            input_value=input_value,
        ),
        margin_bottom="1rem",
    )


def create_key_generation_section():
    """Creates the key generation section with buttons."""
    return rx.box(
        create_section_heading(heading_text="Generar Claves"),
        rx.flex(
            create_styled_button(
                hover_style={"background-color": "#059669"},
                background_color="#10B981",
                button_text="Generar Clave Privada",
                event=DashboardState.GenerarKey,
            ),
            display="flex",
            column_gap="1rem",
        ),
        background_color="#ffffff",
        margin_bottom="1.5rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_styled_button(hover_style, background_color, button_text, event):
    """Creates a styled button with hover effects."""
    return rx.el.button(
        button_text,
        background_color=background_color,
        _hover=hover_style,
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        on_click=event,
    )


def create_section_heading(heading_text):
    """Creates a section heading with specific styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="1rem",
        color="#374151",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_main_content():
    """Creates the main content area of the application."""
    return rx.box(
           rx.cond(
                DashboardState.show,
                create_notification(
                    bg_color="#10B981",
                    icon_alt="Success icon",
                    icon_tag="circle-alert",
                    message=DashboardState.mensaje,
                    eventClose=DashboardState.CloseAlert
                ),
            ),
        rx.heading(f"Welcome {LoginState.username}", size="5"),
        rx.heading(
            "Gestión de API",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            color="#1F2937",
            as_="h2",
        ),
        create_api_selector(),
        create_key_generation_section(),
        rx.box(
            create_section_heading(heading_text="Credenciales de Acceso"),
            create_dashboard_page(),
            width="100%",
        ),
        flex="1 1 0%",
        overflow_y="auto",
        padding="2rem",
    )


@template(
    route="/dashboard",
    title="Api Neumaticos",
    description="",
    on_load=DashboardState.onLoad,
)
@require_login
def Dashboard() -> rx.Component:
    return create_main_content()


"""
create_styled_button(
    hover_style={"background-color": "#2563EB"},
    background_color="#3B82F6",
    button_text="Generar Clave Pública",
    ),
"""

"""
create_labeled_input(
    label_text="Clave Pública",
    input_id="public-key",
    input_type="text",
    input_value="pk_test_1234567890abcdef",
 ),
create_labeled_input(
                label_text="Clave Privada",
                input_id="private-key",
                input_type="password",
                input_value="••••••••••••••••",
            ),
            create_styled_button(
                hover_style={"background-color": "#DC2626"},
                background_color="#EF4444",
                button_text="Revocar Claves",
            ),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
 
 """
