"""Styles for the app."""

import reflex as rx

stylesheet_url=["https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap", "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"]

accent_text_color = rx.color("accent", 10)

markdown_style = {
    "code": lambda text: rx.code(text, color_scheme="gray"),
    "codeblock": lambda text, **props: rx.code_block(text, **props, margin_y="1em"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        text_decoration="underline",
        text_decoration_color=accent_text_color,
    ),
}


text_aling_p = {
    "aling_items": "center",
    "text_align": "center",
    "padding": "30px",
    "margin": "50px",
    "font_size": "20px",
}
