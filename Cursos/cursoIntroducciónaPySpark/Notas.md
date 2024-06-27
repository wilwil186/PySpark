#  ¿Qué es PySpark?

PySpark es una interfaz para Apache Spark en Python. Con PySpark, puedes escribir comandos tipo Python y SQL para manipular y analizar datos en un entorno de procesamiento distribuido.

Apache Spark es un sistema de procesamiento distribuido que se utiliza para realizar tareas de big data y machine learning en grandes conjuntos de datos.

# Cómo instalar PySpark

Antes de instalar Apache Spark y PySpark, debes tener configurado el siguiente software en tu dispositivo:

* Python 
* Java

## Jupyter Notebook

Jupyter Notebook es una aplicación web que puedes utilizar para escribir código y mostrar ecuaciones, visualizaciones y texto.

### Instalar JupyterLab en Debian 12 usando un entorno virtual
En mi computadora se vio necesario hacer el siguiente comando: 

```bash
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```

Es para evitar que el Python no deje instalar por medio de pip.  La razón detrás de eso es que los módulos de Python que se instalan de manera global en todo el sistema pueden interferir con el administrador de paquetes como APT

    1. Crea un entorno virtual de Python usando el módulo venv:

    ```bash
    python3 -m venv /path/to/venv
    ```
    2. Activa el entorno virtual:

    ```bash
    source /path/to/venv/bin/activate
    ```

    3. Una vez activado el entorno, instala JupyterLab usando pip:
    ```bash
    pip install jupyterlab
    ```

    4. Iniciar JupyterLab

    ```bash
    jupyter-lab
    ```

    5. Cuando hayas terminado de trabajar con JupyterLab, puedes desactivar el entorno virtual con el comando 
    ```bash
    deactivate
    ```   
    6. Crear un alias
    ```bash
    vim ~/.bashrc
    ```   
    ```bash
    alias activate='source /path/to/venv/bin/activate'
    ```
    

    
    
