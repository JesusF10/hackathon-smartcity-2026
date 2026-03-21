# Ángeles Viales

<p align="center">
  <img src="docs/logo-chilo-sin-letra.png" alt="Ángeles Viales Logo" width="200">
</p>

> Reduciendo siniestros viales a través de la conciencia visual y el análisis de datos en Hermosillo.

## Dashboard Interactivo
Puedes consultar el mapa de riesgo y las estadísticas en tiempo real en:
[https://jesusflores.me/projects/hackathon/angelesviales](https://jesusflores.me/projects/hackathon/angelesviales)

## El Desafío en Hermosillo
Hermosillo enfrenta una crisis de seguridad vial crítica:
*   **1er Lugar Nacional** en muertes por accidentes viales.
*   **2do Lugar Nacional** en número total de siniestros.
*   **Población en Riesgo:** ~936,263 habitantes.
*   **Causas:** El uso del móvil y conductas imprudentes son los principales detonantes de choques y volcaduras mortales.

## La Solución: Ángeles Viales
Una arquitectura de intervención dual que evoluciona la campaña de **"Estrellas Negras"** (Bogotá, 2003) para la realidad de Hermosillo:

### 1. Intervención Física (Estrellas Negras)
Colocación de **marcadores visuales y señalética de alto impacto** en el pavimento de zonas críticas. No es aleatorio; se basa en un **Visor Geográfico Cuádruple** que analiza:
*   Historial detallado de incidentes (2020-2024).
*   Mapas de calor por tipo de movilidad (peatones, ciclistas, motociclistas).
*   Zonas de velocidades mortales (alta energía cinética).
*   Horarios de máxima siniestralidad.

### 2. Ecosistema Digital
*   **Visor Geográfico:** Cuatro capas de análisis dinámico para visualización de riesgo.
*   **Radiografía de Riesgo:** Diagnósticos de vialidades peligrosas y perfiles "ADN Vial".
*   **Prevención Activa:** Cambio de enfoque de la multa (castigo) a la conciencia (prevención visual).

## Stack Técnico
*   **Análisis de Datos:** Python (`pandas`, `geopandas`, `altair`).
*   **Visualización Web:** Astro, MapLibre GL, Vega-Lite.
*   **Reporteo:** Typst (PDF de alta fidelidad).
*   **Gestión:** `uv` para dependencias de Python.

## Datos
El proyecto utiliza el dataset de **Accidentes de Tránsito en Zonas Urbanas y Suburbanas (ATUS) 2024** de INEGI, filtrado específicamente para el municipio de **Hermosillo, Sonora**.

## Inicio Rápido

Este proyecto utiliza [uv](https://github.com/astral-sh/uv) para la gestión de dependencias.

```bash
# Clonar el proyecto
git clone <url-del-repositorio>

# Instalar dependencias
uv sync

# Ejecutar el análisis principal
uv run scripts/analyze_zip.py
```

## Estructura del Proyecto
- `data/`: Contiene el dataset original y los archivos procesados.
- `scripts/`: Logica de procesamiento y extraccion.
- `reports/`: Reportes generados en PDF y fuentes Typst.
- `GEMINI.md`: Guia de contexto y mandatos para el asistente de IA.

## Bibliografia
- **INEGI (2024):** Accidentes de Transito en Zonas Urbanas y Suburbanas (ATUS). Disponible en: [https://www.inegi.org.mx/app/descarga/ficha.html?tit=81640&ag=0&f=csv](https://www.inegi.org.mx/app/descarga/ficha.html?tit=81640&ag=0&f=csv)
