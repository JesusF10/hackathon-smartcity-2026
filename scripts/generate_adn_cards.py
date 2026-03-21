import os
import pandas as pd
import geopandas as gpd
import json

# Rutas
input_path = "data/processed/hermosillo_maestro_2020_2024/hermosillo_maestro_2020_2024.shp"
output_dir = "/home/jesus/Projects/portfolio-blog/public/data/processed/charts"

tipaccid_map = {
    1: "Vehículo vs Vehículo",
    2: "Atropellamiento",
    4: "Choque con Objeto Fijo",
    5: "Volcadura",
    10: "Motocicleta",
    11: "Ciclista"
}

def get_risk_label(igv, total):
    if igv > 3000: return "EXTREMO"
    if igv > 1500: return "MUY ALTO"
    return "ALTO"

def get_peak_hour(df_subset):
    if df_subset.empty: return "N/A"
    return int(df_subset['HORA'].mode().iloc[0])

try:
    gdf = gpd.read_file(input_path)
    df = pd.DataFrame(gdf.drop(columns="geometry"))
    df['CALLE1'] = df['CALLE1'].astype(str).str.strip().str.upper()
    df['IGV'] = (df['TOTMUERTOS'] * 10) + (df['TOTHERIDOS'] * 3) + 1

    top_5_igv = df.groupby('CALLE1')['IGV'].sum().sort_values(ascending=False).head(5).index.tolist()

    adn_cards = []

    for calle in top_5_igv:
        subset = df[df['CALLE1'] == calle]
        total_acc = len(subset)
        muertos = int(subset['TOTMUERTOS'].sum())
        heridos = int(subset['TOTHERIDOS'].sum())
        igv_total = float(subset['IGV'].sum())
        
        # Letalidad: Muertes por cada 100 accidentes
        letalidad = round((muertos / total_acc * 100), 2) if total_acc > 0 else 0
        
        # Tipo predominante (excluyendo genérico Vehículo vs Vehículo si es posible para dar más valor)
        tipos = subset.groupby('TIPACCID').size().sort_values(ascending=False)
        main_type_id = tipos.index[0]
        secondary_type_id = tipos.index[1] if len(tipos) > 1 else main_type_id
        
        # Hora pico
        peak_h = get_peak_hour(subset)
        
        adn_cards.append({
            "vialidad": calle,
            "etiqueta_riesgo": get_risk_label(igv_total, total_acc),
            "stats": {
                "accidentes": total_acc,
                "muertos": muertos,
                "heridos": heridos,
                "letalidad_index": letalidad
            },
            "adn": {
                "tipo_principal": tipaccid_map.get(main_type_id, "Otro"),
                "tipo_secundario": tipaccid_map.get(secondary_type_id, "Otro"),
                "hora_pico": f"{peak_h:02d}:00 hrs",
                "factor_distintivo": "Alta Frecuencia" if total_acc > 2000 else "Alta Letalidad"
            },
            "recomendacion": "Reducir velocidad y mantener distancia" if letalidad > 0.4 else "Atención a puntos ciegos y cruces"
        })

    output_file = os.path.join(output_dir, "adn_vial_hermosillo.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(adn_cards, f, ensure_ascii=False, indent=2)

    print(f"✅ ADN Vial generado en: {output_file}")

except Exception as e:
    print(f"❌ Error: {e}")
