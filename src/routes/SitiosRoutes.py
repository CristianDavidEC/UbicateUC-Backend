# ------ FastAPI -------------
from fastapi import APIRouter, status, Body
# ------ Libraries -----------
from config.MongoDB import db
from fastapi import APIRouter, status
# ------ Dependencies -------
from models.SitiosModel import Sitio
from schemas.SitioSchema import *
from schemas.SitioSchema import sitio_entity, sitios_all
from handlers.SitesHandlers import *

sitio = APIRouter()

@sitio.post("/sitios",
            tags = ["Sitios"],
            status_code = status.HTTP_201_CREATED,
            response_model=list[Sitio])
async def crearSitio(sitio: Sitio = Body(...)):
    sitio_return = createSite(sitio)
    return [sitio_entity(sitio_return)]

@sitio.get("/sitios",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
           )
async def get_all_sitios(tipo: str = '', nombre: str = '', bloque: str = '', piso: str = ''):
    object_query = {
        "tipo": tipo,
        "nombre": nombre,
        "bloque": bloque,
        "piso": piso
    }
    all_sitios = get_all_sites(object_query)
    return sitios_all(all_sitios)


@sitio.get("/sitios/{id}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=Sitio
           )
async def get_sitio(id: str):
    sitio = get_site(id)
    return sitio_entity(sitio)


@sitio.get("/", tags=["Default"], status_code=status.HTTP_200_OK)
async def get_nan():
    return ""

