import jwt
import time
from jwt import PyJWTError
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from ApiNeaumaticos.Constantes import SECRET_KEY, ALGORITHM
from ApiNeaumaticos.Controllers import UserConroller

oauth2 = OAuth2PasswordBearer(tokenUrl="token")


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Token Expiro"
    )
    tokenExistDb = buscar_token_bd(token)
    if tokenExistDb is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Token no existe"
        )
    try:
        result = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if result is None:
            raise exception
        return result
    except PyJWTError:
        raise exception


async def valid_user(tokenUser: any = Depends(auth_user)):
    if validar_fecha(tokenUser["exp"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Token Expiro"
        )


def validar_fecha(fecha_validar):
    # Obtener el timestamp actual
    current_time = int(time.time())
    # Verificar si la fecha es vigente
    if fecha_validar > current_time:
        return False
    else:
        return True


def buscar_token_bd(token: str):
    _usuarioController = UserConroller()
    return _usuarioController.GetUserToken(token)
