def filtro_nombre(value):
    return {'$regex': value}


def filtro_property(value):
    return value


filtros = {
    "tipo": filtro_property,
    "nombre": filtro_nombre,
    "bloque": filtro_property,
    "piso": filtro_property
}
