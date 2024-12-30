import reflex as rx
from ApiNeaumaticos.Auth.Login import LoginState
from ApiNeaumaticos.Models.CurrentUser import CurrentUser
from ApiNeaumaticos.Controllers import UserConroller


class UserState(rx.State):
    curret_user: CurrentUser = None
    _userController = UserConroller()
    userName: str = ""
    email: str = ""
    show: bool = False

    async def onLoad(self):
        login_state = await self.get_state(LoginState)
        self.curret_user = self._userController.GetUser(login_state.userId)
        self.userName = self.curret_user.userName
        self.email = self.curret_user.email
        self.show = False

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.curret_user.userName = form_data["username"]
        self.curret_user.email = form_data["email"]
        self.curret_user.password = form_data["password"]
        self._userController.UpdateUser(self.curret_user)
        self.show = not (self.show)

    def deleteUser(self):
        self._userController.DeleteUser(self.curret_user.userId)
        self.show = not (self.show)

    def CloseAlert(self):
        self.show = False
