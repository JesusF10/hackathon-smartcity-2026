# Scripts / Lógica del Proyecto

Este directorio contiene los scripts de Python para el procesamiento, filtrado, combinación y visualización de datos de INEGI ATUS para el municipio de Hermosillo.

| Script | Propósito |
| :--- | :--- |
| `analyze_zip.py` | Análisis exploratorio inicial del dataset. |
| `combine_zips_hermosillo.py` | Une los años 2020-2024 desde los archivos ZIP. |
| `extract_hermosillo_shp.py` | Extrae el Shapefile base de Hermosillo. |
| `extract_hermosillo_fatales_shp.py` | Genera el Shapefile de accidentes con víctimas fatales. |
| `extract_hermosillo_all.py` | Genera el CSV completo para Hermosillo. |
| `analyze_risk_causes.py` | Identifica causas de riesgo principales (imprudencia, celular). |
| `generate_intersection_ranking.py`| Top de cruceros peligrosos en Hermosillo. |
| `generate_victim_heatmaps.py` | Mapas de calor de lesionados y muertos. |
| `generate_speed_risk_map.py` | Análisis de relación entre velocidad y fatalidad. |
| `generate_collision_typology_2024.py` | Desglose de tipos de choque (frontal, alcance, etc). |
| `generate_adn_cards.py` | Genera perfiles visuales "ADN" de accidentes individuales. |
| `generate_multilevel_map_data.py`| Prepara capas de datos jerárquicas para visualización web. |
| `generate_interactive_charts.py`| Genera visualizaciones interactivas con Vega-Lite. |
| `export_geojson_web.py` | Exporta datos geoespaciales optimizados para la web. |

### Uso
Todos los scripts están diseñados para ejecutarse con `uv run`:
```bash
uv run scripts/nombre_del_script.py
```
