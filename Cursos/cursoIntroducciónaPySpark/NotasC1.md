# Esquema del curso

En este capítulo, aprenderás cómo gestiona Spark los datos y cómo leer y escribir tablas desde Python.

- ¿Qué es la Chispa?
- Uso de Spark en Python
- Examen de SparkContext
- Uso de DataFrames
- Creación de SparkSession
- Visualización de tablas
- ¿Algo que consultar?
- Pandafy en Spark DataFrame
- Pon algo de Spark en tus datos
- Abandono del intermediario

# ¿Qué es la Chispa?

Spark es una plataforma para la computación en clúster. Spark te permite distribuir datos y cálculos en clusters con múltiples nodos (piensa en cada nodo como un ordenador independiente). Dividir tus datos facilita el trabajo con conjuntos de datos muy grandes, porque cada nodo sólo trabaja con una pequeña cantidad de datos.

Como cada nodo trabaja en su propio subconjunto de los datos totales, también realiza una parte de los cálculos totales necesarios, de modo que tanto el procesamiento de los datos como el cálculo se realizan en paralelo en los nodos del clúster. Es un hecho que la computación paralela puede hacer que ciertos tipos de tareas de programación sean mucho más rápidas.

Sin embargo, una mayor potencia de cálculo conlleva una mayor complejidad.

Decidir si Spark es o no la mejor solución para tu problema requiere cierta experiencia, pero puedes plantearte preguntas como:

    ¿Mis datos son demasiado grandes para trabajar con ellos en una sola máquina?
    ¿Se pueden paralelizar fácilmente mis cálculos?


# Uso de Spark en Python

El primer paso para utilizar Spark es conectarse a un clúster.

En la práctica, el clúster se alojará en una máquina remota que esté conectada a todos los demás nodos. Habrá un ordenador, llamado maestro, que gestionará la división de los datos y los cálculos. El maestro está conectado al resto de ordenadores del clúster, que se denominan trabajadores. El maestro envía a los trabajadores datos y cálculos para que los ejecuten, y éstos envían sus resultados al maestro.

Cuando estás empezando con Spark, es más sencillo ejecutar un clúster localmente.

Crear la conexión es tan sencillo como crear una instancia de la clase SparkContext. El constructor de la clase toma algunos argumentos opcionales que te permiten especificar los atributos del clúster al que te conectas.

Se puede crear un objeto que contenga todos estos atributos con el constructor SparkConf(). ¡Echa un vistazo a la documentación de para conocer todos los detalles!

Para el resto de este curso tendrás un SparkContext llamado sc ya disponible en tu espacio de trabajo



# Examen de SparkContext

```python 
# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)
```

# Uso de DataFrames


La estructura de datos principal de Spark es el *Conjunto de Datos Distribuidos Resilientes (RDD)*. Se trata de un objeto de bajo nivel que permite a Spark hacer su magia repartiendo los datos entre varios nodos del clúster. Sin embargo, es difícil trabajar directamente con los RDD, por lo que en este curso utilizarás la abstracción Spark DataFrame construida sobre los RDD.

El Spark DataFrame se diseñó para comportarse de forma muy parecida a una tabla SQL (una tabla con variables en las columnas y observaciones en las filas). No sólo son más fáciles de entender, los DataFrames también están más optimizados para operaciones complicadas que los RDD.

Cuando empiezas a modificar y combinar columnas y filas de datos, hay muchas formas de llegar al mismo resultado, pero algunas suelen llevar mucho más tiempo que otras. Cuando se utilizan RDDs,  *depende del científico de datos averiguar la forma correcta de optimizar la consulta*, ¡pero la implementación de DataFrame tiene gran parte de esta optimización incorporada!

Para empezar a trabajar con Spark DataFrames, primero tienes que crear un objeto SparkSession a partir de tu SparkContext. Puedes pensar en SparkContext como tu conexión con el clúster y en SparkSession como tu interfaz con esa conexión.


# Creación de SparkSession 


```python 
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
```

# Visualización de tablas

```python 
# Print the tables in the catalog
print(spark.catalog.listTables())
```

# ¿Algo que consultar?

```python 
# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()
```

# Pandafy en Spark DataFrame
```python 
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())
```