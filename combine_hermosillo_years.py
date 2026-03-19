import geopandas as gpd
import pandas as pd
import os
import glob

input_dir = "data/hermosillo_shp_2020_2024"
output_dir = "data/hermosillo_maestro_2020_2024"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Buscar todos los archivos .shp en el directorio
shp_files = glob.glob(os.path.join(input_dir, "*.shp"))
print(f"Encontrados {len(shp_files)} archivos para procesar.")

all_gdfs = []

for shp_path in sorted(shp_files):
    print(f"Procesando: {os.path.basename(shp_path)}...")
    gdf = gpd.read_file(shp_path)
    
    # Normalizar nombres de columnas a mayúsculas para evitar duplicados por case-sensitivity
    gdf.columns = [col.upper() for col in gdf.columns]
    
    # Filtrar por Hermosillo, Sonora (EDO 26, MPIO 30)
    # Algunas versiones de ATUS pueden usar nombres de columnas ligeramente distintos,
    # pero EDO y MPIO son estándar.
    hmo_gdf = gdf[(gdf['EDO'] == 26) & (gdf['MPIO'] == 30)]
    
    print(f"  - Registros encontrados: {len(hmo_gdf)}")
    all_gdfs.append(hmo_gdf)

# Combinar todos los GeoDataFrames
print("\nCombinando todos los registros...")
combined_gdf = pd.concat(all_gdfs, ignore_index=True)

# Asegurarse de que el GeoDataFrame resultante sea válido
combined_gdf = gpd.GeoDataFrame(combined_gdf, geometry='GEOMETRY', crs=all_gdfs[0].crs)

# Exportar a un solo Shapefile
output_path = os.path.join(output_dir, "hermosillo_maestro_2020_2024.shp")
combined_gdf.to_file(output_path, driver='ESRI Shapefile', encoding='utf-8')

print(f"\nExtracción y combinación completada.")
print(f"Total de registros combinados (2020-2024): {len(combined_gdf)}")
print(f"Archivo guardado en: {output_path}")
