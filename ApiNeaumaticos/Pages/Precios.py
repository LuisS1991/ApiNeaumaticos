import reflex as rx

def create_heading(text):
    """Create a styled heading component."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        color="#1F2937",
        as_="h2",
    )


def create_per_month_span():
    """Create a '/month' text span component."""
    return rx.text.span(
        "/month",
        font_weight="400",
        font_size="1rem",
        line_height="1.5rem",
        color="#4B5563",
    )


def create_price_text(price):
    """Create a styled price text component with '/month' suffix."""
    return rx.text(
        price,
        create_per_month_span(),
        font_weight="700",
        margin_bottom="1.5rem",
        font_size="2.25rem",
        line_height="2.5rem",
        color="#2563EB",
    )


def create_check_icon():
    """Create a styled check icon component."""
    return rx.icon(
        tag="check",
        height="1.25rem",
        margin_right="0.75rem",
        color="#10B981",
        width="1.25rem",
    )


def create_feature_text(feature):
    """Create a styled feature text span component."""
    return rx.text.span(feature, color="#374151")


def create_feature_list_item(feature_text):
    """Create a list item with a check icon and feature text."""
    return rx.el.li(
        create_check_icon(),
        create_feature_text(feature=feature_text),
        display="flex",
        align_items="center",
        margin_bottom="0.75rem",
    )


def create_action_button(button_text):
    """Create a styled action button component."""
    return rx.el.button(
        button_text,
        background_color="#2563EB",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_basic_plan_card():
    """Create the Basic plan pricing card component."""
    return rx.flex(
        create_heading(text="Basic"),
        create_price_text(price="$49"),
        rx.list(
            create_feature_list_item(
                feature_text="10,000 API calls/month"
            ),
            create_feature_list_item(
                feature_text="Basic tire data"
            ),
            create_feature_list_item(
                feature_text="Email support"
            ),
            flex_grow="1",
            margin_bottom="2rem",
        ),
        create_action_button(button_text="Choose Basic"),
        background_color="#ffffff",
        border_width="1px",
        border_color="#E5E7EB",
        transition_duration="300ms",
        display="flex",
        flex_direction="column",
        _hover={
            "box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
        },
        padding="2rem",
        border_radius="0.5rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_most_popular_badge():
    """Create a 'Most Popular' badge component."""
    return rx.box(
        "Most Popular",
        position="absolute",
        background_color="#3B82F6",
        font_weight="600",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        right="0",
        font_size="0.875rem",
        line_height="1.25rem",
        color="#ffffff",
        top="0",
    )


def create_pro_plan_card():
    """Create the Pro plan pricing card component."""
    return rx.flex(
        create_most_popular_badge(),
        create_heading(text="Pro"),
        create_price_text(price="$99"),
        rx.list(
            create_feature_list_item(
                feature_text="50,000 API calls/month"
            ),
            create_feature_list_item(
                feature_text="Advanced tire data"
            ),
            create_feature_list_item(
                feature_text="Priority email support"
            ),
            create_feature_list_item(
                feature_text="Real-time updates"
            ),
            flex_grow="1",
            margin_bottom="2rem",
        ),
        create_action_button(button_text="Choose Pro"),
        class_name="transform",
        background_color="#EFF6FF",
        border_width="2px",
        border_color="#3B82F6",
        display="flex",
        flex_direction="column",
        overflow="hidden",
        padding="2rem",
        position="relative",
        border_radius="0.5rem",
        transform="scale(1.05)",
        box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
    )


def create_enterprise_plan_card():
    """Create the Enterprise plan pricing card component."""
    return rx.flex(
        create_heading(text="Enterprise"),
        rx.text(
            "Custom",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="2.25rem",
            line_height="2.5rem",
            color="#2563EB",
        ),
        rx.list(
            create_feature_list_item(
                feature_text="Unlimited API calls"
            ),
            create_feature_list_item(
                feature_text="Full tire database access"
            ),
            create_feature_list_item(
                feature_text="24/7 phone & email support"
            ),
            create_feature_list_item(
                feature_text="Custom integrations"
            ),
            create_feature_list_item(
                feature_text="Dedicated account manager"
            ),
            flex_grow="1",
            margin_bottom="2rem",
        ),
        create_action_button(button_text="Contact Sales"),
        background_color="#ffffff",
        border_width="1px",
        border_color="#E5E7EB",
        transition_duration="300ms",
        display="flex",
        flex_direction="column",
        _hover={
            "box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
        },
        padding="2rem",
        border_radius="0.5rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_pricing_section():
    """Create the main pricing section with all plan cards."""
    return rx.box(
        rx.heading(
            "TireAPI Pricing Plans",
            font_weight="700",
            margin_bottom="1rem",
            font_size="2.25rem",
            line_height="2.5rem",
            text_align="center",
            color="#1F2937",
            as_="h1",
        ),
        rx.text(
            "Choose the plan that fits your needs and start leveraging our powerful tire data API",
            margin_bottom="3rem",
            text_align="center",
            color="#4B5563",
        ),
        rx.box(
            create_basic_plan_card(),
            create_pro_plan_card(),
            create_enterprise_plan_card(),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {"768px": "repeat(3, minmax(0, 1fr))"}
            ),
        ),
        padding_left="2rem",
        padding_right="2rem",
        padding_top="3rem",
        padding_bottom="3rem",
    )


def create_free_trial_banner():
    """Create a banner component for free trial information."""
    return rx.box(
        rx.text(
            "All plans include a 14-day free trial. No credit card required.",
            font_weight="500",
            text_align="center",
            color="#4B5563",
        ),
        background_color="#F9FAFB",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="1.5rem",
        padding_bottom="1.5rem",
    )


def create_pricing_page_content():
    """Create the main content container for the pricing page."""
    return rx.box(
        rx.box(
            create_pricing_section(),
            create_free_trial_banner(),
            background_color="#ffffff",
            max_width="64rem",
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

@rx.page("/pricing", "Api Neumaticos")
def Precios():
    """Create the complete pricing page with styling and layout."""
    return rx.fragment(
        rx.box(
            create_pricing_page_content(),
            background_color="#F3F4F6",
            display="flex",
            align_items="center",
            justify_content="center",
            min_height="100vh",
        ),
    )



