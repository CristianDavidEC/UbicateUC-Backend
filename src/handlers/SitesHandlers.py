from config.MongoDB import db
from bson import ObjectId
from functions.filters import filtros


def get_all_sites(object_query):
    items_inquiry = {}
    for key, value in object_query.items():
        if value != '':
            function_filtro = filtros[key]
            items_inquiry[key] = function_filtro(value)

    all_sitios = db.Sitios.find(items_inquiry)

    return all_sitios


def get_site(id):
    sitio = db.Sitios.find_one({'_id': ObjectId(id)})
    return sitio


def createSite(sitio):
    nuevoSitio = dict(sitio)
    db.Sitios.insert_one(nuevoSitio)
    return nuevoSitio
