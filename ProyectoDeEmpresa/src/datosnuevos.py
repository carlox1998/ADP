from pathlib import Path
import pandas as pd

# 1. Localizar la carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Localizar el archivo Excel
archivo = BASE_DIR / "datos" / "INE.xlsx"

# 3. Comprobar que el archivo existe
if not archivo.exists():
    raise FileNotFoundError(f"No se encuentra el archivo: {archivo}")

# 4. Leer el Excel sin cabecera predefinida para manejar las celdas directamente
df = pd.read_excel(archivo, header=None)

# 5. Extraer a partir de la fila 13 (En Excel la fila 13 equivale al índice 12 en Python)
# Columna A = índice 0, Columna B = índice 1
datos_b13_en_adelante = df.iloc[12:, [0, 1]].copy()

# Renombrar columnas para una lectura más limpia
datos_b13_en_adelante.columns = ["Etiqueta / Concepto (Col A)", "Valor (Col B)"]

# Eliminar filas donde la columna B esté completamente vacía
datos_b13_en_adelante = datos_b13_en_adelante.dropna(subset=["Valor (Col B)"])

# 6. Mostrar el resultado bien estructurado
print("\n" + "=" * 65)
print("       DATOS EXTRAÍDOS DEL ARCHIVO INE.xlsx (DESDE B13)       ")
print("=" * 65)

# Mostrar la tabla formateada en consola
print(datos_b13_en_adelante.to_string(index=False))

print("=" * 65)
print(f"Total de registros encontrados desde B13: {len(datos_b13_en_adelante)}")
print("=" * 65 + "\n")

from pathlib import Path
import pandas as pd

# 1. Localizar la carpeta principal del proyecto y la carpeta de datos
BASE_DIR = Path(__file__).resolve().parent.parent
DIR_DATOS = BASE_DIR / "datos"

# 2. Localizar el archivo de origen y definir el archivo de salida
archivo_origen = DIR_DATOS / "INE.xlsx"
archivo_salida = DIR_DATOS / "INE_Columna_B2.xlsx"

# 3. Comprobar que el archivo existe
if not archivo_origen.exists():
    raise FileNotFoundError(f"No se encuentra el archivo: {archivo_origen}")

# 4. Leer el archivo Excel sin cabecera
df = pd.read_excel(archivo_origen, header=None)

# 5. Extraer a partir de la fila 13 (índice 12 en Python) de las columnas A y B
datos_b13 = df.iloc[12:, [1]].copy()
datos_b13.columns = ["Valor Columna B"]

# Eliminar celdas vacías en la columna B
#datos_b13 = datos_b13.dropna(subset=["Valor Columna B"])

# 6. Guardar el resultado en un nuevo archivo .xlsx en la propia carpeta
datos_b13.to_excel(archivo_salida, index=False)

print("\n" + "=" * 60)
print(f"¡Proceso completado con éxito!")
print(f"Se han guardado {len(datos_b13)} filas en:")
print(f" -> {archivo_salida}")
print("=" * 60 + "\n")