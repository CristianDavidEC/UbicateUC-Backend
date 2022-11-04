from config.MongoDB import db
from bson import ObjectId


def get_all_sites(tipo, nombre):
    items_inquiry = {}

    if tipo:
        items_inquiry['tipo'] = tipo

    if nombre:
        items_inquiry['nombre'] = {'$regex': nombre}

    all_sitios = db.Sitios.find(items_inquiry)
    return all_sitios


def get_site(id):
    sitio = db.Sitios.find_one({'_id': ObjectId(id)})
    return sitio

def get_filter_sites_by_name(name):
    all_sitios = db.Sitios.find({"nombre": {'$regex': name}})
    return list(all_sitios)

def get_filter_sites_by_sede_bloque_piso(sede, bloque, piso):

    items_query = {}

    if sede:
        items_query['sede'] = sede

    if bloque:
        items_query['bloque'] = bloque
    
    if piso:
        items_query['piso'] = piso

    all_sitios = db.Sitios.find(items_query)
    return all_sitios

def createSite(sitio):
    nuevoSitio = dict(sitio)
    db.Sitios.insert_one(nuevoSitio)
    return nuevoSitio

def get_filter_sites_by_piso(piso):
    sitios = db.Sitios.find({"piso": {'$regex': piso}})
    return list(sitios)