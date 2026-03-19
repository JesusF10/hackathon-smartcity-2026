import geopandas as gpd
import os

# Rutas de entrada y salida
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_path = "data/processed/hermosillo_vial.json"

print(f"Leyendo archivo maestro: {input_path}")
try:
    # Cargar el Shapefile
    gdf = gpd.read_file(input_path)

    # 1. Convertir a WGS84 (EPSG:4326) - Indispensable para MapLibre/Web
    print("Transformando coordenadas a WGS84 (EPSG:4326)...")
    gdf = gdf.to_crs(epsg=4326)

    # 2. Limpieza ligera de datos para optimizar el peso del JSON (opcional pero recomendado)
    # Mantendremos solo las variables que el agente de la web solicitó y algunas extras útiles
    cols_to_keep = ['CALLE1', 'TOTMUERTOS', 'CLASE', 'ANIO', 'MES', 'HORA', 'TIPACCID', 'geometry']
    gdf_optimized = gdf[cols_to_keep]

    # 3. Exportar a GeoJSON
    print(f"Exportando a GeoJSON en: {output_path}")
    gdf_optimized.to_file(output_path, driver='GeoJSON')

    print("\nGeneración exitosa.")
    print(f"Total de incidentes exportados: {len(gdf_optimized)}")
    print(f"Tamaño estimado: {os.path.getsize(output_path) / (1024*1024):.2f} MB")

except Exception as e:
    print(f"Error durante la generación del GeoJSON: {e}")
