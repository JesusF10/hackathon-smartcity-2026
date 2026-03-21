import os
import pandas as pd
import geopandas as gpd
import json

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"
os.makedirs(output_dir, exist_ok=True)

print("Generando Ranking de Intersecciones y Calles (2020-2024)...")

def clean_street(name):
    if not name or pd.isna(name):
        return "SIN NOMBRE"
    return str(name).strip().upper()

try:
    # 1. Cargar datos
    gdf = gpd.read_file(input_path)
    df = pd.DataFrame(gdf.drop(columns="geometry"))

    # 2. Limpieza y Normalización
    df['CALLE1'] = df['CALLE1'].apply(clean_street)
    df['CALLE2'] = df['CALLE2'].apply(clean_street)

    # Crear identificador único de intersección (sin importar el orden)
    def get_intersection(row):
        c1, c2 = row['CALLE1'], row['CALLE2']
        if c2 == "SIN NOMBRE" or c2 == "0" or not c2:
            return None # No es una intersección clara o es tramo recto
        streets = sorted([c1, c2])
        return f"{streets[0]} & {streets[1]}"

    df['INTERSECCION'] = df.apply(get_intersection, axis=1)

    # 3. Cálculo de Índice de Gravedad Vial (IGV)
    # Ponderación: Fatal=10, Herido=3, Solo daños=1
    df['IGV'] = (df['TOTMUERTOS'] * 10) + (df['TOTHERIDOS'] * 3) + 1

    # --- RANKING 1: INTERSECCIONES ---
    ranking_intersecciones = df[df['INTERSECCION'].notna()].groupby('INTERSECCION').agg({
        'IGV': 'sum',
        'TOTMUERTOS': 'sum',
        'TOTHERIDOS': 'sum',
        'ID': 'count'
    }).rename(columns={'ID': 'TOTAL_ACCIDENTES'}).reset_index()

    top_intersecciones = ranking_intersecciones.sort_values(by='IGV', ascending=False).head(20)

    # --- RANKING 2: CALLES (VIALIDADES) ---
    # Para calles, sumamos donde aparezca como CALLE1 o CALLE2
    # Pero para no duplicar el IGV de un solo accidente, usamos CALLE1 como referencia principal
    ranking_calles = df.groupby('CALLE1').agg({
        'IGV': 'sum',
        'TOTMUERTOS': 'sum',
        'TOTHERIDOS': 'sum',
        'ID': 'count'
    }).rename(columns={'ID': 'TOTAL_ACCIDENTES'}).reset_index()

    top_calles = ranking_calles.sort_values(by='IGV', ascending=False).head(20)

    # 4. Exportar resultados
    output_data = {
        "intersecciones": top_intersecciones.to_dict(orient="records"),
        "vialidades": top_calles.to_dict(orient="records"),
        "metadata": {
            "periodo": "2020-2024",
            "total_registros_analizados": len(df),
            "metodologia": "IGV = (Muertes*10) + (Heridos*3) + 1"
        }
    }

    output_file = os.path.join(output_dir, "ranking_vial_hermosillo.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Ranking generado exitosamente en: {output_file}")
    print(f"Top 1 Intersección: {top_intersecciones.iloc[0]['INTERSECCION']} (IGV: {top_intersecciones.iloc[0]['IGV']})")
    print(f"Top 1 Vialidad: {top_calles.iloc[0]['CALLE1']} (IGV: {top_calles.iloc[0]['IGV']})")

except Exception as e:
    print(f"❌ Error durante el procesamiento: {e}")
