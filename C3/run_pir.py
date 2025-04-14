from src.naive_pir import servidor_pir, cliente_construye_mascara

# Base de datos simulada (precios)
base_datos = [75, 120, 60, 90, 145]  # Por ejemplo: precios de vuelos

# Cliente desea conocer el precio del vuelo en índice 3 (90 €)
indice_deseado = 3
mascara = cliente_construye_mascara(indice_deseado, len(base_datos))

# Servidor procesa sin conocer el índice
resultado = servidor_pir(base_datos, mascara)

print(f"Precio del vuelo solicitado (índice {indice_deseado}): {resultado} €")
