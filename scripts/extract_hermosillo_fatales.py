import geopandas as gpd

zip_path = "data/atus_2024_shp.zip"
shp_inside = "conjunto_de_datos/BASE_MUNICIPAL_ACCIDENTES_GEORREFERENCIADOS_2024.shp"
uri = f"zip://{zip_path}!{shp_inside}"

print("Reading and filtering data...")
# Read the shapefile
gdf = gpd.read_file(uri)

# Filter for Hermosillo, Sonora (EDO 26, MPIO 30) and at least one death (TOTMUERTOS > 0)
# Note: CLASE == 1 also indicates fatal accidents
hmo_fatales = gdf[(gdf['EDO'] == 26) & (gdf['MPIO'] == 30) & (gdf['TOTMUERTOS'] > 0)]

output_file = "hermosillo_accidentes_fatales_2024.csv"
hmo_fatales.to_csv(output_file, index=False, encoding='utf-8')

print(f"Extraction complete.")
print(f"Total fatal accidents found in Hermosillo: {len(hmo_fatales)}")
print(f"Total deaths in these accidents: {hmo_fatales['TOTMUERTOS'].sum()}")
print(f"File saved as: {output_file}")
