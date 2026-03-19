# Scripts / Lógica del Proyecto

Este directorio contiene los scripts de Python para el procesamiento, filtrado y combinación de datos de INEGI ATUS para el municipio de Hermosillo.

| Script | Propósito |
| :--- | :--- |
| `analyze_zip.py` | Análisis exploratorio inicial del dataset. |
| `combine_zips_hermosillo.py` | Une los años 2020-2024 desde los archivos ZIP. |
| `extract_hermosillo_shp.py` | Extrae el Shapefile base de Hermosillo. |
| `extract_hermosillo_fatales_shp.py` | Genera el Shapefile de accidentes con víctimas fatales. |
| `extract_hermosillo_all.py` | Genera el CSV completo para Hermosillo. |

### Uso
Todos los scripts están diseñados para ejecutarse con `uv run`:
```bash
uv run scripts/nombre_del_script.py
```
