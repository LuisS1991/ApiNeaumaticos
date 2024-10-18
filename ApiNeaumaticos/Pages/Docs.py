import reflex as rx
from ApiNeaumaticos import styles
from ApiNeaumaticos.Constantes import respuesta_json


@rx.page("/doc","documentacion api")
def Docs() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.image("/Icon.png", width="5%", height="5%", margin=5),
            rx.spacer(),
            rx.link(
                "Propuesta",
                href="https://its.utu.edu.uy/wp-content/uploads/sites/33/2024/06/Proyecto-3o-EMT-Enfasis-Soporte-2024-3.pdf",
                padding=5,
                is_external=True,
                margin_rigth=3,
            ),
            rx.color_mode.button(padding=5),
            width="100%",
            direction="row",
            align="center",
            justify="between",
            padding=5,
        ),
        rx.center(
            rx.heading("Api Neumaticos", size="9"),
            width="100%",
        ),
        rx.vstack(
            rx.text(
                rx.text.strong(
                    "La presente API es parte del proyecto de fin de curos del Bachillerato de Informatica orientacion Desarrollo y Soporte."
                ),
                "Dicho servicio web sera integrado con una aplicación de administración para un parkig con gomeria.",
                _as="p",
                size="5",
            ),
            rx.text(
                "Este proyecto nos ocupa utilizar todas las habilidades en documentación,programación e implementación y mantenimiento de redes",
                _as="p",
                size="5",
            ),
              rx.text(
                "Se implemento seguridad  las rutas del proyecto. dicha seguridad es mediante JWT en la cabecera.",
                _as="p",
                size="5",
            ),
               rx.text(
                "Mediante la siguiente ruta se puede acceder a la documentación generada automaticamente mediante Suagger UI",
                _as="p",
                size="5",
            ),
            
            rx.text(
                    "Documentación Swagger UI: https://apineumaticos-production.up.railway.app/docs",
                    size="5",
                ),
            style=styles.text_aling_p,

        ),
        rx.container(
            rx.flex(
                rx.text(
                    "Ruta Principal: https://apineumaticos-production.up.railway.app",
                    size="5",
                ),
                rx.link(
                    "/pirelli",
                    href="https://apineumaticos-production.up.railway.app/pirelli",
                    is_external=True,
                    size="5",
                ),
                rx.link(
                    "/bridgestone",
                    href="https://apineumaticos-production.up.railway.app/bridgestone",
                    is_external=True,
                    size="5",
                ),
                rx.link(
                    "/michelin",
                    href="https://apineumaticos-production.up.railway.app/michelin",
                    is_external=True,
                    size="5",
                ),
                rx.text("ejemplo de respuesta:", size="5"),
                direction="column",
                spacing="5",
            ),
            rx.markdown(respuesta_json),
            width="100%",
        ),
        rx.center(
            rx.link(
                "Instituto Técnico Suparior Arias Balparda ",
                href="https://its.utu.edu.uy/",
                size="5",
            ),
            width="100%",
        ),
        rx.center(
            rx.logo(),
            margin="10px",
            width="100%",
        ),
        width="100%",
        padding="20px",
    )

""" 

    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
 """