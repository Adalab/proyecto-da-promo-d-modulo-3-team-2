Análisis de Satisfacción y Retención de los Empleados en la empresa ABC Corporation

Descripción:

En el entorno empresarial altamente competitivo de hoy en día, la retención de empleados y la satisfacción en el trabajo son cuestiones críticas para cualquier organización, ya que afectan directamente a la productividad, el compromiso y la motivación de los trabajadores, y por ende a la rentabilidad.

Con el objetivo de reducir la rotación de personal y mejorar la satisfacción en el trabajo de los empleados de ABC Corporation, nuestra empresa, Ikigai Nexus, ha sido contratada para desarrollar un proyecto de análisis de datos. 

Nuestra misión fue identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención del talento de la empresa.

En este repositorio, presentamos los resultados de nuestro análisis exploratorio de los datos que nos ha proporcionado ABC, transformación de los datos, visualizaciones, diseño de BBDD y creación de una ETL. 

Estructura del proyecto: 

EDA y limpieza.Final: Notebook principal donde se realizan las transformaciones y análisis de datos.

Transformando_el_talento_Final.csv: Dataset con los datos explorados y transformados.

Visualizacion.Final: Notebook secundario con los gráficos y visualizaciones.

BONUS 1 - Conexion Py-SQL: Notebook de conexión entre Python y MySQL.

BONUS 2 - Creación de una ETL - El archivo que contiene pautas para el proceso automatizado de carga de datos.

README.md: Este archivo, que describe el proyecto entero y cómo ejecutarlo.

Requisitos:

Python 3.7+

Jupyter Notebook

Pandas

NumPy

Matplotlib

Seaborn

SciPy

MySQL Connector

Tecnologías Utilizadas:

Python: Para análisis y modelado de datos.

SQL: Para la gestión y consulta de bases de datos.

Pandas, NumPy: Para manipulación y análisis de datos.

Machine Learning: Para la construcción de modelos predictivos.

Instalación: 

Clonar el repositorio:

git clone https://github.com/tu_usuario/tu_repositorio.git

Navegar al directorio del proyecto:

cd tu_repositorio

Instalar las dependencias:

pip install -r requirements.txt

Ejecución:

Abrir el notebook en Jupyter: EDA y limpieza.Final.ipynb

Ejecutar las celdas del notebook para realizar las transformaciones y análisis de datos.

Análisis Principales Realizados, entre otros: 

Distribución de Género: Análisis de la distribución de género en la empresa.

Imputación y Detección de Valores Nulos: Imputación de valores nulos en variables numéricas y categóricas.

Identificación y detección Valores Duplicados: No se detectaron valores duplicados.

Homogeneización de columnas: Renombrado y limpieza de nombres de columnas.

Creación de Base de Datos: Creación de una base de datos MySQL para almacenar la información procesada.

Visualizaciones: Histplot, Boxplot, Barplot et al., para apoyar los resultados.

Retos y Logros:

Uno de los mayores retos ha sido garantizar la calidad de los datos y la creación de modelos predictivos precisos. Este proceso ha permitido al equipo desarrollar soluciones efectivas y basadas en evidencias.

El aspecto que más orgullo genera en el equipo es la capacidad de transformar datos en recomendaciones concretas que pueden mejorar significativamente la experiencia de los empleados en la empresa.

Fases del proyecto:

Fase 1: Análisis Exploratorio de Datos (EDA).

En esta fase, hemos realizado un análisis exploratorio detallado del conjunto de datos, estudiando las variables y sus tipos, los estadísticos principales, seleccionando la información más relevante para la realización posterior de los análisis.

Fase 2: Transformación de los datos.

Hemos revisado los títulos y contenidos de las variables, homogeneizándolos. Hemos revisado errores ortográficos, eliminado columnas redundantes. Hemos explorado los datos faltantes e imputado cuando ha sido posible, con las indicaciones del cliente o en base a los estudios de imputación realizados. Tras las transformaciones realizadas hemos obtenido un archivo .csv apropiado para realizar los análisis solicitados por el cliente, que posteriormente utilizamos para la visualización de los gráficos.

Fase 3: Diseño de BBDD e Inserción de los Datos (estructura).

Diseño de la Estructura de la Base de Datos: Se ha definido la estructura de la base de datos: las tablas necesarias y sus relaciones, así como las claves primarias y foráneas.

Creación de la Base de Datos: Hemos creado la base de datos utilizando Python y SQL MyWorkBench.

Inserción de Datos Iniciales: Se han insertado los datos de plantilla de la empresa en la base de datos generada.

Fase 4: Creación de una ETL.

El objetivo de esta etapa fue automatizar la inserción de datos en la base de datos relacional y garantizar que la información se actualiza de manera consistente y también automatizar el proceso de transformación de la información antes de la inserción en la BBDD.

Fase 5: Reporte de los resultados.

El objetivo de esta fase es proporcionar a ABC Corporation un informe detallado del contexto general de la empresa utilizando visualizaciones en Python. Este informe permite una comprensión más profunda de la situación actual y sirve como base para la toma de decisiones informadas.

Equipo:

—Andrea Garrido (scrum master)

—Evelina Saponjic Jovanovic (data analyst)

—Arellis Carla Quispe Torres(data analyst)

—Marta Gómez (data analyst)

—Lorena Núñez Santaemilia (data analyst)
