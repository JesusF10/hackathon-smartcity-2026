import geopandas as gpd
import pandas as pd
import zipfile
import os

zip_files = [
    "data/atus_2020_shp.zip",
    "data/atus_2021_shp.zip",
    "data/atus_2022_shp.zip",
    "data/atus_2023_shp.zip",
    "data/atus_2024_shp.zip"
]

output_dir = "data/hermosillo_maestro_2020_2024"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

all_gdfs = []

for zip_path in zip_files:
    print(f"Procesando {zip_path}...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            shp_files = [f for f in z.namelist() if f.endswith('.shp') and 'conjunto_de_datos' in f]
            if not shp_files:
                shp_files = [f for f in z.namelist() if f.endswith('.shp')]
            
            if not shp_files:
                print(f"  - No se encontró archivo .shp en {zip_path}")
                continue
                
            shp_file = shp_files[0]
            print(f"  - Leyendo: {shp_file}")
            
            uri = f"zip://{zip_path}!{shp_file}"
            gdf = gpd.read_file(uri)
            
            # Guardar el CRS original
            original_crs = gdf.crs
            
            # Normalizar nombres de columnas
            gdf.columns = [col.upper() for col in gdf.columns]
            
            # Reasignar la columna de geometría activa (que ahora es 'GEOMETRY')
            gdf = gdf.set_geometry('GEOMETRY')
            gdf.crs = original_crs
            
            # Filtrar por Hermosillo (EDO 26, MPIO 30)
            hmo_gdf = gdf[(gdf['EDO'] == 26) & (gdf['MPIO'] == 30)]
            print(f"  - Registros Hermosillo: {len(hmo_gdf)}")
            
            all_gdfs.append(hmo_gdf)
            
    except Exception as e:
        print(f"  - Error procesando {zip_path}: {e}")

if all_gdfs:
    print("\nCombinando todos los años...")
    # Concatenar
    combined_df = pd.concat(all_gdfs, ignore_index=True)
    
    # Crear el GeoDataFrame final
    combined_gdf = gpd.GeoDataFrame(combined_df, geometry='GEOMETRY', crs=all_gdfs[0].crs)
    
    output_path = os.path.join(output_dir, "hermosillo_maestro_2020_2024.shp")
    combined_gdf.to_file(output_path, driver='ESRI Shapefile', encoding='utf-8')
    
    print(f"\nÉxito. Archivo maestro generado en: {output_path}")
    print(f"Total de registros (2020-2024): {len(combined_gdf)}")
else:
    print("\nNo se pudieron procesar datos.")
