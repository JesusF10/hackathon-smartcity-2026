#set page(paper: "a4", margin: (x: 2cm, y: 2cm))
#set text(font: "Liberation Sans", size: 10pt)

#align(center)[
  #text(size: 20pt, weight: "bold")[Diccionario de Variables H-Vial / H-Vital]
  #v(0.5em)
  #text(size: 14pt, fill: gray)[Dataset Histórico Hermosillo (2020-2024)]
]

#v(1em)
= Introducción
Este documento describe exhaustivamente las variables contenidas en el dataset consolidado de accidentes de tránsito en Hermosillo. La información proviene del INEGI (ATUS) y ha sido procesada para facilitar la identificación de puntos críticos para la campaña de seguridad vial.


== Identificación y Ubicación
#table(
  columns: (1.5fr, 1fr, 3fr, 2fr),
  fill: (x, y) => if y == 0 { gray.lighten(60%) },
  [*Variable*], [*Tipo*], [*Descripción*], [*Utilidad*],
  [`ID`], [str], [Identificador único del accidente.], [Filtrado espacial],
  [`EDO`], [int64], [Código del Estado (Sonora = 26).], [Filtrado espacial],
  [`MPIO`], [int64], [Código del Municipio (Hermosillo = 30).], [Filtrado espacial],
  [`URBANA`], [int64], [Indicador de accidente en zona urbana.], [Filtrado espacial],
  [`SUBURBANA`], [int64], [Indicador de accidente en zona suburbana.], [Filtrado espacial],
  [`CALLE1`], [str], [Vialidad principal del accidente.], [Filtrado espacial],
  [`CALLE2`], [str], [Vialidad secundaria o intersección.], [Filtrado espacial],
  [`CARRETERA`], [str], [Nombre de la carretera si aplica.], [Filtrado espacial],
  [`LONGITUD`], [float64], [Coordenada geográfica X.], [Filtrado espacial],
  [`LATITUD`], [float64], [Coordenada geográfica Y.], [Filtrado espacial],
)

== Cronología
#table(
  columns: (1.5fr, 1fr, 3fr, 2fr),
  fill: (x, y) => if y == 0 { gray.lighten(60%) },
  [*Variable*], [*Tipo*], [*Descripción*], [*Utilidad*],
  [`ANIO`], [int64], [Año de ocurrencia (2020-2024).], [Análisis de tendencias],
  [`MES`], [int64], [Mes (1-12).], [Análisis de tendencias],
  [`DIA`], [int64], [Día del mes.], [Análisis de tendencias],
  [`DIASEMANA`], [int64], [Día de la semana (1:Domingo a 7:Sábado o similar).], [Análisis de tendencias],
  [`HORA`], [int64], [Hora del día (0-23).], [Análisis de tendencias],
  [`MINUTOS`], [int64], [Minuto de la hora.], [Análisis de tendencias],
)

== Tipología y Causa
#table(
  columns: (1.5fr, 1fr, 3fr, 2fr),
  fill: (x, y) => if y == 0 { gray.lighten(60%) },
  [*Variable*], [*Tipo*], [*Descripción*], [*Utilidad*],
  [`TIPACCID`], [int64], [Tipo de siniestro (Choque, volcadura, atropello, etc.).], [Identificación de patrones],
  [`CLASE`], [int64], [Severidad (1:Fatal, 2:No Fatal, 3:Solo daños).], [Identificación de patrones],
  [`CAUSAACCI`], [int64], [Causa probable (Conductor, Peatón, Falla mecánica, etc.).], [Identificación de patrones],
  [`CAPAROD`], [int64], [Tipo de superficie de rodamiento.], [Identificación de patrones],
)

== Vehículos Involucrados
#table(
  columns: (1.5fr, 1fr, 3fr, 2fr),
  fill: (x, y) => if y == 0 { gray.lighten(60%) },
  [*Variable*], [*Tipo*], [*Descripción*], [*Utilidad*],
  [`AUTOMOVIL`], [int64], [Cantidad de automóviles.], [Perfil de riesgo],
  [`CAMPASAJ`], [int64], [Cantidad de camionetas de pasajeros.], [Perfil de riesgo],
  [`MICROBUS`], [int64], [Cantidad de microbuses.], [Perfil de riesgo],
  [`PASCAMION`], [int64], [Cantidad de camiones de pasajeros.], [Perfil de riesgo],
  [`OMNIBUS`], [int64], [Cantidad de ómnibus.], [Perfil de riesgo],
  [`TRANVIA`], [int64], [Cantidad de tranvías o trenes ligeros.], [Perfil de riesgo],
  [`CAMIONETA`], [int64], [Cantidad de camionetas de carga.], [Perfil de riesgo],
  [`CAMION`], [int64], [Cantidad de camiones de carga.], [Perfil de riesgo],
  [`TRACTOR`], [int64], [Cantidad de tractores.], [Perfil de riesgo],
  [`FERROCARRI`], [int64], [Cantidad de locomotoras.], [Perfil de riesgo],
  [`MOTOCICLET`], [int64], [Cantidad de motocicletas.], [Perfil de riesgo],
  [`BICICLETA`], [int64], [Cantidad de bicicletas.], [Perfil de riesgo],
  [`OTROVEHIC`], [int64], [Otros tipos de vehículos.], [Perfil de riesgo],
)

== Víctimas y Seguridad
#table(
  columns: (1.5fr, 1fr, 3fr, 2fr),
  fill: (x, y) => if y == 0 { gray.lighten(60%) },
  [*Variable*], [*Tipo*], [*Descripción*], [*Utilidad*],
  [`SEXO`], [int64], [Sexo del conductor responsable.], [Medición de impacto social],
  [`ALIENTO`], [int64], [Presencia de aliento alcohólico.], [Medición de impacto social],
  [`CINTURON`], [int64], [Uso del cinturón de seguridad.], [Medición de impacto social],
  [`EDAD`], [int64], [Edad del conductor.], [Medición de impacto social],
  [`CONDMUERTO`], [int64], [Conductores fallecidos.], [Medición de impacto social],
  [`CONDHERIDO`], [int64], [Conductores heridos.], [Medición de impacto social],
  [`PASAMUERTO`], [int64], [Pasajeros fallecidos.], [Medición de impacto social],
  [`PASAHERIDO`], [int64], [Pasajeros heridos.], [Medición de impacto social],
  [`PEATMUERTO`], [int64], [Peatones fallecidos.], [Medición de impacto social],
  [`PEATHERIDO`], [int64], [Peatones heridos.], [Medición de impacto social],
  [`CICLMUERTO`], [int64], [Ciclistas fallecidos.], [Medición de impacto social],
  [`CICLHERIDO`], [int64], [Ciclistas heridos.], [Medición de impacto social],
  [`OTROMUERTO`], [int64], [Otras personas fallecidas.], [Medición de impacto social],
  [`OTROHERIDO`], [int64], [Otras personas heridas.], [Medición de impacto social],
  [`TOTMUERTOS`], [int64], [Total general de fallecidos.], [Medición de impacto social],
  [`TOTHERIDOS`], [int64], [Total general de heridos.], [Medición de impacto social],
)
