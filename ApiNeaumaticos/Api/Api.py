import json
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from ApiNeaumaticos.Api.AuthJtw import valid_user

from ApiNeaumaticos.Servicios import (
    PirelliServices,
    BridgestoneServices,
    MichelinServices,
)
from ApiNeaumaticos.Constantes import (
    headers,
    pirelli_url,
    michelin_url,
    bridgestone_url,
)

router = APIRouter(
    prefix="/proveedor",
    tags=["jwtauth"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}},
)


servPirelli = PirelliServices(pirelli_url, headers)
servBristone = BridgestoneServices(bridgestone_url, headers)
servMichelin = MichelinServices(michelin_url, headers)


"""
async def api_neumaticos_pirelli():
    return servPirelli.PeticionGet()
async def api_neumaticos_bgristone():
    return servBristone.PeticionGet()
async def api_neumaticos_michelin():
    return servMichelin.PeticionGet()
"""


async def raiz():
    return RedirectResponse("/ping")


@router.get("/michelin")
async def api_neumaticos_michelin_file(token = Depends(valid_user)):
    return read_file("Data/michelin.json")


@router.get("/pirelli")
async def api_neumaticos_pirelli_file(token = Depends(valid_user)):
    return read_file("Data/pirelli.json")


@router.get("/bridgestone")
async def api_neumaticos_bgristone_file(token = Depends(valid_user)):
    return read_file("Data/bridgestone.json")


def read_file(path) -> json:
    with open(path, "r", encoding="UTF-8") as data:
        response = json.load(data)
        return response
