# ------ FastAPI -------------
from bson import ObjectId
# ------ Libraries -----------
from config.MongoDB import db
from fastapi import APIRouter, status
# ------ Dependencies -------
from models.SitiosModel import Sitio
from schemas.SitioSchema import sitio_entity, sitios_all
from handlers.SitesHandlers import get_all_sites, get_filter_sites_by_name, get_site

sitio = APIRouter()


@sitio.get("/sitios/",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
           )
async def get_all_sitios(tipo: str = '', nombre: str = ''):
    object_query = {
        "tipo": tipo,
        "nombre": nombre
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


@sitio.get("/sitios-by-name/{name}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           )
async def get_sitio_by_name(name: str):
    sitios = get_filter_sites_by_name(name)
    return sitios_all(sitios)


@sitio.get("/", tags=["Default"], status_code=status.HTTP_200_OK)
async def get_nan():
    return ""
