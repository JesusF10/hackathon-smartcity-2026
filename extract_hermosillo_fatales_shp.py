import geopandas as gpd
import os

input_path = "data/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "data/hermosillo_fatales_2020_2024"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Cargando archivo maestro: {input_path}...")
gdf = gpd.read_file(input_path)

# Filtrar por accidentes con al menos una muerte
# La columna normalizada en el paso anterior es 'TOTMUERTOS'
# También se puede usar CLASE == 1
hmo_fatales = gdf[gdf['TOTMUERTOS'] > 0]

output_path = os.path.join(output_dir, "hermosillo_fatales_2020_2024.shp")
print(f"Filtrado completado. Registros fatales encontrados: {len(hmo_fatales)}")

# Guardar como Shapefile
hmo_fatales.to_file(output_path, driver='ESRI Shapefile', encoding='utf-8')

print(f"\nÉxito. Archivo de accidentes fatales generado en: {output_path}")
print(f"Total de víctimas mortales en el periodo (2020-2024): {hmo_fatales['TOTMUERTOS'].sum()}")
