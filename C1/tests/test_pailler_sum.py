import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import paillier_sum

def test_suma_homomorfica_correcta():
    gastos = [100, 200, 300, 400, 500]
    pub, priv = paillier_sum.generar_claves()
    cifrados = paillier_sum.cifrar_lista(pub, gastos)
    suma_cifrada = paillier_sum.sumar_cifrados(cifrados)
    resultado = paillier_sum.descifrar(priv, suma_cifrada)
    assert resultado == sum(gastos)

def test_privacidad_de_cifrado():
    gastos = [1234]
    pub, priv = paillier_sum.generar_claves()
    cifrado = paillier_sum.cifrar_lista(pub, gastos)[0]
    with pytest.raises(AttributeError):
        _ = cifrado.raw_value  # raw_value no debe existir

def test_carga_masiva():
    gastos = list(range(1, 10001))
    pub, priv = paillier_sum.generar_claves()
    cifrados = paillier_sum.cifrar_lista(pub, gastos)
    suma_cifrada = paillier_sum.sumar_cifrados(cifrados)
    resultado = paillier_sum.descifrar(priv, suma_cifrada)
    assert resultado == sum(gastos)
