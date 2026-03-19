#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.5cm),
  header: align(right)[H-Vial / H-Vital | Reporte 2024],
  footer: context [
    #h(1fr)
    #counter(page).display()
  ]
)

#set text(
  font: "Liberation Sans",
  size: 11pt,
  lang: "es"
)

#align(center)[
  #v(1em)
  #text(size: 24pt, weight: "bold")[Reporte de Siniestralidad Vial]
  #v(0.5em)
  #text(size: 16pt, fill: gray)[Municipio de Hermosillo, Sonora]
  #v(1em)
  #datetime.today().display("[day] de [month repr:long] de [year]")
]

#v(2em)

= 1. Resumen Ejecutivo
El presente reporte detalla los siniestros viales ocurridos en el municipio de Hermosillo durante el año 2024, basados en el dataset ATUS de INEGI. El objetivo es identificar patrones que permitan la implementación de la campaña *H-Vial / H-Vital*.

#table(
  columns: (1fr, 1fr),
  inset: 10pt,
  align: center,
  stroke: none,
  fill: (x, y) => if calc.even(y) { gray.lighten(90%) },
  [*Indicador*], [*Valor*],
  [Total de Accidentes], [11,801],
  [Total de Fallecidos], [89],
  [Total de Heridos], [892],
  [Promedio Mensual], [~983],
)

= 2. Gravedad de los Accidentes (Clase)
La mayoría de los eventos resultaron en daños materiales, sin embargo, el número de fatalidades subraya la urgencia de intervenciones visuales.

- *Fatal (1):* 86 accidentes (0.7%)
- *No Fatal (2):* 764 accidentes (6.5%)
- *Sólo Daños (3):* 10,951 accidentes (92.8%)

= 3. Tipología de Siniestros
Los choques entre vehículos automotores dominan la estadística, seguidos por incidentes con motocicletas.

#table(
  columns: (auto, 1fr, auto),
  fill: (x, y) => if y == 0 { gray.lighten(60%) },
  [*Código*], [*Tipo de Accidente*], [*Frecuencia*],
  [1], [Colisión con vehículo automotor], [9,284],
  [10], [Colisión con motocicleta], [1,039],
  [4], [Colisión con objeto fijo], [760],
  [2], [Colisión con peatón (Atropellamiento)], [287],
  [11], [Colisión con ciclista], [157],
  [6], [Caída de pasajero], [114],
  [5], [Volcadura], [94],
  [7], [Salida del camino], [65],
)

= 4. Análisis Geográfico: Puntos Críticos
Las siguientes vialidades presentan la mayor concentración de accidentes:

1. *Bulevar Solidaridad:* 928 accidentes.
2. *José María Morelos y Pavón:* 442 accidentes.
3. *Jesús García Morales:* 428 accidentes.
4. *Antonio Quiroga:* 409 accidentes.
5. *Luis Encinas Johnson:* 408 accidentes.

= 5. Factores Temporales
*Hora Crítica:* La mayor incidencia ocurre a las 14:00 horas, con 1,302 registros.
*Meses Críticos:* Mayo (1,132) y Junio (1,055) registraron los picos más altos del año.

#pagebreak()

= 6. Diccionario de Variables y Significado
A continuación se detallan todas las variables contenidas en el dataset analizado para Hermosillo.

== 6.1 Identificación y Geografía
- *ID*: Identificador único del registro de accidente.
- *EDO / MPIO*: Códigos numéricos del Estado (26) y Municipio (30).
- *URBANA / SUBURBANA*: Indicadores de si el evento ocurrió en zona urbana o suburbana.
- *CALLE1 / CALLE2 / CARRETERA*: Nombres de las vialidades donde ocurrió el siniestro.
- *LONGITUD / LATITUD*: Coordenadas exactas para mapeo geoespacial.
- *geometry*: Objeto geométrico (Punto) utilizado por Geopandas.

== 6.2 Variables Temporales
- *ANIO / MES / DIA*: Fecha exacta del siniestro.
- *DIASEMANA*: Código del día de la semana (1-7).
- *HORA / MINUTOS*: Tiempo preciso del impacto.

== 6.3 Clasificación del Accidente
- *TIPACCID*: Tipo de evento (Colisión, atropello, volcadura, etc.).
- *CLASE*: Nivel de gravedad (Fatal, No Fatal, Solo Daños).
- *CAUSAACCI*: Factor determinante del accidente (Conductor, falla mecánica, etc.).
- *CAPAROD*: Tipo de superficie (Pavimentada, terracería, etc.).

== 6.4 Conteo de Víctimas (Muertos y Heridos)
El dataset desglosa las víctimas por su rol en el accidente:
- *CONDMUERTO / CONDHERIDO*: Conductores.
- *PASAMUERTO / PASAHERIDO*: Pasajeros.
- *PEATMUERTO / PEATHERIDO*: Peatones.
- *CICLMUERTO / CICLHERIDO*: Ciclistas.
- *OTROMUERTO / OTROHERIDO*: Otros roles.
- *TOTMUERTOS / TOTHERIDOS*: Sumatoria total de víctimas por evento.

== 6.5 Perfil del Conductor y Vehículo
- *SEXO*: Género del conductor presunto responsable.
- *ALIENTO*: Indica si había aliento alcohólico.
- *CINTURON*: Indica si el conductor portaba el cinturón de seguridad.
- *EDAD*: Edad del conductor.
- *AUTOMOVIL, MOTOCICLET, etc.*: Indicadores (0/1) del tipo de vehículos involucrados.

#v(2em)
#align(center)[
  #block(
    fill: black,
    inset: 15pt,
    radius: 5pt,
    text(fill: white, weight: "bold")[NO USES EL CELULAR AL CONDUCIR]
  )
]
