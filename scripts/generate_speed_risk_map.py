import os
import pandas as pd
import geopandas as gpd
import json

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"

try:
    print("Generando Mapa de Velocidad Mortal...")
    gdf = gpd.read_file(input_path)
    gdf = gdf.to_crs(epsg=4326)
    df = pd.DataFrame(gdf)
    
    # Coordenadas base
    df['lat'] = gdf.geometry.y
    df['lng'] = gdf.geometry.x
    df['CALLE1'] = df['CALLE1'].astype(str).str.strip().str.upper()

    # Filtro de Velocidad: Volcaduras (5), Salidas de Camino (7) 
    # y Choques con Objeto Fijo (4) solo si hubo víctimas (indicador de impacto fuerte)
    tipos_velocidad = [5, 7]
    speed_accidents = df[
        (df['TIPACCID'].isin(tipos_velocidad)) | 
        ((df['TIPACCID'] == 4) & (df['CLASE'].isin([1, 2])))
    ].copy()

    # Cálculo de Riesgo de Velocidad (Ponderado por Fatalidad)
    speed_accidents['speed_score'] = (speed_accidents['TOTMUERTOS'] * 15) + (speed_accidents['TOTHERIDOS'] * 5) + 2

    # Agrupar por Corredores para identificar los tramos rectos más peligrosos
    corredores_velocidad = speed_accidents.groupby('CALLE1').agg({
        'speed_score': 'sum',
        'ID': 'count',
        'TOTMUERTOS': 'sum',
        'TOTHERIDOS': 'sum'
    }).rename(columns={'ID': 'total_incidentes_velocidad'}).reset_index()

    # Filtrar solo los corredores con riesgo real (Top 30)
    top_corredores = corredores_velocidad.sort_values(by='speed_score', ascending=False).head(30)

    # Preparar puntos individuales para el mapa (solo los más graves para no saturar)
    puntos_velocidad = speed_accidents[speed_accidents['speed_score'] > 5][['lat', 'lng', 'speed_score', 'CALLE1', 'TOTMUERTOS']].to_dict(orient="records")

    speed_map_data = {
        "corredores": top_corredores.to_dict(orient="records"),
        "puntos_criticos": puntos_velocidad,
        "metadata": {
            "periodo": "2020-2024",
            "tipos_analizados": ["Volcadura", "Salida de Camino", "Choque con Objeto Fijo Grave"],
            "mensaje": "Zonas donde la velocidad domina la severidad del impacto."
        }
    }

    output_file = os.path.join(output_dir, "speed_mortality_map.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(speed_map_data, f, ensure_ascii=False)

    print(f"✅ Mapa de Velocidad Mortal generado en: {output_file}")
    print(f"   - Puntos identificados: {len(puntos_velocidad)}")
    print(f"   - Corredor más veloz/mortal: {top_corredores.iloc[0]['CALLE1']}")

except Exception as e:
    print(f"❌ Error: {e}")
