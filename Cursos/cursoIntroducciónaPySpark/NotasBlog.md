# Guía para Instalar y Utilizar PySpark en Debian 12: Procesamiento de Datos y Machine Learning

PySpark es la interfaz de Python para Apache Spark, un potente motor de procesamiento distribuido que permite analizar grandes volúmenes de datos de manera eficiente. Esta guía te llevará paso a paso por la instalación y configuración de PySpark en Debian 12, junto con ejemplos de su uso en tareas de Machine Learning.

## ¿Qué es PySpark?

PySpark es una interfaz para Apache Spark en Python. Con PySpark, puedes escribir comandos tipo Python y SQL para manipular y analizar datos en un entorno de procesamiento distribuido.

Apache Spark es un sistema de procesamiento distribuido que se utiliza para realizar tareas de big data y machine learning en grandes conjuntos de datos.

## ¿Por qué PySpark?

* **Escalabilidad:** Procesa grandes volúmenes de datos que no caben en la memoria de una sola máquina.
* **Velocidad:** Ejecuta operaciones en paralelo en un clúster de máquinas, acelerando el análisis.
* **Facilidad de uso:** Proporciona una API familiar en Python para trabajar con datos distribuidos.
* **Machine Learning:** Incluye bibliotecas como MLlib para tareas de aprendizaje automático a gran escala.

## Cómo instalar PySpark

### Requisitos Previos

* **Python 3:** Asegúrate de tener Python 3 instalado en tu sistema Debian. Puedes verificar la versión con `python3 --version`.
* **Java:** PySpark requiere Java. Puedes instalarlo con `sudo apt install default-jdk`.

### Jupyter Notebook (Opcional):

Jupyter Notebook es una aplicación web que puedes utilizar para escribir código y mostrar ecuaciones, visualizaciones y texto.

Antes de hacer cualquier cosa, ejecuta el siguiente comando para poder instalar paquetes con pip:

```bash
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```

Esto es para evitar que Python no permita instalar con pip. La razón detrás de esto es que los módulos de Python que se instalan de manera global en todo el sistema pueden interferir con el administrador de paquetes APT.

1. Crea un entorno virtual de Python: `python3 -m venv /ruta/al/entorno/virtual` 
2. Activa el entorno virtual: `source /ruta/al/entorno/virtual/bin/activate`
3. Instala JupyterLab: `pip install jupyterlab`
4. Inicia JupyterLab: `jupyter-lab`
5. Cuando hayas terminado de trabajar con JupyterLab, puedes desactivar el entorno virtual con el comando `deactivate`
6. (Opcional) Crea un alias para activar el entorno virtual:
   ```bash
   echo "alias activate='source /ruta/al/entorno/virtual/bin/activate'" >> ~/.bashrc
   source ~/.bashrc
   ```

### Instalación de Apache Spark

En el entorno virtual que creaste, ejecuta:

```bash
pip install pyspark
```

## Machine Learning con PySpark

Vamos a crear un modelo de K-medias con los datos [https://www.kaggle.com/datasets/vijayuv/onlineretail?resource=download](https://www.kaggle.com/datasets/vijayuv/onlineretail?resource=download) para aprender mejor como se usa la libreria PySpark: 

El siguiente paso es cambiar su nombre por datacamp_ecommerce esto unicamente para seguir el tutorial de la pagina [https://www.datacamp.com/es/tutorial/pyspark-tutorial-getting-started-with-pyspark](https://www.datacamp.com/es/tutorial/pyspark-tutorial-getting-started-with-pyspark)

*Para seguir este proyecto consultar el archivo ML.ipynb de esta misma carpeta*

