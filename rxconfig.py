import reflex as rx

config = rx.Config(
    app_name="ApiNeaumaticos",
    db_url="sqlite:///reflexUser.db",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://api-neaumaticos.vercel.app",
    ],
)
"""
    api_url="https://apineumaticos-production.up.railway.app" https://apineaumaticos-production.up.railway.app/proveedor/pirelli
cors_allowed_origins=[
    "https://docs-api-neumaticos.vercel.app/"
    "*"
], """
