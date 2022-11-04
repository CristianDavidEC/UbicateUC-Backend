# ------ FastAPI -------------
from fastapi import APIRouter, status, Body
# ------ Libraries -----------
from config.MongoDB import db
from fastapi import APIRouter, status
# ------ Dependencies -------
from models.SitiosModel import Sitio
from schemas.SitioSchema import *
from schemas.SitioSchema import sitio_entity, sitios_all
#from handlers.SitesHandlers import get_all_sites, get_filter_sites_by_name, get_site, get_filter_sites_by_bloque_piso_sede
from handlers.SitesHandlers import *

sitio = APIRouter()

@sitio.post("/sitios",
            tags = ["Sitios"],
            status_code = status.HTTP_201_CREATED,
            response_model=list[Sitio])
async def crearSitio(sitio: Sitio = Body(...)):
    sitio_return = createSite(sitio)
    #status en caso de fallo
    return [sitio_entity(sitio_return)]

@sitio.get("/sitios/",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
           )
async def get_all_sitios(tipo: str = None, nombre: str = None):
    all_sitios = get_all_sites(tipo, nombre)
    return sitios_all(all_sitios)


@sitio.get("/sitios/{id}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=Sitio
           )
async def get_sitio(id: str):
    sitio = get_site(id)
    return sitio_entity(sitio)

@sitio.get("/sitios-by-block-sede-piso/",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
        )
async def get_sitio_for(sede: str, bloque: str, piso: str):
    sitios = get_filter_sites_by_sede_bloque_piso(sede, bloque, piso)
    return sitios_all(sitios)

@sitio.get("/sitios-by-name/{name}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           )
async def get_sitio_by_name(name: str):
    sitios = get_filter_sites_by_name(name)
    return sitios_all(sitios)

@sitio.get("/sitios-by-piso/{piso}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           )
async def get_sitio_by_name(piso: str):
    sitios = get_filter_sites_by_piso(piso)
    return sitios_all(sitios)

@sitio.get("/", tags=["Default"], status_code=status.HTTP_200_OK)
async def get_nan():
    return ""

