import reflex as rx
import time
from typing import List
from ApiNeaumaticos.Models.TokenApi import TokenApi
from ApiNeaumaticos.Auth.Login import LoginState
from ApiNeaumaticos.Controllers.DashboardController import DashboardController
from ApiNeaumaticos.Utils.CreateToken import GenerarTokenAcces


class DashboardState(rx.State):
    _dashController = DashboardController()
    username: str = ""
    current_user: str
    show_key_input: bool = False
    mensaje = ""
    tokenList: List[TokenApi] = []
    idSelectedShowKey = 0
    show: bool = False

    async def onLoad(self):
        self.mensaje = ""
        self.show = False
        login_state = await self.get_state(LoginState)
        self.current_user = login_state.userId
        self.username = login_state.username
        self.loadKeys()

    def loadKeys(self):
        self.tokenList = self._dashController.GetCurrentUser(self.current_user)

    def ShowKey(self, value):
        self.show_key_input = not self.show_key_input
        self.idSelectedShowKey = 0 if not self.show_key_input else value

    def GenerarKey(self):
        token = TokenApi(
            token=self.generar_clave_secreta(),
            userId=self.current_user,
            apiName="API de Neumáticos",
        )
        self._dashController.GuardarKey(token)
        self.mensaje = "¡Seceret Key Generada Correctamente!"
        self.ShowAlert()
        self.tokenList.append(token)

    def UpdateToken(self, tokenId):
        if self._dashController.UpdateKey(tokenId):
            self.loadKeys()
            self.mensaje = "¡Seceret Key Actualizada Correctamente!"
            self.ShowAlert()

    def DeleteKey(self, tokenId):
        if self._dashController.DeleteKey(tokenId):
            self.loadKeys()

    def Copykey(self, secret_key):
        self.mensaje = "copiado correctamente"
        self.ShowAlert()
        return rx.set_clipboard(secret_key)

    def generar_clave_secreta(self):
        return GenerarTokenAcces(self.current_user)

    def ShowAlert(self):
        self.show = True

    def CloseAlert(self):
        self.show = False
