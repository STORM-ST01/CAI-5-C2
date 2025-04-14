import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.naive_pir import servidor_pir, cliente_construye_mascara

def test_pir_indice_central():
    base_datos = [100, 200, 300, 400, 500]
    indice = 2
    mascara = cliente_construye_mascara(indice, len(base_datos))
    resultado = servidor_pir(base_datos, mascara)
    assert resultado == 300

def test_pir_primero_y_ultimo():
    base_datos = [11, 22, 33, 44, 55]
    mascara_ini = cliente_construye_mascara(0, 5)
    mascara_fin = cliente_construye_mascara(4, 5)
    assert servidor_pir(base_datos, mascara_ini) == 11
    assert servidor_pir(base_datos, mascara_fin) == 55

def test_mascara_invalida_levanta_excepcion():
    base_datos = [1, 2, 3]
    mascara = [0, 1]  # Dimensión incorrecta
    try:
        servidor_pir(base_datos, mascara)
    except AssertionError as e:
        assert "Dimensiones incompatibles" in str(e)
