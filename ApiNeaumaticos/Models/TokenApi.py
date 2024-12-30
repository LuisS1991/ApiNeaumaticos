import reflex as rx


class TokenApi(rx.Model, table=True):
    token: str
    userId: int
    apiName: str
