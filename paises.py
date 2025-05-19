codigo_paises = {
    "EC": "Ecuador",
    "CO": "Colombia",
    "PE": "Peru",
    "US": "Estados Unidos",
    "MX": "México",
    "CA": "Canada",
    "AR": "Argentina",
    "BR": "Brasil",
    "ES": "Espana",
}

def pais_id(id):
    codigo = id[:2]
    return codigo_paises.get(codigo)