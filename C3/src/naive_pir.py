import numpy as np

def servidor_pir(base_datos, consulta_enmascarada):
    """Recibe una base de datos y una máscara binaria. Devuelve el resultado del PIR."""
    assert len(base_datos) == len(consulta_enmascarada), "Dimensiones incompatibles"
    return int(np.dot(base_datos, consulta_enmascarada))

def cliente_construye_mascara(indice, longitud):
    """Devuelve una máscara binaria con un 1 en la posición deseada"""
    mascara = [0] * longitud
    mascara[indice] = 1
    return mascara