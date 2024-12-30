import reflex as rx


def create_icon(alt_text, icon_tag):
    """Create an icon element with specific attributes."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="1.5rem",
        margin_right="0.5rem",
        width="1.5rem",
    )


def create_text_span(text):
    """Create a text span element."""
    return rx.text.span(text)


def create_notification(bg_color, icon_alt, icon_tag, message,eventClose):
    """Create a notification component with an icon and message."""
    return rx.flex(
        create_icon(alt_text=icon_alt, icon_tag=icon_tag),
        create_text_span(text=message),
        rx.spacer(),
        rx.button(
            create_icon(alt_text="x", icon_tag="x"),
            border="none",
            background_color="transparent",
            on_click=eventClose
        ),
        background_color=bg_color,
        display="flex",
        align_items="center",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        margin_botton="1.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        color="#ffffff",
        class_name="animate__animated animate__fadeIn",
    )


"""
  create_notification(
            bg_color="#10B981",
            icon_alt="Success icon",
            icon_tag="circle-alert",
            message="Information updated successfully!",
        ),
"""
