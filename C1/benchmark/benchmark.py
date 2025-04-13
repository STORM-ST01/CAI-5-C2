import time
import random
from phe import paillier
import pandas as pd

NUM_GASTOS = 10000
VALOR_MAXIMO = 10000

start_time = time.time()
public_key, private_key = paillier.generate_paillier_keypair(n_length=2048)
keygen_time = time.time() - start_time

gastos = [random.randint(1, VALOR_MAXIMO) for _ in range(NUM_GASTOS)]

start_time = time.time()
gastos_cifrados = [public_key.encrypt(x) for x in gastos]
cifrado_time = time.time() - start_time

start_time = time.time()
suma_cifrada = sum(gastos_cifrados)
suma_time = time.time() - start_time

start_time = time.time()
suma_total = private_key.decrypt(suma_cifrada)
descifrado_time = time.time() - start_time

print("\n--- Resultados de Prueba Homomórfica ---")
print(f"Número de elementos: {NUM_GASTOS}")
print(f"Suma esperada: {sum(gastos)}")
print(f"Suma desencriptada: {suma_total}")
print(f"Coincide: {'✅' if suma_total == sum(gastos) else '❌'}")
print(f"Tiempo generación de claves: {keygen_time:.2f}s")
print(f"Tiempo cifrado: {cifrado_time:.2f}s")
print(f"Tiempo suma cifrada: {suma_time:.2f}s")
print(f"Tiempo descifrado: {descifrado_time:.2f}s")

df = pd.DataFrame([{
    "num_elementos": NUM_GASTOS,
    "suma_esperada": sum(gastos),
    "suma_descifrada": suma_total,
    "clave_bits": 2048,
    "tiempo_clave_s": round(keygen_time, 3),
    "tiempo_cifrado_s": round(cifrado_time, 3),
    "tiempo_suma_s": round(suma_time, 3),
    "tiempo_descifrado_s": round(descifrado_time, 3),
    "resultado_correcto": suma_total == sum(gastos)
}])
df.to_csv("resultados_pruebas_paillier.csv", index=False)
