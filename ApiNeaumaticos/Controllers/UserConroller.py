import reflex as rx
from sqlmodel import select
from ApiNeaumaticos.Models.TokenApi import TokenApi
from ApiNeaumaticos.Models.CurrentUser import CurrentUser
from ApiNeaumaticos.Auth.User import LocalUser


class UserConroller:
    def __init__(self):
        self.tokenApi: TokenApi = None

    def UpdateUser(self, currentUser: CurrentUser):
        user_bd = None
        with rx.session() as session:
            user_bd = session.exec(
                select(LocalUser).where(LocalUser.id == currentUser.userId)
            ).one_or_none()
            user_bd.username = currentUser.userName
            user_bd.email = currentUser.email
            user_bd.password_hash = LocalUser.hash_password(currentUser.password)
            session.add(user_bd)
            session.commit()

    def DeleteUser(self, idUser):
        user_bd = None
        with rx.session() as session:
            user_bd = session.exec(
                select(LocalUser).where(LocalUser.id == idUser)
            ).one_or_none()
        user_bd.enabled = False
        session.add(user_bd)
        session.commit()

    def GetUser(self, id):
        user_bd = None
        with rx.session() as session:
            user_bd = session.exec(LocalUser.select().where(LocalUser.id == id)).first()
        return CurrentUser(
            userId=user_bd.id,
            userName=user_bd.username,
            email=user_bd.email,
            enabled=user_bd.enabled,
            password="",
        )

    def GetUserToken(self, current_token):
        with rx.session() as session:
            self.tokenApi = session.exec(
                TokenApi.select().where(TokenApi.token == current_token)
            ).first()
        return self.tokenApi
