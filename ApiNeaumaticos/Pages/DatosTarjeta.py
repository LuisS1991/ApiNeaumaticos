import reflex as rx


def create_stylesheet_link(stylesheet_url):
    """Creates a link element for a stylesheet with the given URL."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_heading(text):
    """Creates a styled heading element with the given text."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="0.75rem",
        color="#374151",
        font_size="1.125rem",
        line_height="1.75rem",
        as_="h2",
    )


def create_bold_span(text):
    """Creates a span element with bold text."""
    return rx.text.span(text, display="block", font_weight="600")


def create_muted_span(text):
    """Creates a span element with muted text styling."""
    return rx.text.span(
        text,
        color="#6B7280",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_label_span(bold_text, muted_text):
    """Creates a span element with bold and muted text components."""
    return rx.text.span(
        create_bold_span(text=bold_text),
        create_muted_span(text=muted_text),
        margin_left="0.5rem",
    )


def create_radio_input():
    """Creates a styled radio input element."""
    return rx.el.input(
        type="radio",
        name="plan",
        class_name="form-radio",
        color="#2563EB",
    )


def create_plan_option(plan_name, plan_price):
    """Creates a labeled radio input for a plan option."""
    return rx.el.label(
        create_radio_input(),
        create_label_span(bold_text=plan_name, muted_text=plan_price),
        border_width="1px",
        cursor="pointer",
        display="flex",
        _hover={"background-color": "#F9FAFB"},
        align_items="center",
        padding="0.75rem",
        border_radius="0.5rem",
    )


def create_form_label(label_text):
    """Creates a styled label for form elements."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.25rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_text_input(input_id, placeholder_text):
    """Creates a styled text input element."""
    return rx.el.input(
        type="text",
        id=input_id,
        placeholder=placeholder_text,
        border_width="1px",
        border_color="#D1D5DB",
        padding="0.5rem",
        border_radius="0.375rem",
        width="100%",
    )


def create_labeled_input(label_text, input_id, placeholder_text):
    """Creates a labeled input field with a given label, ID, and placeholder."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_text_input(
            input_id=input_id,
            placeholder_text=placeholder_text,
        ),
    )


def create_flex_input(label_text, input_id, placeholder_text):
    """Creates a flexible labeled input field for use in a flex container."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_text_input(
            input_id=input_id,
            placeholder_text=placeholder_text,
        ),
        flex="1 1 0%",
    )


def create_basic_plan_option():
    """Creates a pre-selected radio option for the Basic Plan."""
    return rx.el.label(
        rx.el.input(
            type="radio",
            name="plan",
            class_name="form-radio",
            checked=True,
            color="#2563EB",
        ),
        create_label_span(bold_text="Basic Plan", muted_text="$9.99/month"),
        border_width="1px",
        cursor="pointer",
        display="flex",
        _hover={"background-color": "#F9FAFB"},
        align_items="center",
        padding="0.75rem",
        border_radius="0.5rem",
    )


def create_payment_form():
    """Creates a form for entering payment information."""
    return rx.box(
        create_labeled_input(
            label_text="Card Number",
            input_id="card-number",
            placeholder_text="1234 5678 9012 3456",
        ),
        rx.flex(
            create_flex_input(
                label_text="Expiry Date",
                input_id="expiry-date",
                placeholder_text="MM/YY",
            ),
            create_flex_input(
                label_text="CVV",
                input_id="cvv",
                placeholder_text="123",
            ),
            display="flex",
            column_gap="1rem",
        ),
        create_labeled_input(
            label_text="Cardholder Name",
            input_id="cardholder-name",
            placeholder_text="John Doe",
        ),
        display="flex",
        flex_direction="column",
        gap="1rem",
    )


def create_subscribe_button():
    """Creates a styled subscribe button."""
    return rx.el.button(
        "Subscribe Now",
        background_color="#2563EB",
        transition_duration="300ms",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_subscription_form():
    """Creates the main subscription form including plan selection and payment details."""
    return rx.box(
        rx.heading(
            "Subscribe to TireAPI",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            color="#1F2937",
            as_="h1",
        ),
        rx.box(
            create_heading(text="Select a Plan"),
            rx.box(
                create_basic_plan_option(),
                create_plan_option(
                    plan_name="Pro Plan",
                    plan_price="$19.99/month",
                ),
                create_plan_option(
                    plan_name="Enterprise Plan",
                    plan_price="$49.99/month",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
            margin_bottom="1.5rem",
        ),
        rx.box(
            create_heading(text="Payment Information"),
            create_payment_form(),
            margin_bottom="1.5rem",
        ),
        create_subscribe_button(),
        rx.text(
            "By subscribing, you agree to our Terms of Service and Privacy Policy",
            margin_top="1rem",
            text_align="center",
            color="#6B7280",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        background_color="#ffffff",
        max_width="28rem",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
        width="100%",
    )


def create_subscription_page():
    """Creates the complete subscription page with styling and layout."""
    return rx.fragment(

        rx.box(
            rx.flex(
                create_subscription_form(),
                display="flex",
                align_items="center",
                justify_content="center",
                min_height="100vh",
            ),
            class_name="font-inter",
            background_color="#F3F4F6",
        ),
    )


@rx.page("/tarjeta", "Api")
def DatosTarjeta() -> rx.Component:
    return create_subscription_page()
