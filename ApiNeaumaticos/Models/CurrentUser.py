import reflex as rx


class CurrentUser(rx.Base):
    userId: int
    userName: str
    email: str
    enabled: bool
    password:str