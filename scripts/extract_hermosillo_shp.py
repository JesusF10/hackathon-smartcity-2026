import geopandas as gpd
import os

# Configuración de rutas
zip_path = "data/atus_2024_shp.zip"
shp_inside = "conjunto_de_datos/BASE_MUNICIPAL_ACCIDENTES_GEORREFERENCIADOS_2024.shp"
uri = f"zip://{zip_path}!{shp_inside}"
output_dir = "data/hermosillo_shapefile"

# Crear directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Cargando dataset original y filtrando para Hermosillo...")
try:
    # Leer directamente del ZIP usando fiona (backend de geopandas)
    gdf = gpd.read_file(uri)

    # Filtrar: Sonora (26), Hermosillo (30)
    hmo_gdf = gdf[(gdf['EDO'] == 26) & (gdf['MPIO'] == 30)]

    # Guardar como Shapefile
    # Nota: El driver 'ESRI Shapefile' generará .shp, .shx, .dbf y .prj
    output_path = os.path.join(output_dir, "hermosillo_atus_2024.shp")
    hmo_gdf.to_file(output_path, driver='ESRI Shapefile', encoding='utf-8')

    print(f"\nExtracción completada exitosamente.")
    print(f"Directorio de salida: {output_dir}")
    print(f"Registros geoespaciales exportados: {len(hmo_gdf)}")
    print("\nArchivos generados:")
    for f in os.listdir(output_dir):
        if f.startswith("hermosillo_atus_2024"):
            print(f"- {f}")

except Exception as e:
    print(f"Error durante la extracción: {e}")
