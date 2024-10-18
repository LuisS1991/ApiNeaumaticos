import reflex as rx


def create_icon(alt_text, icon_name):
    """Create an icon with specified alt text and icon name."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="1.25rem",
        margin_right="0.5rem",
        width="1.25rem",
    )


def create_link(url, link_text):
    """Create a styled link with hover effect."""
    return rx.el.a(
        link_text,
        href=url,
        _hover={"text-decoration": "underline"},
        color="#2563EB",
    )


def create_home_button():
    """Create a styled home button with icon."""
    return rx.el.a(
        create_icon(alt_text="Home icon", icon_name="home"),
        " Go to Homepage ",
        href="/",
        background_color="#2563EB",
        transition_duration="300ms",
        display="flex",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        align_items="center",
        justify_content="center",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_contact_button():
    """Create a styled contact support button with icon."""
    return rx.el.a(
        create_icon(
            alt_text="Contact icon",
            icon_name="message-circle",
        ),
        " Contact Support ",
        href="/contact",
        background_color="#E5E7EB",
        transition_duration="300ms",
        display="flex",
        font_weight="600",
        _hover={"background-color": "#D1D5DB"},
        align_items="center",
        justify_content="center",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#1F2937",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_404_content():
    """Create the main content for the 404 error page."""
    return rx.box(
        rx.heading(
            "404",
            font_weight="700",
            margin_bottom="1rem",
            font_size="3.75rem",
            line_height="1",
            color="#2563EB",
            as_="h1",
        ),
        rx.heading(
            "Oops! Page Not Found",
            font_weight="600",
            margin_bottom="1rem",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#1F2937",
            as_="h2",
        ),
        rx.text(
            "Looks like this tire has gone flat. The page you're looking for doesn't exist or has been moved.",
            margin_bottom="2rem",
            color="#4B5563",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.box(
            rx.image(
                src="/auto.webp",
                alt="Illustration of a car with a flat tire, representing the 404 error",
                margin_left="auto",
                margin_right="auto",
                border_radius="0.5rem",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            ),
            margin_bottom="3rem",
        ),
        rx.flex(
            create_home_button(),
            create_contact_button(),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "640px": "row"}
            ),
            gap="1rem",
            justify_content="center",
        ),
        padding_left="2rem",
        padding_right="2rem",
        padding_top="3rem",
        padding_bottom="3rem",
        text_align="center",
    )


def create_help_footer():
    """Create a footer with helpful links for the 404 page."""
    return rx.box(
        rx.text(
            "Need help? Check our ",
            create_link(url="/faq", link_text="FAQ"),
            " or ",
            create_link(
                url="/documentation",
                link_text="API Documentation",
            ),
            ".",
            text_align="center",
            color="#4B5563",
        ),
        background_color="#F9FAFB",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="1.5rem",
        padding_bottom="1.5rem",
    )


def create_responsive_container():
    """Create a responsive container for the 404 page content."""
    return rx.box(
        rx.box(
            create_404_content(),
            create_help_footer(),
            background_color="#ffffff",
            max_width="48rem",
            margin_left="auto",
            margin_right="auto",
            overflow="hidden",
            border_radius="0.75rem",
            box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.25)",
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
        padding_top="3rem",
        padding_bottom="3rem",
    )


def create_404_page():
    """Create the complete 404 error page with styling and content."""
    return rx.fragment(
        rx.box(
            create_responsive_container(),
            background_color="#F3F4F6",
            display="flex",
            align_items="center",
            justify_content="center",
            min_height="100vh",
        ),
    )