import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.psi_hash import identificar_comunes

def test_interseccion_correcta_dnis():
    pasajeros = ['DNI1', 'DNI2', 'DNI3']
    delincuentes = ['DNI3', 'DNI4']
    comunes = identificar_comunes(pasajeros, delincuentes)
    assert comunes == ['DNI3']

def test_sin_coincidencias_dnis():
    pasajeros = ['DNI10', 'DNI20']
    delincuentes = ['DNI30', 'DNI40']
    comunes = identificar_comunes(pasajeros, delincuentes)
    assert comunes == []

def test_conjuntos_vacios_dnis():
    assert identificar_comunes([], []) == []
    assert identificar_comunes(['DNI1'], []) == []
    assert identificar_comunes([], ['DNI1']) == []

def test_varios_comunes():
    pasajeros = ['DNIa', 'DNIb', 'DNIc', 'DNId']
    delincuentes = ['DNIx', 'DNIb', 'DNId', 'DNIz']
    comunes = identificar_comunes(pasajeros, delincuentes)
    assert sorted(comunes) == sorted(['DNIb', 'DNId'])

