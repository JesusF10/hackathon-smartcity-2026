# GEMINI.md - H-Vial / H-Vital

## Project Mission
**H-Vial / H-Vital** is a road safety initiative designed to reduce traffic accidents caused by mobile phone use and reckless driving in Hermosillo, Sonora. Inspired by Colombia's "Estrellas Negras" campaign, the project combines physical visual markers in the city with digital data analysis to raise awareness and save lives.

## Foundational Mandates
- **Contextual Precedence:** All operations must align with the goal of identifying high-risk zones for visual intervention.
- **Data Integrity:** Use the INEGI ATUS (Accidentes de Tránsito en Zonas Urbanas y Suburbanas) 2024 dataset as the primary source for analysis.
- **Privacy:** Never expose specific personal identifiers from accident records if they were to exist (currently working with anonymized statistical/geospatial data).
- **Technical Stack:** Use `geopandas`, `pandas`, and `matplotlib` for analysis. Manage dependencies with `uv`.

## Key Symbols & Entities
- **Fatal Accidents:** Records where `TOTMUERTOS > 0` or `CLASE == 1`.
- **Target Zones:** Clusters of accidents involving "Colisión con objeto fijo" (Type 4) or "Volcadura" (Type 5).
- **Output:** Geospatial CSVs and maps intended for urban planning and public awareness.

## Design Principles
- **Aesthetic:** High-contrast visuals (Black/Yellow) reflecting the "Estrellas Negras" inspiration.
- **Clarity:** Data visualizations must be accessible to both urban planners and the general public.
