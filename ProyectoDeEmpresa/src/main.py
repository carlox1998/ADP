from pathlib import Path
import pandas as pd

# 1. Localizar la carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Localizar el archivo Excel
archivo = (
    BASE_DIR
    / "datos"
    / "INE.xlsx"
)

# 3. Comprobar que el archivo existe
if not archivo.exists():
    raise FileNotFoundError(
        f"No se encuentra el archivo: {archivo}"
    )

# 4. Leer el Excel
poblacion = pd.read_excel(archivo)

# 5. Mostrar información inicial
print("\n=== PRIMER ANÁLISIS DE Poblacion ===")

print("\nColumnas del archivo:")
print(poblacion.columns.tolist())

print("\nPrimeras cinco datos:")
print(poblacion.head(6).to_string(index=False))

print("\nDimensiones del conjunto de datos:")
print(f"Reservas: {poblacion.shape[0]}")
print(f"Columnas: {poblacion.shape[2]}")

print("\nTipos de datos:")
print(poblacion.dtypes)

# 6. Analizar el estado de las reservas
if "1 de enero de 2025" in poblacion.columns:
    print("\nEdades en Enero:")
    print(poblacion["1 de enero de 2025"].value_counts(dropna=False))

# 7. Analizar las habitaciones
if "1 de julio de 2024" in poblacion.columns:
    print("\n:")
    print(
        poblacion["1 de julio de 2024"]
        .value_counts(dropna=False)
    )

print("\n=== FIN DEL ANÁLISIS ===")