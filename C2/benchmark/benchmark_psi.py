import time
import random
from src.psi_hash import identificar_comunes

def generar_dnis(n, prefijo="DNI"):
    """Genera n DNIs aleatorios únicos."""
    return [f"{prefijo}{random.randint(10000000, 99999999)}" for _ in range(n)]

# Generar 10.000 pasajeros únicos
pasajeros = generar_dnis(10000)

# Generar 5.000 delincuentes, de los cuales 10 están entre los pasajeros
delincuentes = pasajeros[:10] + generar_dnis(4990)

# Benchmark
start_time = time.time()
coincidentes = identificar_comunes(pasajeros, delincuentes)
total_time = time.time() - start_time

# Resultados
print("\n--- Benchmark PSI actualizado ---")
print(f"Pasajeros procesados: {len(pasajeros)}")
print(f"Delincuentes procesados: {len(delincuentes)}")
print(f"Coincidencias detectadas: {len(coincidentes)}")
print(f"Tiempo total de ejecución: {round(total_time, 3)} segundos")

# Ejemplo de salida
if len(coincidentes) > 0:
    print(f"Ejemplo de coincidencias detectadas: {coincidentes[:5]}")
