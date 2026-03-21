import os
import pandas as pd
import geopandas as gpd
import json

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"
os.makedirs(output_dir, exist_ok=True)

# Mapeos oficiales INEGI
tipaccid_map = {
    1: "Colisión con vehículo",
    2: "Atropellamiento",
    3: "Colisión con animal",
    4: "Colisión con objeto fijo",
    5: "Volcadura",
    6: "Caída de pasajero",
    7: "Salida del camino",
    9: "Incendio",
    10: "Colisión con motocicleta",
    11: "Colisión con ciclista",
    12: "Otros"
}

clase_map = {
    1: "Fatal",
    2: "No fatal (Heridos)",
    3: "Sólo daños materiales"
}

print("Procesando Tipología de Colisiones 2024...")
try:
    gdf = gpd.read_file(input_path)
    # Filtrar solo por el año 2024
    df = pd.DataFrame(gdf[gdf["ANIO"] == 2024].drop(columns="geometry"))

    if df.empty:
        print("ADVERTENCIA: No se encontraron datos para el año 2024.")
    else:
        # Aplicar mapeos y limpiar
        df["TIPO_NAME"] = df["TIPACCID"].map(tipaccid_map).fillna("Otros")
        df["GRAVEDAD"] = df["CLASE"].map(clase_map).fillna("Desconocido")

        # Agregación Previa: Cruce de Tipo vs Gravedad
        df_typology = df.groupby(["TIPO_NAME", "GRAVEDAD"]).size().reset_index(name="TOTAL")

        # Validación No NaN
        df_typology = df_typology.fillna(0)

        # Exportar JSON optimizado (<100KB)
        output_file = os.path.join(output_dir, "collision_typology_2024.json")
        df_typology.to_json(output_file, orient="records", force_ascii=False)

        print(f"Análisis completado. Archivo generado: {output_file}")
        print(f"Total de registros 2024: {len(df)}")
        print(f"Tamaño: {os.path.getsize(output_file)/1024:.2f} KB")

except Exception as e:
    print(f"Error durante el procesamiento: {e}")
