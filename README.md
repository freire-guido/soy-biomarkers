# Motivación

Identificar biomarcadores, entendidos como genes con perfiles de expresión asociados a factores de estrés bióticos y abióticos, permite entender los procesos que originan respuestas a los estreses, diseñar estrategias de manejo de cultivos e incluso generar nuevas variedades de plantas capaces de prosperar en entornos adversos o de ofrecer un mayor rendimiento nutricional.

La relevancia de esta investigación se magnifica al considerar el rol fundamental de la soja en la economía argentina, donde representa aproximadamente el 30% de las exportaciones totales del país. Este cultivo no solo es crucial para el sector agroindustrial nacional, sino que también posiciona a Argentina como un actor estratégico en la seguridad alimentaria global. La optimización de su producción mediante la identificación de biomarcadores de resistencia resulta particularmente significativa dado que gran parte de las áreas de cultivo se encuentran expuestas a diversos factores de estrés ambiental, como sequías, salinidad y enfermedades patógenas. La mejora en la resistencia de la soja a estas condiciones adversas tendría un impacto directo en la sostenibilidad del sector agrícola argentino.

El proceso típico de investigación de biomarcadores consiste en tres partes fundamentales:

- Se cultiva la planta en condiciones de control y estrés.
- Se secuencian muestras de la planta en laboratorios (muchas veces tercerizados).
- Se comparan los datos transcriptómicos de las plantas utilizando métodos estadísticos.

En los últimos años, la secuenciación (generación de información genética) se ha vuelto mucho más accesible en precio y tiempo gracias a avances tecnológicos conocidos como NGS (*Next Generation Sequencing*). Las técnicas de machine learning gozaron avances muy parecidos, gracias al abaratamiento del poder de cómputo, que permite entrenar modelos más sofisticados con un presupuesto y tiempo menores.

A pesar de estos avances en ambos campos, el costo de secuenciación sigue siendo el principal cuello de botella a la hora de implementar machine learning moderno en la identificación de biomarcadores. Tener un tamaño de población mayor permitiría al investigador acceder a mejores modelos estadísticos, mejorar su eficacia e identificar más biomarcadores.

Es por esto que aprovechar los datos genéticos ya disponibles plantea un modelo de investigación *en seco* completamente distinto, donde el enfoque no está en cultivar plantas para cada experimento, sino que agregar los datos ya existentes. Los puntos principales del nuevo paradigma de investigación bioinformática son:

- Normalizar los datos de diversas fuentes en lugar de generarlos (haciendo la búsqueda de biomarcadores más económica).
- Generar anotaciones automáticamente usando sus metadatos (ahorrando tiempo).
- Usar modelos avanzados de machine learning para analizar los datos.

# Objetivos

En este trabajo, se busca identificar biomarcadores genéticos usando técnicas de machine learning diferentes a las tradicionales. A este fin, es necesario recopilar la mayor cantidad de datos genómicos de soja posible: implementamos una suite de herramientas que interactúan con las APIs de los principales repositorios de datos genómicos (SRA, GEO, etc.) para crear una base de datos de miles de muestras de plantas de soja.

También es central la curación y consolidación de metadatos de cada muestra, muchas veces fragmentados en las distintas plataformas. Además de la información genómica, es necesario poseer información sobre las condiciones de crecimiento y tratamiento de cada una de las muestras. Los modelos de machine learning van a intentar predecir estas condiciones basándose únicamente en la información genética.

El objetivo de un trabajo de modelado con machine learning suele ser producir un modelo con un alto poder predictivo. En este caso, si bien se utilizan métricas de exactitud como en aquellos trabajos, se busca explicar usando las variables que el modelo selecciona los genes e interacciones responsables de la resistencia a estreses. En estadística esto se conoce como inferencia.

# Trabajos previos

Utilizar más y mejores técnicas para analizar las expresiones genómicas es una temática central de la biología molecular. En los últimos años, el machine learning emergió como una herramienta poderosa para el análisis de datos genómicos, ofreciendo nuevas perspectivas más allá de los métodos estadísticos tradicionales. Los métodos clásicos para identificar biomarcadores genéticos en soja típicamente se han basado en estudios de asociación del genoma completo (GWAS) y análisis de expresión diferencial. Depeng et al. [1] realizaron un extenso estudio utilizando GWAS para identificar loci asociados con la resistencia a la sequía en soja, estableciendo un punto de referencia para los métodos tradicionales.

Sin embargo, las limitaciones de estos enfoques han llevado a la exploración de técnicas de machine learning. Nazari et al. [2] realizaron un meta-análisis con inteligencia artificial para identificar fenotipos de resistencia a partir de datos transcriptómicos, logrando identificar nuevos genes candidatos que los métodos estadísticos tradicionales no detectaron. De manera similar, Zhou et al. [3] aplicaron Random Forests para diferenciar infecciones de Covid y *Mycoplasma pneumoniae*.

Un trabajo particularmente relevante es el de Venancio et al. [4], quienes desarrollaron una pipeline integrada que combina datos genómicos de múltiples fuentes públicas para expresión diferencial por tejidos. Su análisis destaca la importancia de la integración de datos, aunque se limitaron a métodos estadísticos convencionales. En cuanto a la curación y consolidación de datos genómicos, Brancato et al. [5] crearon un framework para la normalización y estandarización de metadatos de expresión génica provenientes de diferentes repositorios públicos.

# Referencias

1. [A Nuclear Factor Y-B Transcription Factor, GmNFYB17, Regulates Resistance to Drought Stress in Soybean](https://doi.org/10.3390/ijms23137242) - Depeng, W. et al. (2022)
2. [Integrated transcriptomic meta‐analysis and comparative artificial intelligence models in maize under biotic stress](https://doi.org/10.1038/s41598-023-42984-4) - Nazari L. et al. (2023)
3. [Using random forest and biomarkers for differentiating COVID-19 and Mycoplasma pneumoniae infections](https://doi.org/10.1038/s41598-024-74057-5) - Zhou, X. et al. (2024)
4. [The Soybean Expression Atlas v2: A comprehensive database of over 5000 RNA-seq samples](https://doi.org/10.1111/tpj.16459) - Almeida-Silva F. et al. (2023)
5. [Standardizing digital biobanks: integrating imaging, genomic, and clinical data for precision medicine](https://doi.org/10.1186/s12967-024-04891-8) - Brancato, V. et al. (2024)
