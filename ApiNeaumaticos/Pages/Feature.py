import reflex as rx


def create_link(link_url, link_text):
    """Create a link element with hover effect."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover={"color": "#BFDBFE"},
    )


def create_small_heading(font_size, margin_bottom, heading_text):
    """Create a small heading with custom font size and margin."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_="h3",
    )


def create_medium_heading(font_size, margin_bottom, heading_text):
    """Create a medium-sized heading with custom font size and margin."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="2rem",
        as_="h3",
    )


def create_large_heading(heading_level, font_size, line_height, heading_text):
    """Create a large heading with custom properties."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="1.5rem",
        font_size=font_size,
        line_height=line_height,
        as_=heading_level,
    )


def create_paragraph(paragraph_text):
    """Create a paragraph with predefined styling."""
    return rx.text(
        paragraph_text,
        margin_bottom="2rem",
        font_size="1.25rem",
        line_height="1.75rem",
    )


def create_arrow_icon(icon_height, margin_left, icon_width):
    """Create a right arrow icon with custom dimensions and margin."""
    return rx.icon(
        alt="Right arrow icon",
        tag="arrow-right",
        height=icon_height,
        margin_left=margin_left,
        width=icon_width,
    )


def create_button_link(button_url, button_text):
    """Create a styled button link with an arrow icon."""
    return rx.el.a(
        button_text,
        create_arrow_icon(
            icon_height="1.25rem",
            margin_left="0.5rem",
            icon_width="1.25rem",
        ),
        href=button_url,
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#DBEAFE"},
        display="inline-flex",
        align_items="center",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#2563EB",
        font_size="1.125rem",
        line_height="1.75rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_section_title(title_text):
    """Create a centered section title."""
    return rx.heading(
        title_text,
        font_weight="700",
        margin_bottom="3rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )


def create_feature_icon(icon_alt_text, icon_tag):
    """Create a feature icon with alt text and tag."""
    return rx.icon(
        alt=icon_alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        color="#2563EB",
        width="3rem",
    )


def create_colored_text(text_color, text_content):
    """Create text with a specified color."""
    return rx.text(text_content, color=text_color)


def create_feature_box(
    icon_alt_text,
    icon_tag,
    feature_title,
    feature_description,
):
    """Create a feature box with an icon, title, and description."""
    return rx.box(
        create_feature_icon(icon_alt_text=icon_alt_text, icon_tag=icon_tag),
        create_small_heading(
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=feature_title,
        ),
        create_colored_text(
            text_color="#4B5563",
            text_content=feature_description,
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_update_description(description_text):
    """Create a description for an update with predefined styling."""
    return rx.text(
        description_text,
        margin_bottom="1rem",
        color="#4B5563",
    )


def create_learn_more_link(learn_more_url):
    """Create a 'Learn more' link with an arrow icon."""
    return rx.el.a(
        " Learn more ",
        create_arrow_icon(
            icon_height="1rem",
            margin_left="0.25rem",
            icon_width="1rem",
        ),
        href=learn_more_url,
        _hover={"text-decoration": "underline"},
        display="inline-flex",
        align_items="center",
        color="#2563EB",
    )


def create_update_box(update_title, update_description, learn_more_url):
    """Create an update box with title, description, and learn more link."""
    return rx.box(
        create_small_heading(
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=update_title,
        ),
        create_update_description(description_text=update_description),
        create_learn_more_link(learn_more_url=learn_more_url),
        background_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_per_month_span():
    """Create a '/month' text span for pricing."""
    return rx.text.span(
        "/month",
        font_weight="400",
        color="#4B5563",
        font_size="1.125rem",
        line_height="1.75rem",
    )


def create_price_text(price_amount):
    """Create a price text with '/month' suffix."""
    return rx.text(
        price_amount,
        create_per_month_span(),
        font_weight="700",
        margin_bottom="1.5rem",
        font_size="2.25rem",
        line_height="2.5rem",
    )


def create_check_icon():
    """Create a check icon for feature lists."""
    return rx.icon(
        alt="Check icon",
        tag="check",
        height="1.25rem",
        margin_right="0.5rem",
        color="#10B981",
        width="1.25rem",
    )


def create_text_span(span_text):
    """Create a text span element."""
    return rx.text.span(span_text)


def create_feature_list_item(feature_text):
    """Create a feature list item with a check icon."""
    return rx.el.li(
        create_check_icon(),
        create_text_span(span_text=feature_text),
        display="flex",
        align_items="center",
    )


def create_cta_button(button_url, button_text):
    """Create a call-to-action button with hover effect."""
    return rx.el.a(
        button_text,
        href=button_url,
        background_color="#2563EB",
        display="block",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        text_align="center",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_feature_list(feature_1, feature_2, feature_3, feature_4):
    """Create a list of features with check icons."""
    return rx.list(
        create_feature_list_item(feature_text=feature_1),
        create_feature_list_item(feature_text=feature_2),
        create_feature_list_item(feature_text=feature_3),
        create_feature_list_item(feature_text=feature_4),
        display="flex",
        flex_direction="column",
        margin_bottom="2rem",
        gap="0.5rem",
    )


def create_footer_link(link_url, link_text):
    """Create a footer link with hover effect."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )


def create_footer_list_item(link_url, link_text):
    """Create a footer list item with a link."""
    return rx.el.li(create_footer_link(link_url=link_url, link_text=link_text))


def create_social_icon(icon_alt_text, icon_tag):
    """Create a social media icon."""
    return rx.icon(
        alt=icon_alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )


def create_social_link(social_url, icon_alt_text, icon_tag):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_social_icon(icon_alt_text=icon_alt_text, icon_tag=icon_tag),
        href=social_url,
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )


def create_signup_button():
    """Create a 'Sign Up' button for the navigation bar."""
    return rx.el.a(
        "Sign Up",
        href="/login",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#DBEAFE"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#2563EB",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_navigation_bar():
    """Create the main navigation bar with logo and links."""
    return rx.flex(
        rx.flex(
            rx.image("/Icon.png", width="10%"),
            rx.center(
                rx.el.a(
                    "TireAPI",
                    href="/",
                    font_weight="700",
                    font_size="1.5rem",
                    line_height="2rem",
                ),
            ),
            gap="15px"
        ),
        rx.box(
            create_link(link_url="/", link_text="Home"),
            create_link(link_url="#features", link_text="Features"),
            create_link(link_url="/pricing", link_text="Pricing"),
            create_link(link_url="/doc", link_text="Docs"),
            create_signup_button(),
            display="flex",
            column_gap="1.5rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_header():
    """Create the page header with navigation bar."""
    return rx.box(
        rx.box(
            create_navigation_bar(),
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
            padding_top="1.5rem",
            padding_bottom="1.5rem",
        ),
        background_color="#2563EB",
        color="#ffffff",
    )


def create_hero_section():
    """Create the hero section with main heading and call-to-action."""
    return rx.box(
        rx.box(
            create_large_heading(
                heading_level="h1",
                font_size="3rem",
                line_height="1",
                heading_text="Revolutionize Your Tire Data Management",
            ),
            create_paragraph(
                paragraph_text="TireAPI provides comprehensive tire data and advanced analytics to power your automotive applications."
            ),
            create_button_link(
                button_url="/register",
                button_text=" Get Started ",
            ),
            max_width="48rem",
            margin_left="auto",
            margin_right="auto",
            text_align="center",
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
    )


def create_features_section():
    """Create the features section with key features."""
    return rx.box(
        create_section_title(title_text="Key Features"),
        rx.box(
            create_feature_box(
                icon_alt_text="Database icon",
                icon_tag="database",
                feature_title="Extensive Tire Database",
                feature_description="Access detailed information on thousands of tire models from all major manufacturers.",
            ),
            create_feature_box(
                icon_alt_text="Chart icon",
                icon_tag="bar-chart-2",
                feature_title="Advanced Analytics",
                feature_description="Gain insights with our powerful analytics tools, including performance comparisons and trend analysis.",
            ),
            create_feature_box(
                icon_alt_text="Code icon",
                icon_tag="code",
                feature_title="Easy Integration",
                feature_description="Seamlessly integrate TireAPI into your existing applications with our well-documented RESTful API.",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
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
    )


def create_updates_section():
    """Create the updates section with latest features."""
    return rx.box(
        create_section_title(title_text="Latest Updates"),
        rx.box(
            create_update_box(
                update_title="New: Tire Wear Prediction",
                update_description="Our machine learning model now predicts tire wear based on various factors, helping you optimize maintenance schedules.",
                learn_more_url="/features/tire-wear-prediction",
            ),
            create_update_box(
                update_title="Enhanced: Real-time Inventory Tracking",
                update_description="Keep track of tire inventory across multiple locations with our improved real-time tracking system.",
                learn_more_url="/features/inventory-tracking",
            ),
            max_width="48rem",
            margin_left="auto",
            margin_right="auto",
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
    )


def create_basic_plan_box():
    """Create the pricing box for the Basic plan."""
    return rx.box(
        create_medium_heading(
            font_size="1.5rem",
            margin_bottom="1rem",
            heading_text="Basic",
        ),
        create_price_text(price_amount="$0"),
        rx.list(
            create_feature_list_item(feature_text="Up to 1,000 API calls/day"),
            create_feature_list_item(feature_text="Basic analytics"),
            create_feature_list_item(feature_text="Email support"),
            display="flex",
            flex_direction="column",
            margin_bottom="2rem",
            gap="0.5rem",
        ),
        create_cta_button(
            button_url="/signup?plan=basic",
            button_text="Choose Plan",
        ),
        background_color="#ffffff",
        border_width="1px",
        border_color="#E5E7EB",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_popular_tag():
    """Create a 'Most Popular' tag for the featured pricing plan."""
    return rx.text.span(
        "Most Popular",
        class_name="transform",
        transform="translateY(-50%) translateX(-50%) translateX(-50%) translateX(-50%)",
        position="absolute",
        background_color="#2563EB",
        font_weight="700",
        left="50%",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        border_radius="9999px",
        font_size="0.875rem",
        line_height="1.25rem",
        color="#ffffff",
        top="0",
    )


def create_pro_plan_box():
    """Create the pricing box for the Pro plan."""
    return rx.box(
        create_popular_tag(),
        create_medium_heading(
            font_size="1.5rem",
            margin_bottom="1rem",
            heading_text="Pro",
        ),
        create_price_text(price_amount="$199"),
        create_feature_list(
            feature_1="Up to 10,000 API calls/day",
            feature_2="Advanced analytics",
            feature_3="Priority support",
            feature_4="Tire wear prediction",
        ),
        create_cta_button(
            button_url="/signup?plan=pro",
            button_text="Choose Plan",
        ),
        background_color="#ffffff",
        border_width="2px",
        border_color="#2563EB",
        padding="2rem",
        position="relative",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_enterprise_plan_box():
    """Create the pricing box for the Enterprise plan."""
    return rx.box(
        create_medium_heading(
            font_size="1.5rem",
            margin_bottom="1rem",
            heading_text="Enterprise",
        ),
        rx.text(
            "Custom",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="2.25rem",
            line_height="2.5rem",
        ),
        create_feature_list(
            feature_1="Unlimited API calls",
            feature_2="Custom analytics",
            feature_3="24/7 dedicated support",
            feature_4="Custom integrations",
        ),
        create_cta_button(
            button_url="/contact-sales",
            button_text="Contact Sales",
        ),
        background_color="#ffffff",
        border_width="1px",
        border_color="#E5E7EB",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_pricing_section():
    """Create the pricing section with all plan options."""
    return rx.box(
        create_section_title(title_text="Pricing Plans"),
        rx.box(
            create_basic_plan_box(),
            create_pro_plan_box(),
            create_enterprise_plan_box(),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
            max_width="64rem",
            margin_left="auto",
            margin_right="auto",
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
    )


def create_cta_section():
    """Create the call-to-action section at the bottom of the page."""
    return rx.box(
        rx.box(
            create_large_heading(
                heading_level="h2",
                font_size="1.875rem",
                line_height="2.25rem",
                heading_text="Ready to Transform Your Tire Data Management?",
            ),
            create_paragraph(
                paragraph_text="Start using TireAPI today and experience the power of comprehensive tire data and analytics."
            ),
            create_button_link(
                button_url="/login",
                button_text=" Get Started Now ",
            ),
            max_width="48rem",
            margin_left="auto",
            margin_right="auto",
            text_align="center",
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
    )


def create_main_content():
    """Create the main content of the page including all sections."""
    return rx.box(
        rx.box(
            create_hero_section(),
            background_color="#2563EB",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        rx.box(
            create_features_section(),
            id="features",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_updates_section(),
            background_color="#F9FAFB",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_pricing_section(),
            id="pricing",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_cta_section(),
            id="getstarted",
            background_color="#2563EB",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
    )


def create_footer_content():
    """Create the content for the page footer."""
    return rx.box(
        rx.box(
            create_small_heading(
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="TireAPI",
            ),
            create_colored_text(
                text_color="#9CA3AF",
                text_content="Empowering the automotive industry with comprehensive tire data and analytics.",
            ),
        ),
        rx.box(
            create_small_heading(
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Quick Links",
            ),
            rx.list(
                create_footer_list_item(link_url="/", link_text="Home"),
                create_footer_list_item(
                    link_url="/features",
                    link_text="Features",
                ),
                create_footer_list_item(link_url="/pricing", link_text="Pricing"),
                create_footer_list_item(
                    link_url="/docs",
                    link_text="Documentation",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        rx.box(
            create_small_heading(
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Support",
            ),
            rx.list(
                create_footer_list_item(link_url="/faq", link_text="FAQ"),
                create_footer_list_item(
                    link_url="/contact",
                    link_text="Contact Us",
                ),
                create_footer_list_item(
                    link_url="/status",
                    link_text="API Status",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        rx.box(
            create_small_heading(
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Follow Us",
            ),
            rx.flex(
                create_social_link(
                    social_url="https://twitter.com/tireapi",
                    icon_alt_text="Twitter icon",
                    icon_tag="twitter",
                ),
                create_social_link(
                    social_url="https://linkedin.com/company/tireapi",
                    icon_alt_text="LinkedIn icon",
                    icon_tag="linkedin",
                ),
                create_social_link(
                    social_url="https://github.com/tireapi",
                    icon_alt_text="GitHub icon",
                    icon_tag="github",
                ),
                display="flex",
                column_gap="1rem",
            ),
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(4, minmax(0, 1fr))",
            }
        ),
    )


def create_footer():
    """Create the page footer with content and copyright notice."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text("© 2023 TireAPI. All rights reserved."),
            border_color="#374151",
            border_top_width="1px",
            margin_top="3rem",
            padding_top="2rem",
            text_align="center",
            color="#9CA3AF",
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
    )


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        create_header(),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="3rem",
            padding_bottom="3rem",
            color="#ffffff",
        ),
        background_color="#F3F4F6",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
    )


@rx.page("/features", "Api Neumaticos")
def Features():
    """Create the complete page with necessary styles and content."""
    return rx.fragment(
        create_page_layout(),
    )
