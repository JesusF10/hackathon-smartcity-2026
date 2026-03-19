# Documentación de Datos - ATUS 2024

## Origen
**Fuente:** INEGI - Accidentes de Tránsito en Zonas Urbanas y Suburbanas (Georreferenciado).
**Año:** 2024 (Publicado en 2025).
**Ubicación original:** `data/atus_2024_shp.zip`

## Diccionario de Variables Clave (H-Vial)

| Variable | Descripción | Valores Relevantes |
| :--- | :--- | :--- |
| `EDO` | Estado | 26 (Sonora) |
| `MPIO` | Municipio | 30 (Hermosillo) |
| `CLASE` | Gravedad | 1: Fatal, 2: No fatal, 3: Solo daños |
| `TIPACCID` | Tipo de Accidente | 4: Objeto Fijo, 5: Volcadura, 10: Moto |
| `TOTMUERTOS` | Total de Fallecidos | > 0 para intervenciones críticas |
| `geometry` | Ubicación | Puntos (Longitud, Latitud) |

## Procesamiento Realizado
1. **Filtrado Espacial:** Reducción a registros con `EDO=26` y `MPIO=30`.
2. **Filtrado por Gravedad:** Extracción de registros con al menos una persona fallecida (`TOTMUERTOS > 0`).
3. **Exportación:** Generación de `hermosillo_accidentes_fatales_2024.csv` para uso en mapeo visual.
