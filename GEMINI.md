# GEMINI.md - Ángeles Viales

## Project Mission
**Ángeles Viales** is a road safety initiative designed to reduce traffic accidents caused by mobile phone use and reckless driving in Hermosillo, Sonora.
 Inspired by Colombia's "Estrellas Negras" campaign, the project combines physical visual markers in the city with digital data analysis to raise awareness and save lives.

## Foundational Mandates
- **Contextual Precedence:** All operations must align with the goal of identifying high-risk zones for visual intervention.
- **Data Integrity:** Use the processed INEGI ATUS (Accidentes de Tránsito en Zonas Urbanas y Suburbanas) 2020-2024 dataset.
- **Privacy:** Anonymized geospatial data is the core of our analysis.
- **Technical Stack:** Use `geopandas`, `pandas`, `matplotlib`, and `typst`. Manage dependencies with `uv`.

## Project Structure
- `scripts/`: Python logic for ETL and analysis.
- `data/`: Processed geospatial and tabular datasets (Hermosillo only).
- `reports/`: PDF reports and Typst sources.
- `docs/`: Extra project documentation.

## Key Symbols & Entities
- **Fatal Accidents:** Records where `TOTMUERTOS > 0`.
- **Intervention Points:** Clusters of fatal accidents for "Estrellas Negras" placement.

## Design Principles
- **Aesthetic:** High-contrast visuals (Black/Yellow).
- **Impact:** Use data to drive visual change in urban infrastructure.
