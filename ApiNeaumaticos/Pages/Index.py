import reflex as rx


def create_hover_link(hover_styles, text_color, link_text, url):
    """Create a link with hover effects and custom color."""
    return rx.el.a(
        link_text,
        href=url,
        _hover=hover_styles,
        color=text_color,
    )


def create_custom_heading(heading_level, font_size, line_height, heading_text):
    """Create a custom heading with specified styles."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        as_=heading_level,
    )


def create_subheading(subheading_text):
    """Create a subheading with predefined styles."""
    return rx.heading(
        subheading_text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.125rem",
        line_height="1.75rem",
        as_="h4",
    )


def create_styled_text(text_color, margin_bottom, text_content):
    """Create a styled text element with custom color and margin."""
    return rx.text(
        text_content,
        margin_bottom=margin_bottom,
        color=text_color,
    )


def create_check_icon():
    """Create a check icon with predefined styles."""
    return rx.icon(
        tag="check",
        height="1.25rem",
        margin_right="0.5rem",
        color="#10B981",
        width="1.25rem",
    )


def create_list_item_with_icon(item_text):
    """Create a list item with a check icon and custom text."""
    return rx.el.li(
        create_check_icon(),
        item_text,
        display="flex",
        align_items="center",
        margin_bottom="0.5rem",
    )


def create_per_month_span():
    """Create a span element with '/month' text and predefined styles."""
    return rx.text.span(
        "/month",
        font_weight="400",
        font_size="1.125rem",
        line_height="1.75rem",
    )


def create_price_text(price):
    """Create a styled price text with '/month' suffix."""
    return rx.text(
        price,
        create_per_month_span(),
        font_weight="700",
        margin_bottom="1.5rem",
        font_size="1.875rem",
        line_height="2.25rem",
    )


def create_get_started_button():
    """Create a 'Get Started' button with predefined styles."""
    return rx.el.a(
        "Get Started",
        href="/login",
        background_color="#3B82F6",
        display="block",
        _hover={"background-color": "#2563EB"},
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        text_align="center",
        color="#ffffff",
        width="100%",
        
    )


def create_footer_list_item(item_text):
    """Create a footer list item with custom text and styles."""
    return rx.el.li(
        create_hover_link(
            hover_styles={"color": "#ffffff"},
            text_color="#9CA3AF",
            link_text=item_text,
            url="/"
        ),
        margin_bottom="0.5rem",
    )


def create_header_get_started_button():
    """Create a 'Get Started' button for the header with predefined styles."""
    return rx.el.a(
        "Login",
        href="/login",
        background_color="#3B82F6",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
    )


def create_header():
    """Create the header section with logo, navigation, and button."""
    return rx.flex(
        rx.flex(
            rx.image("/Icon.png", width="10%"),
            rx.center(
                rx.box(
                    "TireAPI",
                    font_weight="700",
                    font_size="1.5rem",
                    line_height="2rem",
                    color="#1F2937",
                ),
            ),
            gap="20px",
        ),
        rx.box(
            create_hover_link(
                hover_styles={"color": "#111827"},
                text_color="#4B5563",
                link_text="Home",
                url="/",
            ),
            create_hover_link(
                hover_styles={"color": "#111827"},
                text_color="#4B5563",
                link_text="Features",
                url="/features",
            ),
            create_hover_link(
                hover_styles={"color": "#111827"},
                text_color="#4B5563",
                link_text="Pricing",
                url="/pricing",
            ),
            create_hover_link(
                hover_styles={"color": "#111827"},
                text_color="#4B5563",
                link_text="Documentation",
                url="/doc",
            ),
            display=rx.breakpoints({"0px": "none", "768px": "flex"}),
            column_gap="1.5rem",
        ),
        create_header_get_started_button(),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_header_container():
    """Create a container for the header with responsive styles."""
    return rx.box(
        rx.box(
            create_header(),
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
            padding_left="1.5rem",
            padding_right="1.5rem",
            padding_top="1rem",
            padding_bottom="1rem",
        ),
        background_color="#ffffff",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_hero_cta_button():
    """Create a call-to-action button for the hero section."""
    return rx.el.a(
        "Start Your Free Trial",
        href="/register",
        background_color="#3B82F6",
        _hover={"background-color": "#2563EB"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        font_size="1.125rem",
        line_height="1.75rem",
        color="#ffffff",
    )


def create_hero_section():
    """Create the hero section with title, description, and CTA button."""
    return rx.box(
        create_custom_heading(
            heading_level="h1",
            font_size="3rem",
            line_height="1",
            heading_text="Access Comprehensive Tire Data with TireAPI",
        ),
        rx.text(
            "Get detailed information about various tire providers, specifications, and pricing all in one place.",
            margin_bottom="2rem",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_hero_cta_button(),
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
        padding_left="1.5rem",
        padding_right="1.5rem",
        text_align="center",
    )


def create_free_tier_card():
    """Create a pricing card for the free tier."""
    return rx.box(
        create_custom_heading(
            heading_level="h3",
            font_size="1.5rem",
            line_height="2rem",
            heading_text="Free Tier",
        ),
        create_styled_text(
            text_color="#4B5563",
            margin_bottom="1.5rem",
            text_content="Basic access to tire information",
        ),
        rx.list(
            create_list_item_with_icon(item_text=" Limited API calls "),
            create_list_item_with_icon(item_text=" Basic tire specifications "),
            create_list_item_with_icon(item_text=" Public data only "),
            margin_bottom="1.5rem",
        ),
        create_price_text(price="$0"),
        create_get_started_button(),
        background_color="#ffffff",
        height="100%",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_standard_tier_card():
    """Create a pricing card for the standard tier."""
    return rx.box(
        create_custom_heading(
            heading_level="h3",
            font_size="1.5rem",
            line_height="2rem",
            heading_text="Standard Tier",
        ),
        create_styled_text(
            text_color="#4B5563",
            margin_bottom="1.5rem",
            text_content="Enhanced access for businesses",
        ),
        rx.list(
            create_list_item_with_icon(item_text=" Increased API call limit "),
            create_list_item_with_icon(item_text=" Detailed tire specifications "),
            create_list_item_with_icon(item_text=" Pricing information "),
            create_list_item_with_icon(item_text=" Basic analytics "),
            margin_bottom="1.5rem",
        ),
        create_price_text(price="$49"),
        create_get_started_button(),
        background_color="#ffffff",
        border_width="2px",
        border_color="#3B82F6",
        height="100%",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_premium_tier_card():
    """Create a pricing card for the premium tier."""
    return rx.box(
        create_custom_heading(
            heading_level="h3",
            font_size="1.5rem",
            line_height="2rem",
            heading_text="Premium Tier",
        ),
        create_styled_text(
            text_color="#4B5563",
            margin_bottom="1.5rem",
            text_content="Full access for power users",
        ),
        rx.list(
            create_list_item_with_icon(item_text=" Unlimited API calls "),
            create_list_item_with_icon(item_text=" Comprehensive tire data "),
            create_list_item_with_icon(item_text=" Real-time pricing updates "),
            create_list_item_with_icon(item_text=" Advanced analytics "),
            create_list_item_with_icon(item_text=" Priority support "),
            margin_bottom="1.5rem",
        ),
        create_price_text(price="$99"),
        create_get_started_button(),
        background_color="#ffffff",
        height="100%",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_pricing_cards_container():
    """Create a container for all pricing tier cards."""
    return rx.flex(
        rx.box(
            create_free_tier_card(),
            margin_bottom="2rem",
            padding_left="1rem",
            padding_right="1rem",
            width=rx.breakpoints({"0px": "100%", "768px": "33.333333%"}),
        ),
        rx.box(
            create_standard_tier_card(),
            margin_bottom="2rem",
            padding_left="1rem",
            padding_right="1rem",
            width=rx.breakpoints({"0px": "100%", "768px": "33.333333%"}),
        ),
        rx.box(
            create_premium_tier_card(),
            margin_bottom="2rem",
            padding_left="1rem",
            padding_right="1rem",
            width=rx.breakpoints({"0px": "100%", "768px": "33.333333%"}),
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="center",
    )


def create_pricing_section():
    """Create the complete pricing section with title and cards."""
    return rx.box(
        rx.heading(
            "Choose Your Plan",
            font_weight="700",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            text_align="center",
            as_="h2",
        ),
        create_pricing_cards_container(),
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
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_main_content():
    """Create the main content area with hero and pricing sections."""
    return rx.box(
        rx.box(
            create_hero_section(),
            background_color="#1F2937",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        rx.box(
            create_pricing_section(),
            padding_top="5rem",
            padding_bottom="5rem",
        ),
    )


def create_email_input():
    """Create an email input field for the newsletter subscription."""
    return rx.el.input(
        type="email",
        placeholder="Enter your email",
        background_color="#374151",
        margin_bottom="0.5rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        width="100%",
    )


def create_subscribe_button():
    """Create a subscribe button for the newsletter form."""
    return rx.el.button(
        "Subscribe",
        type="submit",
        background_color="#3B82F6",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        width="100%",
    )


def create_footer_content():
    """Create the main content for the footer section."""
    return rx.flex(
        rx.box(
            create_custom_heading(
                heading_level="h3",
                font_size="1.25rem",
                line_height="1.75rem",
                heading_text="TireAPI",
            ),
            rx.text(
                "Your one-stop solution for tire information and pricing data.",
                color="#9CA3AF",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        rx.box(
            create_subheading(subheading_text="Quick Links"),
            rx.list(
                create_footer_list_item(item_text="Home"),
                create_footer_list_item(item_text="Features"),
                create_footer_list_item(item_text="Pricing"),
                create_footer_list_item(item_text="Documentation"),
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        rx.box(
            create_subheading(subheading_text="Connect"),
            rx.list(
                create_footer_list_item(item_text="Twitter"),
                create_footer_list_item(item_text="LinkedIn"),
                create_footer_list_item(item_text="GitHub"),
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        rx.box(
            create_subheading(subheading_text="Newsletter"),
            create_styled_text(
                text_color="#9CA3AF",
                margin_bottom="1rem",
                text_content="Stay updated with our latest features and news.",
            ),
            rx.form(
                create_email_input(),
                create_subscribe_button(),
            ),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        display="flex",
        flex_wrap="wrap",
    )


def create_footer():
    """Create the complete footer section with content and copyright."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text("© 2023 TireAPI. All rights reserved."),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="2rem",
            color="#9CA3AF",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        rx.logo(style={"color": "white"}),
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
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        create_header_container(),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="2rem",
            padding_bottom="2rem",
            color="#ffffff",
        ),
        class_name="font-inter",
        background_color="#F3F4F6",
    )


def create_complete_page():
    """Create the complete page including stylesheets, fonts, and all content sections."""
    return rx.fragment(
        create_page_layout(),
    )


@rx.page("/", "Api Neumaticos")
def Index() -> rx.Component:
    return create_complete_page()
