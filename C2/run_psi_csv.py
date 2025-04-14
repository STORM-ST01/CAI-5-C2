import pandas as pd
from src.psi_hash import identificar_comunes

df_pasajeros = pd.read_csv("datos/pasajeros.csv")
df_delincuentes = pd.read_csv("datos/delincuentes.csv")

pasajeros = df_pasajeros["DNI"].tolist()
delincuentes = df_delincuentes["DNI"].tolist()

comunes = identificar_comunes(pasajeros, delincuentes)

# Guardar los DNIs coincidentes en un CSV
df_resultado = pd.DataFrame({"DNI_detectado": comunes})
df_resultado.to_csv("resultado_detectados.csv", index=False)

print("Coincidencias encontradas:")
print(df_resultado)
