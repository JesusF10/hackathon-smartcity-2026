import geopandas as gpd
import pandas as pd
import os

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"
os.makedirs(output_dir, exist_ok=True)

# Mapeos
def get_franja(h):
    if 6 <= h < 12: return 'Mañana'
    if 12 <= h < 18: return 'Tarde'
    if 18 <= h < 24: return 'Noche'
    return 'Madrugada'

clase_map = {1: "Fatal", 2: "Heridos", 3: "Sólo Daños"}

print("Generando Mapa Multinivel Completo (3 Clases) - 2024...")

try:
    # 1. Cargar y transformar
    gdf = gpd.read_file(input_path)
    gdf = gdf.to_crs(epsg=4326)
    gdf_2024 = gdf[gdf['ANIO'] == 2024].copy()

    # --- NIVEL 1: HEATMAP (Agregado por Rejilla para <100KB) ---
    # Agrupamos por coordenadas redondeadas para representar densidad de los 11k+ accidentes
    gdf_2024['lat_grid'] = gdf_2024.geometry.y.round(3)
    gdf_2024['lng_grid'] = gdf_2024.geometry.x.round(3)
    
    heatmap_agg = gdf_2024.groupby(['lat_grid', 'lng_grid']).size().reset_index(name='count')
    heatmap_path = os.path.join(output_dir, "heatmap_all_2024.json")
    heatmap_agg.to_json(heatmap_path, orient="records")

    # --- NIVEL 3: PUNTOS DE INTERVENCIÓN (Solo Fatal y Heridos para precisión) ---
    # Incluimos CLASE 1 y 2. La CLASE 3 se visualiza vía Heatmap para evitar lag.
    df_severe = gdf_2024[gdf_2024['CLASE'].isin([1, 2])].copy()
    df_severe['lat'] = df_severe.geometry.y
    df_severe['lng'] = df_severe.geometry.x
    df_severe['clase_name'] = df_severe['CLASE'].map(clase_map)
    df_severe['franja'] = df_severe['HORA'].apply(get_franja)
    
    cols_severe = ['lat', 'lng', 'clase_name', 'franja', 'TOTMUERTOS', 'TOTHERIDOS', 'CALLE1']
    points_path = os.path.join(output_dir, "intervention_points_2024.json")
    df_severe[cols_severe].fillna(0).to_json(points_path, orient="records", force_ascii=False)

    # --- NIVEL 2: CORREDORES (Ya pondera las 3 clases) ---
    gdf_2024['irs'] = (gdf_2024['TOTMUERTOS'] * 10) + (gdf_2024['TOTHERIDOS'] * 3) + 1
    corredores = gdf_2024.groupby('CALLE1').agg({
        'irs': 'sum',
        'TOTMUERTOS': 'sum',
        'TOTHERIDOS': 'sum',
        'ID': 'count' # Total de accidentes de cualquier clase
    }).rename(columns={'ID': 'total_accidentes'}).reset_index()
    
    corredores = corredores.sort_values(by='irs', ascending=False).head(100)
    corredores_path = os.path.join(output_dir, "risk_corridors_2024.json")
    corredores.to_json(corredores_path, orient="records", force_ascii=False)

    print("\nArchivos multinivel (3 clases) generados:")
    print(f"- Heatmap (Todas): {heatmap_path} ({os.path.getsize(heatmap_path)/1024:.2f} KB)")
    print(f"- Puntos (Graves): {points_path} ({os.path.getsize(points_path)/1024:.2f} KB)")
    print(f"- Corredores: {corredores_path} ({os.path.getsize(corredores_path)/1024:.2f} KB)")

except Exception as e:
    print(f"Error: {e}")
