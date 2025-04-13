from src import paillier_sum

gastos = [250, 1200, 80, 430, 1500]
pub_key, priv_key = paillier_sum.generar_claves()

cifrados = paillier_sum.cifrar_lista(pub_key, gastos)
suma_cifrada = paillier_sum.sumar_cifrados(cifrados)
resultado = paillier_sum.descifrar(priv_key, suma_cifrada)

print(f"Gastos: {gastos}")
print(f"Suma desencriptada: {resultado}")