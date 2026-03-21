import os
import pandas as pd
import geopandas as gpd
import json

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"

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

print("Analizando Radiografía de Riesgo por Vialidad...")

try:
    gdf = gpd.read_file(input_path)
    df = pd.DataFrame(gdf.drop(columns="geometry"))
    df['CALLE1'] = df['CALLE1'].astype(str).str.strip().str.upper()
    df['TIPO_NAME'] = df['TIPACCID'].map(tipaccid_map).fillna("Otros")

    # Identificar las Top 5 vialidades (por IGV)
    top_vialidades = df.groupby('CALLE1')['TOTMUERTOS'].sum().sort_values(ascending=False).head(5).index.tolist()
    # Si por muertos no es suficiente, usamos el IGV calculado antes
    df['IGV'] = (df['TOTMUERTOS'] * 10) + (df['TOTHERIDOS'] * 3) + 1
    top_5_igv = df.groupby('CALLE1')['IGV'].sum().sort_values(ascending=False).head(5).index.tolist()

    resumen_causas = []

    for calle in top_5_igv:
        subset = df[df['CALLE1'] == calle]
        causas = subset.groupby('TIPO_NAME').agg({
            'ID': 'count',
            'TOTMUERTOS': 'sum',
            'TOTHERIDOS': 'sum'
        }).rename(columns={'ID': 'TOTAL'}).reset_index()
        
        causas['PORCENTAJE'] = (causas['TOTAL'] / causas['TOTAL'].sum() * 100).round(1)
        causas = causas.sort_values(by='TOTAL', ascending=False)

        resumen_causas.append({
            "vialidad": calle,
            "total_accidentes": int(subset.shape[0]),
            "muertes_totales": int(subset['TOTMUERTOS'].sum()),
            "heridos_totales": int(subset['TOTHERIDOS'].sum()),
            "causas_principales": causas.to_dict(orient="records")
        })

    output_file = os.path.join(output_dir, "radiografia_vialidades.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(resumen_causas, f, ensure_ascii=False, indent=2)

    print(f"✅ Radiografía generada en: {output_file}")

except Exception as e:
    print(f"❌ Error: {e}")
