import geopandas as gpd
import pandas as pd

# Load the combined dataset
path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
gdf = gpd.read_file(path)

# Extract column info
cols = gdf.columns
dtypes = gdf.dtypes

# Categories and Descriptions based on INEGI ATUS Metadata
categories = {
    "Identificación y Ubicación": {
        "ID": "Identificador único del accidente.",
        "EDO": "Código del Estado (Sonora = 26).",
        "MPIO": "Código del Municipio (Hermosillo = 30).",
        "URBANA": "Indicador de accidente en zona urbana.",
        "SUBURBANA": "Indicador de accidente en zona suburbana.",
        "CALLE1": "Vialidad principal del accidente.",
        "CALLE2": "Vialidad secundaria o intersección.",
        "CARRETERA": "Nombre de la carretera si aplica.",
        "LONGITUD": "Coordenada geográfica X.",
        "LATITUD": "Coordenada geográfica Y.",
        "GEOMETRY": "Objeto espacial para mapeo."
    },
    "Cronología": {
        "ANIO": "Año de ocurrencia (2020-2024).",
        "MES": "Mes (1-12).",
        "DIA": "Día del mes.",
        "DIASEMANA": "Día de la semana (1:Domingo a 7:Sábado o similar).",
        "HORA": "Hora del día (0-23).",
        "MINUTOS": "Minuto de la hora."
    },
    "Tipología y Causa": {
        "TIPACCID": "Tipo de siniestro (Choque, volcadura, atropello, etc.).",
        "CLASE": "Severidad (1:Fatal, 2:No Fatal, 3:Solo daños).",
        "CAUSAACCI": "Causa probable (Conductor, Peatón, Falla mecánica, etc.).",
        "CAPAROD": "Tipo de superficie de rodamiento."
    },
    "Vehículos Involucrados": {
        "AUTOMOVIL": "Cantidad de automóviles.",
        "CAMPASAJ": "Cantidad de camionetas de pasajeros.",
        "MICROBUS": "Cantidad de microbuses.",
        "PASCAMION": "Cantidad de camiones de pasajeros.",
        "OMNIBUS": "Cantidad de ómnibus.",
        "TRANVIA": "Cantidad de tranvías o trenes ligeros.",
        "CAMIONETA": "Cantidad de camionetas de carga.",
        "CAMION": "Cantidad de camiones de carga.",
        "TRACTOR": "Cantidad de tractores.",
        "FERROCARRI": "Cantidad de locomotoras.",
        "MOTOCICLET": "Cantidad de motocicletas.",
        "BICICLETA": "Cantidad de bicicletas.",
        "OTROVEHIC": "Otros tipos de vehículos."
    },
    "Víctimas y Seguridad": {
        "SEXO": "Sexo del conductor responsable.",
        "ALIENTO": "Presencia de aliento alcohólico.",
        "CINTURON": "Uso del cinturón de seguridad.",
        "EDAD": "Edad del conductor.",
        "CONDMUERTO": "Conductores fallecidos.",
        "CONDHERIDO": "Conductores heridos.",
        "PASAMUERTO": "Pasajeros fallecidos.",
        "PASAHERIDO": "Pasajeros heridos.",
        "PEATMUERTO": "Peatones fallecidos.",
        "PEATHERIDO": "Peatones heridos.",
        "CICLMUERTO": "Ciclistas fallecidos.",
        "CICLHERIDO": "Ciclistas heridos.",
        "OTROMUERTO": "Otras personas fallecidas.",
        "OTROHERIDO": "Otras personas heridas.",
        "TOTMUERTOS": "Total general de fallecidos.",
        "TOTHERIDOS": "Total general de heridos."
    }
}

# Generate Typst Content
typst_output = """#set page(paper: "a4", margin: (x: 2cm, y: 2cm))
#set text(font: "Liberation Sans", size: 10pt)

#align(center)[
  #text(size: 20pt, weight: "bold")[Diccionario de Variables H-Vial / H-Vital]
  #v(0.5em)
  #text(size: 14pt, fill: gray)[Dataset Histórico Hermosillo (2020-2024)]
]

#v(1em)
= Introducción
Este documento describe exhaustivamente las variables contenidas en el dataset consolidado de accidentes de tránsito en Hermosillo. La información proviene del INEGI (ATUS) y ha sido procesada para facilitar la identificación de puntos críticos para la campaña de seguridad vial.

"""

for cat, vars_dict in categories.items():
    typst_output += f"\n== {cat}\n"
    typst_output += "#table(\n  columns: (1.5fr, 1fr, 3fr, 2fr),\n  fill: (x, y) => if y == 0 { gray.lighten(60%) },\n  [*Variable*], [*Tipo*], [*Descripción*], [*Utilidad*],\n"
    for var, desc in vars_dict.items():
        if var in dtypes:
            dtype = str(dtypes[var])
            # Assigning utility based on category
            utility = "Filtrado espacial" if cat == "Identificación y Ubicación" else \
                      "Análisis de tendencias" if cat == "Cronología" else \
                      "Identificación de patrones" if cat == "Tipología y Causa" else \
                      "Perfil de riesgo" if cat == "Vehículos Involucrados" else \
                      "Medición de impacto social"
            typst_output += f"  [`{var}`], [{dtype}], [{desc}], [{utility}],\n"
    typst_output += ")\n"

with open("docs/diccionario_datos.typ", "w", encoding="utf-8") as f:
    f.write(typst_output)

print("Typst dictionary file generated in docs/diccionario_datos.typ")
