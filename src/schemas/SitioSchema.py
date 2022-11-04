def sitio_entity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'nombre': item['nombre'],
        'descripcion': item['descripcion'],
        'latitud': item['latitud'],
        'longitud': item['longitud'],
        'tipo': item['tipo'],
        'sede': item['sede'],
        'estado': item['estado'],
        'bloque': item['bloque'],
        'piso': item['piso']
    }

def sitio(item) -> list:
    return [sitio_entity(item)]

def sitios_all(items) -> list:
    return [sitio_entity(item) for item in items]

def filter_for(items, sede, bloque, piso) -> list:
    return [sitio_entity(item) for item in items if (item["sede"] == sede and item["bloque"] == bloque and item["piso"] == piso)]

