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
