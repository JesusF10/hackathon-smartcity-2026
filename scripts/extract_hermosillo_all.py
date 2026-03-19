import geopandas as gpd

zip_path = "data/atus_2024_shp.zip"
shp_inside = "conjunto_de_datos/BASE_MUNICIPAL_ACCIDENTES_GEORREFERENCIADOS_2024.shp"
uri = f"zip://{zip_path}!{shp_inside}"

print("Leyendo dataset completo y filtrando por Hermosillo...")
# Leer el shapefile
gdf = gpd.read_file(uri)

# Filtrar por Hermosillo, Sonora (EDO 26, MPIO 30)
hmo_todos = gdf[(gdf['EDO'] == 26) & (gdf['MPIO'] == 30)]

output_file = "hermosillo_accidentes_todos_2024.csv"
hmo_todos.to_csv(output_file, index=False, encoding='utf-8')

print(f"Extracción completada.")
print(f"Total de accidentes encontrados en Hermosillo: {len(hmo_todos)}")
print(f"Archivo guardado como: {output_file}")
