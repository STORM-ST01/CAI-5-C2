import hashlib

def hash_set(dataset):
    """Devuelve un diccionario {hash: valor original}."""
    return {hashlib.sha256(x.encode()).hexdigest(): x for x in dataset}

def intersectar_hashes(set1, set2):
    """Devuelve los hashes comunes entre dos diccionarios."""
    return set(set1.keys()).intersection(set2.keys())

def identificar_comunes(pasajeros, delincuentes):
    """
    Devuelve la lista de DNIs reales de delincuentes que están también en la lista de pasajeros.
    """
    hashed_pasajeros = hash_set(pasajeros)
    hashed_delincuentes = hash_set(delincuentes)

    comunes_hashes = intersectar_hashes(hashed_pasajeros, hashed_delincuentes)

    # Devolver los DNIs reales (según la base de datos de la autoridad)
    return [hashed_delincuentes[h] for h in comunes_hashes]

