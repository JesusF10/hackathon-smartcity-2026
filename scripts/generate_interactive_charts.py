import pandas as pd
import altair as alt
import geopandas as gpd
import os

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"
os.makedirs(output_dir, exist_ok=True)

# Cargar datos
print("Cargando datos históricos...")
gdf = gpd.read_file(input_path)
df = pd.DataFrame(gdf.drop(columns='geometry'))

# Estética Darkmatter personalizada
dark_theme = {
    'config': {
        'view': {'stroke': 'transparent'},
        'axis': {
            'domainColor': '#404040',
            'gridColor': '#1a1a1a',
            'labelColor': '#a3a3a3',
            'titleColor': '#ffffff',
            'labelFont': 'JetBrains Mono',
            'titleFont': 'JetBrains Mono'
        },
        'legend': {
            'labelColor': '#a3a3a3',
            'titleColor': '#ffffff',
            'labelFont': 'JetBrains Mono',
            'titleFont': 'JetBrains Mono'
        },
        'title': {
            'color': '#ffffff',
            'font': 'JetBrains Mono'
        }
    }
}

alt.themes.register('darkmatter', lambda: dark_theme)
alt.themes.enable('darkmatter')

# 1. Gráfica de Cronología (Evolución de Fallecidos)
# Agrupar por Mes y Año
df_chrono = df[df['TOTMUERTOS'] > 0].groupby(['ANIO', 'MES'])['TOTMUERTOS'].sum().reset_index()
# Crear una fecha ficticia para el eje X
df_chrono['FECHA'] = pd.to_datetime(df_chrono['ANIO'].astype(str) + '-' + df_chrono['MES'].astype(str) + '-01')

line_chart = alt.Chart(df_chrono).mark_line(
    color='#b91c1c', # Rojo Darkmatter
    point=True,
    interpolate='monotone'
).encode(
    x=alt.X('FECHA:T', title='Timeline'),
    y=alt.Y('TOTMUERTOS:Q', title='Fatalities'),
    tooltip=['ANIO', 'MES', 'TOTMUERTOS']
).properties(
    width=600,
    height=300,
    title='Fatalities Evolution (2020-2024)'
).interactive()

# 2. Gráfica de Barras (Tipo de Accidente)
# Mapear códigos a nombres (estimados basados en el reporte previo)
tipaccid_map = {
    1: 'Vehicle Collision',
    2: 'Pedestrian Hit',
    4: 'Fixed Object',
    5: 'Overturn',
    10: 'Motorcycle',
    11: 'Cyclist'
}
df['TIPO_NAME'] = df['TIPACCID'].map(tipaccid_map).fillna('Other')

bar_chart = alt.Chart(df).mark_bar(color='#404040').encode(
    y=alt.Y('TIPO_NAME:N', sort='-x', title='Accident Type'),
    x=alt.X('count():Q', title='Total Incidents'),
    color=alt.condition(
        alt.datum.TIPO_NAME == 'Motorcycle',
        alt.value('#b91c1c'), # Destacar motos en rojo
        alt.value('#404040')
    ),
    tooltip=['TIPO_NAME', 'count()']
).properties(
    width=600,
    height=300,
    title='Incident Distribution by Type'
).interactive()

# Guardar como JSON (Vega-Lite)
print(f"Exportando gráficas JSON a: {output_dir}")
line_chart.save(os.path.join(output_dir, "chrono_fatalities.json"))
bar_chart.save(os.path.join(output_dir, "type_distribution.json"))

print("\nGeneración de gráficas interactivas exitosa.")
