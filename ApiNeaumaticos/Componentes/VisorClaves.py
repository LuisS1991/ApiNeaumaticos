import reflex as rx
from ApiNeaumaticos.States.DashboardState import DashboardState


def create_section_heading(text):
    """Create a section heading with specific styling."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        color="#1F2937",
        as_="h2",
    )


def create_table_header_cell(content):
    """Create a styled table header cell with specific formatting."""
    return rx.table.column_header_cell(
        content,
        background_color="#F9FAFB",
        border_bottom_width="1px",
        border_color="#E5E7EB",
        font_weight="500",
        line_height="1rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        color="#6B7280",
        text_align="left",
        font_size="0.75rem",
        letter_spacing="0.05em",
        text_transform="uppercase",
    )


def create_table_cell(content):
    """Create a standard table cell with border and padding."""
    return rx.table.cell(
        content,
        border_bottom_width="1px",
        border_color="#E5E7EB",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_hidden_token_span(secret_key, id):
    """Create a span element that displays a hidden token placeholder."""
    return rx.cond(
        (DashboardState.show_key_input) & (id == DashboardState.idSelectedShowKey),
        rx.text.span(
            secret_key,
            background_color="#E5E7EB",
            margin_right="0.5rem",
            padding_left="0.5rem",
            padding_right="0.5rem",
            padding_top="0.25rem",
            padding_bottom="0.25rem",
            border_radius="0.25rem",
            width="200px",
            id=f"{id}",
        ),
        rx.text.span(
            "••••••••••••",
            background_color="#E5E7EB",
            margin_right="0.5rem",
            padding_left="0.5rem",
            padding_right="0.5rem",
            padding_top="0.25rem",
            padding_bottom="0.25rem",
            border_radius="0.25rem",
            width="200px",
            id=f"{id}",
        ),
    )


def create_show_icon(id):
    """Create an icon element for showing hidden content."""
    return rx.cond(
        id == DashboardState.idSelectedShowKey,
        rx.icon(
            alt="Show", tag="eye-off", height="1.25rem", width="1.25rem", id=f"{id}"
        ),
        rx.icon(alt="Show", tag="eye", height="1.25rem", width="1.25rem", id=f"{id}"),
    )


def create_show_button(id):
    """Create a button with a show icon for revealing hidden content."""
    return rx.el.button(
        create_show_icon(id=id),
        _hover={"color": "#1E40AF"},
        color="#2563EB",
        on_click=DashboardState.ShowKey(id),
    )


def create_token_display(secret_key, id):
    """Create a flex container with hidden token and show button."""
    return rx.flex(
        create_hidden_token_span(secret_key, id),
        create_show_button(id),
        display="flex",
        align_items="center",
    )


def create_token_cell(secret_key, id):
    """Create a table cell containing the token display component."""
    return rx.table.cell(
        create_token_display(secret_key, id),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_copy_button(secret_key):
    """Create a styled 'Copy' button for copying content."""
    return rx.el.button(
        "Copy",
        background_color="#3B82F6",
        _hover={"background-color": "#2563EB"},
        margin_right="0.5rem",
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        border_radius="0.25rem",
        color="#ffffff",
        on_click=DashboardState.Copykey(secret_key),
    )


def create_regenerate_button(tokenId):
    """Create a styled 'Regenerate' button for regenerating content."""
    return rx.el.button(
        "Regenerate",
        background_color="#10B981",
        _hover={"background-color": "#059669"},
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        border_radius="0.25rem",
        color="#ffffff",
        on_click=DashboardState.UpdateToken(tokenId),
    )


def create_delete_button(tokenId):
    """Create a styled 'Regenerate' button for delete content."""
    return rx.el.button(
        "Delete",
        background_color="#EF4444",
        _hover={"background-color": "#DC2626"},
        margin_right="0.5rem",
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        border_radius="0.25rem",
        color="#ffffff",
        on_click=DashboardState.DeleteKey(tokenId),
    )


def create_action_cell(secret_key: str, tokenId):
    """Create a table cell containing copy and regenerate buttons."""
    return rx.table.cell(
        create_copy_button(secret_key),
        create_delete_button(tokenId),
        create_regenerate_button(tokenId),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_api_table_row(api_name: str, secret_key: str, id):
    """Create a table row for displaying API information."""
    return rx.table.row(
        create_table_cell(content=api_name),
        create_token_cell(secret_key=secret_key, id=id),
        create_action_cell(secret_key, tokenId=id),
    )


def create_list_item(content):
    """Create a list item element with the given content."""
    return rx.el.li(content)


def forItem(apiName: str, token: str, id: int):
    return create_api_table_row(api_name=apiName, secret_key=token, id=id)


def create_api_table():
    """Create the main API credentials table with headers and rows."""
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                create_table_header_cell(content="API Name"),
                create_table_header_cell(content="Secret Token"),
                create_table_header_cell(content="Actions"),
            ),
            width="100%",
        ),
        rx.table.body(
            rx.foreach(
                DashboardState.tokenList,
                lambda token: forItem(token.apiName, token.token, token.id),
            ),
            width="100%",
        ),
        background_color="#ffffff",
        width="100%",
    )


def create_security_recommendations_list():
    """Create a list of security recommendations for API usage."""
    return rx.list(
        create_list_item(
            content="Nunca compartas tus tokens secretos de API con nadie."
        ),
        create_list_item(
            content="Rote periódicamente sus tokens API para mejorar la seguridad."
        ),
        create_list_item(
            content="Utilice variables de entorno para almacenar tokens en sus aplicaciones."
        ),
        create_list_item(
            content="Supervise el uso de API y configure alertas para actividades sospechosas."
        ),
        display="flex",
        flex_direction="column",
        list_style_type="disc",
        padding_left="1.5rem",
        gap="0.5rem",
        color="#374151",
    )


def create_dashboard_content():
    """Create the main content of the Secure API Dashboard."""
    return rx.box(
        rx.box(
            create_section_heading(text="API Credentials"),
            rx.box(create_api_table(), overflow_x="auto"),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        rx.box(
            create_section_heading(text="Security Recommendations"),
            create_security_recommendations_list(),
            background_color="#ffffff",
            margin_top="2rem",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
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


def create_dashboard_page():
    """Create the complete Secure API Dashboard page with styling and content."""
    return create_dashboard_content()
