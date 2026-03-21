import os
import json
import altair as alt
import geopandas as gpd
import pandas as pd

# Rutas
input_path = (
    "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
)
# Ruta destino en el proyecto de la web para producción
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"
os.makedirs(output_dir, exist_ok=True)

# Cargar datos
print("Cargando datos históricos...")
gdf = gpd.read_file(input_path)
df = pd.DataFrame(gdf.drop(columns="geometry"))

# --- 1. VALIDACIÓN DE ESTÁNDAR JSON (No NaN) ---
# Acción: Convertir NaN, Infinity o -Infinity a 0 para mantener compatibilidad
df = df.fillna(0).replace([float('inf'), float('-inf')], 0)

# Estética Darkmatter personalizada
dark_theme = {
    "config": {
        "view": {"stroke": "transparent"},
        "axis": {
            "domainColor": "#404040",
            "gridColor": "#1a1a1a",
            "labelColor": "#a3a3a3",
            "titleColor": "#ffffff",
            "labelFont": "JetBrains Mono",
            "titleFont": "JetBrains Mono",
        },
        "legend": {
            "labelColor": "#a3a3a3",
            "titleColor": "#ffffff",
            "labelFont": "JetBrains Mono",
            "titleFont": "JetBrains Mono",
        },
        "title": {"color": "#ffffff", "font": "JetBrains Mono"},
    }
}

alt.themes.register("darkmatter", lambda: dark_theme)
alt.themes.enable("darkmatter")

# --- 2. AGREGACIÓN PREVIA (Optimización de Peso) ---

# 1. Gráfica de Cronología (Evolución de Fallecidos)
# Agrupar por Mes y Año para no enviar todo el dataset
df_chrono = (
    df[df["TOTMUERTOS"] > 0].groupby(["ANIO", "MES"])["TOTMUERTOS"].sum().reset_index()
)
# Crear una fecha ficticia para el eje X
df_chrono["FECHA"] = pd.to_datetime(
    df_chrono["ANIO"].astype(str) + "-" + df_chrono["MES"].astype(str) + "-01"
).dt.strftime('%Y-%m-%d') # Convertir a string para evitar problemas con JSON

line_chart = (
    alt.Chart(df_chrono)
    .mark_line(
        color="#b91c1c",  # Rojo Darkmatter
        point=True,
        interpolate="monotone",
    )
    .encode(
        x=alt.X("FECHA:T", title="Fecha"),
        y=alt.Y("TOTMUERTOS:Q", title="Fatalidades"),
        tooltip=["ANIO", "MES", "TOTMUERTOS"],
    )
    .properties(width=600, height=300, title="Cronología de Fatalidades (2020-2024)")
    .interactive()
)

# 2. Gráfica de Barras (Tipo de Accidente)
# --- 3. CONSISTENCIA DE IDIOMA Y ETIQUETAS ---
tipaccid_map = {
    1: "Colisión de Vehículos",
    2: "Choque con Peatón",
    4: "Choque con Objetos Fijos",
    5: "Volcamiento",
    10: "Motocicleta",
    11: "Ciclista",
}
df["TIPO_NAME"] = df["TIPACCID"].map(tipaccid_map).fillna("Otros")

# AGREGACIÓN PREVIA: Contar incidentes antes de crear la gráfica
df_bar = df.groupby("TIPO_NAME").size().reset_index(name="TOTAL_ACCIDENTES")

bar_chart = (
    alt.Chart(df_bar)
    .mark_bar(color="#404040")
    .encode(
        y=alt.Y("TIPO_NAME:N", sort="-x", title="Tipo de Accidente"),
        x=alt.X("TOTAL_ACCIDENTES:Q", title="Accidentes Totales"),
        color=alt.condition(
            alt.datum.TIPO_NAME == "Motocicleta", # Corregido: Coincide con tipaccid_map
            alt.value("#b91c1c"),  # Destacar motos en rojo
            alt.value("#404040"),
        ),
        tooltip=["TIPO_NAME", "TOTAL_ACCIDENTES"],
    )
    .properties(width=600, height=300, title="Accidentes Totales por Tipo")
    .interactive()
)

# --- 4. CODIFICACIÓN DE CARACTERES (UTF-8 sin BOM) ---
print(f"Exportando gráficas JSON a: {output_dir}")

# Guardar asegurando UTF-8
line_chart.save(os.path.join(output_dir, "chrono_fatalities.json"))
bar_chart.save(os.path.join(output_dir, "type_distribution.json"))

print("\nGeneración de gráficas interactivas exitosa.")
print(f"Tamaño de chrono_fatalities.json: {os.path.getsize(os.path.join(output_dir, 'chrono_fatalities.json'))/1024:.2f} KB")
print(f"Tamaño de type_distribution.json: {os.path.getsize(os.path.join(output_dir, 'type_distribution.json'))/1024:.2f} KB")
