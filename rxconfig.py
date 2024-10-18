import reflex as rx

config = rx.Config(
    app_name="ApiNeaumaticos", 
    db_url="sqlite:///reflexUser.db",
    api_url="https://apineumaticos-production.up.railway.app" 
)
"""
"http://app.example.com:8000",
cors_allowed_origins=[
    "https://docs-api-neumaticos.vercel.app/"
    "*"
], """
