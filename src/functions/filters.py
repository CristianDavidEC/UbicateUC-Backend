def filtro_tipo(value):
    return value


def filtro_nombre(value):
    return {'$regex': value}


filtros = {
    "tipo": filtro_tipo,
    "nombre": filtro_nombre
}
