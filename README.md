## Análisis de Satisfacción y Retención de Empleados en ABC Corporation 📊🤝

En el competitivo entorno empresarial actual, la **retención de empleados** y la **satisfacción laboral** son cruciales para el éxito. Por ello, **ABC Corporation** confió en **Ikigai Nexus** para realizar un análisis de datos exhaustivo.

🎯 **Nuestro objetivo:** Identificar los factores clave que influyen en la satisfacción laboral y fortalecer la retención de talento en ABC Corporation.

En este proyecto, exploramos, transformamos y visualizamos los datos proporcionados por ABC, diseñamos una base de datos y creamos un proceso ETL automatizado.

📂 **Estructura del Proyecto:**

```
.
├── EDA y limpieza_Final.ipynb
├── Transformando_el_talento_Final.csv
├── Visualizacion_Final.ipynb
├── BONUS 1 - Conexion Py-SQL.ipynb
├── BONUS 2 - Creación de una ETL.py
└── README.md
```

⚙️ **Tecnologías Utilizadas:** Python, SQL, Pandas, NumPy, Matplotlib, Seaborn, SciPy, MySQL Connector.

🛠️ **Instalación:**

```bash
git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
cd tu_repositorio
pip install -r requirements.txt
```

🚀 **Ejecución:** Abre `EDA y limpieza.Final.ipynb` en Jupyter y ejecuta las celdas.

🔍 **Análisis Principales:**

* **Distribución de Género**: Análisis de la distribución de género en la empresa.
* **Imputación y Detección de Valores Nulos**: Imputación de valores nulos en variables numéricas y categóricas.
* **Homogeneización de Columnas**: No se detectaron valores duplicados. Renombrado y limpieza de nombres de columnas.
* **Creación de Base de Datos MySQL**:  Creación de una base de datos MySQL para almacenar la información procesada.
* **Visualizaciones: (Histplot, Boxplot, Barplot, etc.)**

💪 **Retos y Logros:** Garantizar la calidad de los datos y transformar la información en recomendaciones accionables para mejorar la experiencia de los empleados.

Uno de los mayores retos ha sido garantizar la calidad de los datos y la creación de modelos predictivos precisos. Este proceso ha permitido al equipo desarrollar soluciones efectivas y basadas en evidencias.

El aspecto que más orgullo genera en el equipo es la capacidad de transformar datos en recomendaciones concretas que pueden mejorar significativamente la experiencia de los empleados en la empresa.


 **Fases del Proyecto**

1.  **Análisis Exploratorio de Datos (EDA)** En esta fase, hemos realizado un análisis exploratorio detallado del conjunto de datos, estudiando las variables y sus tipos, los estadísticos principales, seleccionando la información más relevante para la realización posterior de los análisis.

2.  **Transformación de los Datos** Hemos revisado los títulos y contenidos de las variables, homogeneizándolos. Hemos revisado errores ortográficos, eliminado columnas redundantes. Hemos explorado los datos faltantes e imputado cuando ha sido posible, con las indicaciones del cliente o en base a los estudios de imputación realizados. Tras las transformaciones realizadas hemos obtenido un archivo .csv apropiado para realizar los análisis solicitados por el cliente, que posteriormente utilizamos para la visualización de los gráficos.

3.  **Diseño de BBDD e Inserción de los Datos** Diseño de la Estructura de la Base de Datos: Se ha definido la estructura de la base de datos: las tablas necesarias y sus relaciones, así como las claves primarias y foráneas.
Creación de la Base de Datos: Hemos creado la base de datos utilizando Python y SQL MyWorkBench.
Inserción de Datos Iniciales: Se han insertado los datos de plantilla de la empresa en la base de datos generada.

4.  **Creación de una ETL (automatización de la carga y transformación de datos)** El objetivo de esta etapa fue automatizar la inserción de datos en la base de datos relacional y garantizar que la información se actualiza de manera consistente y también automatizar el proceso de transformación de la información antes de la inserción en la BBDD.

5.  **Reporte de los Resultados (con visualizaciones en Python)** El objetivo de esta fase es proporcionar a ABC Corporation un informe detallado del contexto general de la empresa utilizando visualizaciones en Python. Este informe permite una comprensión más profunda de la situación actual y sirve como base para la toma de decisiones informadas.


🤝 **Equipo:**

* **Andrea Garrido:** Scrum Master
* **Evelina Saponjic Jovanovic:** Data Analyst
* **Arellis Carla Quispe Torres:** Data Analyst
* **Marta Gómez:** Data Analyst
* **Lorena Núñez Santaemilia:** Data Analyst
