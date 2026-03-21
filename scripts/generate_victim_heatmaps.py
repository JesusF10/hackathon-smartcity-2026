import os
import pandas as pd
import geopandas as gpd
import json

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"

def get_grid_data(df_subset):
    if df_subset.empty: return []
    # Agrupar por rejilla de 3 decimales (~110m)
    grid = df_subset.groupby(['lat_grid', 'lng_grid']).size().reset_index(name='i')
    return grid.rename(columns={'lat_grid': 'lat', 'lng_grid': 'lng'}).to_dict(orient="records")

try:
    print("Actualizando Mapas de Calor con categoría 'Vehículos'...")
    gdf = gpd.read_file(input_path)
    gdf = gdf.to_crs(epsg=4326)
    df = pd.DataFrame(gdf)
    
    df['lat_grid'] = gdf.geometry.y.round(3)
    df['lng_grid'] = gdf.geometry.x.round(3)

    # 1. Peatones: Atropellamientos o víctimas peatones
    peatones = df[(df['TIPACCID'] == 2) | (df['PEATMUERTO'] > 0) | (df['PEATHERIDO'] > 0)]
    
    # 2. Motociclistas: Colisión con moto o involucrados
    motos = df[(df['TIPACCID'] == 10) | (df['MOTOCICLET'] > 0)]
    
    # 3. Ciclistas: Colisión con ciclista o involucrados
    ciclistas = df[(df['TIPACCID'] == 11) | (df['BICICLETA'] > 0)]
    
    # 4. Vehículos (Autos/Camionetas): 
    # Colisión entre vehículos (1), Objeto fijo (4), Volcadura (5), Salida de camino (7)
    # Enfocándonos en accidentes donde hay heridos o muertos para que el mapa sea de 'riesgo'
    vehiculos = df[
        (df['TIPACCID'].isin([1, 4, 5, 7])) & 
        ((df['CONDMUERTO'] > 0) | (df['CONDHERIDO'] > 0) | (df['PASAMUERTO'] > 0) | (df['PASAHERIDO'] > 0))
    ]

    victim_heatmaps = {
        "peatones": get_grid_data(peatones),
        "motos": get_grid_data(motos),
        "ciclistas": get_grid_data(ciclistas),
        "vehiculos": get_grid_data(vehiculos),
        "metadata": {
            "periodo": "2020-2024",
            "resolucion": "~110m"
        }
    }

    output_file = os.path.join(output_dir, "victim_heatmaps.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(victim_heatmaps, f, ensure_ascii=False)

    print(f"✅ Mapas de calor actualizados. Categoría 'Vehículos': {len(vehiculos)} incidentes graves.")

except Exception as e:
    print(f"❌ Error: {e}")
