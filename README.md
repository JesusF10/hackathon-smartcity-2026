<<<<<<< HEAD
# H-Vial / H-Vital 🚗⭐

> Reduciendo siniestros viales a través de la conciencia visual y el análisis de datos.

## 🌟 Inspiración
Inspirado en la campaña **"Estrellas Negras"** de Colombia (iniciada por Antanas Mockus en 2003), donde marcas en el asfalto señalan los puntos exactos donde ocurrieron accidentes mortales. **H-Vial / H-Vital** busca adaptar este concepto a la realidad local, utilizando datos para identificar dónde la imprudencia y el uso del celular cobran vidas.

## 🎯 El Problema
El uso del teléfono móvil y conductas imprudentes del conductor derivan constantemente en choques, volcaduras y atropellamientos. Estos eventos no son solo estadísticas; son puntos de dolor en nuestra infraestructura urbana.

## 🛠️ La Solución
Una arquitectura dual:
1.  **Elementos Visuales:** Señalética física en puntos críticos identificados mediante análisis geoespacial.
2.  **Campaña Informativa:** Recursos digitales basados en datos reales para concientizar a conductores y peatones.

## 📊 Datos
El proyecto utiliza el dataset de **Accidentes de Tránsito en Zonas Urbanas y Suburbanas (ATUS) 2024** de INEGI, filtrado específicamente para el municipio de **Hermosillo, Sonora**.

## 🚀 Inicio Rápido

Este proyecto utiliza [uv](https://github.com/astral-sh/uv) para la gestión de dependencias.

```bash
# Clonar el proyecto
git clone <url-del-repositorio>

# Instalar dependencias
uv sync

# Ejecutar el análisis principal
uv run python analyze_zip.py
```

## 🏗️ Estructura del Proyecto
- `data/`: Contiene el dataset original y los archivos procesados.
- `extract_hermosillo_fatales.py`: Script de filtrado de datos para Hermosillo.
- `hermosillo_accidentes_fatales_2024.csv`: Datos de accidentes con víctimas fatales.
- `GEMINI.md`: Guía de contexto y mandatos para el asistente de IA.
=======
# hackathon-smartcity-2026
Smartcity Hackathon 2026
>>>>>>> c82cc55ac07d66076804827c98369a3a67db21c0
