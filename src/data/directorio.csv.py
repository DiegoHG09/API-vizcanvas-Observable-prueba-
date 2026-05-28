import pandas as pd
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')  # ← agregar esta línea
xlsx_path = os.path.join(os.path.dirname(__file__), "Directorio_fuentes_datos.xlsx")

sheets = {
    "Demografía_y_sociedad": "Demografía y Sociedad",
    "Economía_y_Sectores_Productivos": "Economía y Sectores Productivos",
    "Geografía_y_medio_ambiente": "Geografía y Medio Ambiente",
    "Gobierno_Seguridad_y_Justicia": "Gobierno, Seguridad y Justicia"
}

dfs = []
for sheet_name, categoria in sheets.items():
    df = pd.read_excel(xlsx_path, sheet_name=sheet_name)
    df = df[~df["Nombre_de_la_fuente"].str.startswith("*", na=False)]
    df["categoria"] = categoria
    dfs.append(df)

directorio = pd.concat(dfs, ignore_index=True) 

directorio = directorio.dropna(subset=["Nombre_de_la_fuente"])
directorio = directorio[directorio["Nombre_de_la_fuente"].str.strip() != ""]

directorio["Año_referencia"] = pd.to_numeric(
    directorio["Año_referencia"], errors="coerce"
).astype("Int64")

directorio = directorio.rename(columns={"Insitutucion": "Institucion"})

directorio.to_csv(sys.stdout, index=False)