from ApiNeaumaticos.Models.TokenApi import TokenApi
from ApiNeaumaticos.Utils.CreateToken import GenerarTokenAcces
import reflex as rx


class DashboardController:
    def __init__(self):
        self.tokenList = []

    def GetCurrentUser(self, current_user):
        with rx.session() as session:
            self.tokenList = session.exec(
                TokenApi.select().where(TokenApi.userId == current_user)
            ).all()
        return self.tokenList

    def UpdateKey(self, tokenId):
        token = None
        with rx.session() as session:
            token = session.exec(
                TokenApi.select().where(TokenApi.id == tokenId)
            ).first()
            if token is None:
                return False
            else:
                token.token = GenerarTokenAcces(token.userId)
                session.add(token)
                session.commit()
                return True

    def DeleteKey(self, tokenId):
        token = None
        with rx.session() as session:
            token = session.exec(
                TokenApi.select().where(TokenApi.id == tokenId)
            ).first()
            if token is None:
                return False
            else:
                session.delete(token)
                session.commit()
            return True

    def GuardarKey(self, token):
        with rx.session() as session:
            session.add(token)
            session.commit()
            session.refresh(token)
