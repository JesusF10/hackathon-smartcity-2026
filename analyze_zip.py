import geopandas as gpd
import zipfile
import os

zip_path = "data/atus_2024_shp.zip"
# Geopandas can read directly from zip using zip:// protocol
try:
    # Identify the .shp file path inside the zip
    with zipfile.ZipFile(zip_path, 'r') as z:
        shp_files = [f for f in z.namelist() if f.endswith('.shp')]
        if not shp_files:
            print("No .shp file found in ZIP")
            exit(1)
        shp_file = shp_files[0]
        print(f"Reading: {shp_file}")

    # Construct the URI for geopandas
    uri = f"zip://{zip_path}!{shp_file}"
    gdf = gpd.read_file(uri)

    print("\n--- Tipos de Variables ---")
    print(gdf.dtypes)
    
    print("\n--- Información General ---")
    print(gdf.info())

    print("\n--- Primeras filas ---")
    print(gdf.head())

except Exception as e:
    print(f"Error: {e}")
