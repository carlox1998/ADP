#Pathlib es una librería que nos permite trabajar con rutas de archivos y directorios de manera más sencilla y legible.
from pathlib import Path

#Pandas es una librería de Python que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar.
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_CSV = BASE_DIR / "datos" / "IBEX 35 (IBEX).csv"


def main() -> None :
    if not ARCHIVO_CSV.exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {ARCHIVO_CSV}")
    
    datos_ibex = pd.read_csv(ARCHIVO_CSV, decimal=",", encoding="utf-8-sig")

    datos_ibex.columns = datos_ibex.columns.str.strip()

    print(f"Analisis IBEX 35")
    print(f"Numero de empresa: {datos_ibex.shape[0]}")#El 0 es el numero de filas
    print(f"Numero de columnas: {datos_ibex.shape[1]}")#El 1 es el numero de columnas

    




if __name__ == "__main__":
    main()

