# ------ FastAPI -------------
from fastapi import APIRouter, status, Body
# ------ Libraries -----------
from config.MongoDB import db
from bson import ObjectId
# ------ Dependencies -------
from models.SitiosModel import Sitio
from schemas.SitioSchema import *

sitio = APIRouter()

@sitio.post("/sitios",
            tags = ["Sitios"],
            status_code = status.HTTP_201_CREATED,
            response_model=list[Sitio])
async def crearSitio(sitio: Sitio = Body(...)):
    nuevoSitio = dict(sitio)
    db.Sitios.insert_one(nuevoSitio)
    #status en caso de fallo
    return sitio

@sitio.get("/sitios",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
           )
async def get_all_sitios():
    all_sitios = db.Sitios.find()
    return sitios_all(all_sitios)


@sitio.get("/sitios/{id}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=Sitio
           )
async def get_sitio(id: str):
    sitio = db.Sitios.find_one({'_id': ObjectId(id)})
    return sitio_entity(sitio)

@sitio.get("/sitios/{sede}/{bloque}/{piso}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
        )
async def get_sitio_for(sede: str, bloque: str, piso: str):
    sitios = db.Sitios.find()
    return filter_for(sitios_all(sitios), sede, bloque, piso)