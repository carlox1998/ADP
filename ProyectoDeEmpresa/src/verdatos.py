from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1. Definir la ruta del archivo Excel
BASE_DIR = Path(__file__).resolve().parent.parent
archivo_excel = BASE_DIR / "datos" / "INE_Columna_B2.xlsx"

# Si el archivo está en la misma carpeta que el script, usar la ruta directa
if not archivo_excel.exists():
    archivo_excel = BASE_DIR / "INE_Columna_B2.xlsx"

if not archivo_excel.exists():
    raise FileNotFoundError(f"No se encuentra el archivo en: {archivo_excel}")

# 2. Leer los datos desde Excel
df = pd.read_excel(archivo_excel)

# 3. Limpieza y preparación de datos
# Obtener la columna de datos (si tiene nombre o tomar la primera/segunda)
col_datos = df.columns[-1]

# Eliminar valores nulos o vacíos
df_clean = df.dropna(subset=[col_datos]).copy()

# Convertir la columna a valores numéricos
df_clean[col_datos] = pd.to_numeric(df_clean[col_datos], errors="coerce")
df_clean = df_clean.dropna(subset=[col_datos])

# 4. Configurar la figura con Matplotlib
plt.figure(figsize=(12, 6))

# Dibujar gráfico de línea con área rellenada
plt.plot(
    df_clean.index,
    df_clean[col_datos],
    color="#1f77b4",
    linewidth=2,
    label="Población / Registro (Columna B)"
)
plt.fill_between(
    df_clean.index,
    df_clean[col_datos],
    color="#1f77b4",
    alpha=0.15
)

# 5. Personalización del gráfico
plt.title("Visualización de Datos - INE Columna B", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Índice de Registro / Fila", fontsize=11)
plt.ylabel("Habitantes / Personas", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)

# Formatear el eje Y con separadores de miles
ax = plt.gca()
ax.yaxis.set_major_formatter("{x:,.0f}")

plt.legend(loc="upper right")
plt.tight_layout()

# 6. Guardar la imagen y mostrar la gráfica
imagen_salida = BASE_DIR / "grafico_poblacion_INE.png"
plt.savefig(imagen_salida, dpi=300)
print(f" Gráfico guardado exitosamente en: {imagen_salida}")

plt.show()