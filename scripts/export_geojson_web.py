import geopandas as gpd
import os

# Rutas de entrada y salida
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
# Ruta para el proyecto web
output_path = "/home/jesus/Projects/portfolio-blog/public/data/processed/hermosillo_vial.json"

# Asegurar que el directorio existe
os.makedirs(os.path.dirname(output_path), exist_ok=True)

print(f"Leyendo archivo maestro: {input_path}")
try:
    # Cargar el Shapefile
    gdf = gpd.read_file(input_path)

    # 1. Convertir a WGS84 (EPSG:4326) - Indispensable para MapLibre/Web
    print("Transformando coordenadas a WGS84 (EPSG:4326)...")
    gdf = gdf.to_crs(epsg=4326)

    # 2. Limpieza y Optimización
    # --- VALIDACIÓN DE ESTÁNDAR JSON (No NaN) ---
    # Convertir NaN a 0 o null para evitar errores en el parseo JSON de la web
    gdf = gdf.fillna(0)

    # Mantener solo columnas esenciales para reducir peso (>30MB es crítico)
    cols_to_keep = ['CALLE1', 'TOTMUERTOS', 'CLASE', 'ANIO', 'MES', 'HORA', 'TIPACCID', 'geometry']
    gdf_optimized = gdf[cols_to_keep]

    # 3. Exportar a GeoJSON (UTF-8 por defecto en GeoPandas)
    print(f"Exportando a GeoJSON en: {output_path}")
    gdf_optimized.to_file(output_path, driver='GeoJSON')

    print("\nGeneración exitosa.")
    print(f"Total de incidentes exportados: {len(gdf_optimized)}")
    file_size_mb = os.path.getsize(output_path) / (1024*1024)
    print(f"Tamaño final: {file_size_mb:.2f} MB")
    
    if file_size_mb > 30:
        print("ADVERTENCIA: El archivo supera los 30MB, considera simplificar la geometría o eliminar más columnas.")

except Exception as e:
    print(f"Error durante la generación del GeoJSON: {e}")
