# CHANGES_GEMINI.md

Este archivo registra los cambios estructurales y estratégicos realizados durante el Hackathon Smart City 2026.

## [2026-03-18] - Reorganización para Agilidad
### Agregado
- Directorio `scripts/` para centralizar la lógica de procesamiento.
- Directorio `reports/` para centralizar la documentación técnica y PDF.
- `data/processed/` para separar los datos limpios de los archivos de origen.
- `CHANGES_GEMINI.md` para seguimiento de evolución del asistente.

### Cambiado
- Estructura de archivos de plana a jerárquica para mejor mantenibilidad en equipos.
- `GEMINI.md` actualizado con los nuevos mandatos de estructura y enfoque histórico (2020-2024).

### Eliminado
- Archivos ZIP nacionales originales de INEGI (300MB+ de datos redundantes).
- Carpetas temporales de extracción nacional.
- Scripts duplicados en raíz.

## [2026-03-21] - Galería de Activos y Visualización
### Agregado
- Incorporación de `docs/captura-mapa.png` al README para mostrar el Dashboard Interactivo.
- Incorporación de `docs/calle-logo.png` al README para ilustrar la propuesta de intervención física en calles.

## [2026-03-21] - Actualización de Contenido Web y Métricas
### Agregado
- Integración de métricas de siniestralidad de Hermosillo (1er Lugar Nacional en fatalidades).
- Detalles técnicos del stack web (Astro, MapLibre GL).
- Explicación del Visor Geográfico Cuádruple y la metodología de intervención física.

## [2026-03-21] - Identidad Visual y Documentación Local
### Agregado
- Integración de logo oficial `docs/logo-chilo-sin-letra.png` en el `README.md` global.
- Catálogo de documentación por carpeta (`scripts/`, `data/`, `reports/`).

## [2026-03-21] - Rebranding a Ángeles Viales
### Cambiado
- Nombre del proyecto de "H-Vial / H-Vital" a **Ángeles Viales**.
- `README.md`: Actualización de nombre y adición de sección para el Dashboard interactivo.
- `GEMINI.md`: Actualización de misión del proyecto y encabezados.
- `pyproject.toml`: Renombrado de paquete a `angeles-viales` y actualización de descripción.

## [2026-03-21] - Análisis de Riesgo y Documentación
### Agregado
- `scripts/analyze_risk_causes.py`: Identificación de causas principales (imprudencia, celular).
- `scripts/generate_intersection_ranking.py`: Top de cruceros peligrosos en Hermosillo.
- `scripts/generate_victim_heatmaps.py`: Mapas de calor de lesionados y muertos.
- `scripts/generate_speed_risk_map.py`: Análisis de relación entre velocidad y fatalidad.
- `scripts/generate_collision_typology_2024.py`: Desglose de tipos de choque (frontal, alcance, etc).
- `scripts/generate_adn_cards.py`: Generación de tarjetas "ADN" para perfiles de accidentes individuales.
- `scripts/generate_multilevel_map_data.py`: Capas jerárquicas (punto, zona, sector) para visualización web.

### Cambiado
- `scripts/README.md`: Documentación exhaustiva de todos los scripts de análisis y visualización.
- Refinamiento de `scripts/export_geojson_web.py` y `scripts/generate_interactive_charts.py` para mejor integración con el front-end.
- Actualización de `CHANGES_GEMINI.md` para seguimiento de progreso.
