# Proyecto de Análisis de Préstamos

Este proyecto incluye scripts de Python para limpiar datos de préstamos, realizar un análisis básico usando consultas SQL en memoria (SQLite) y generar documentación sobre el modelo de datos (Modelo Estrella) y el pipeline propuesto en AWS.

## 📁 Estructura del Proyecto

* /src -> Contiene el script principal de Python (main.py).

* /data -> Debe contener los archivos CSV originales (loans.csv, branches.csv) y almacenará el archivo limpio (loans_clean.csv) después de la ejecución.

* /sql -> Contiene el código SQL de ejemplo (consulta.sql).

* /docs -> Contiene la documentación del proyecto (modelo.md, pipeline_aws.md).

* requirements.txt -> Lista de librerías necesarias.

* README.md -> Este archivo.

## ⚙️ Requisitos

Asegúrate de tener instalado:

* **Python 3.x** ## 💻 Ejecución Local (Recomendado)

Sigue estos pasos para configurar y ejecutar el proyecto localmente usando un entorno virtual:

### 1. Crear y Activar el Entorno Virtual

El uso de un entorno virtual (venv) es altamente recomendado para aislar las dependencias del proyecto.

```

# Crear el entorno virtual llamado 'venv'

python -m venv venv

# Activar el entorno virtual (Linux/macOS)

source venv/bin/activate

# Activar el entorno virtual (Windows)

# Si estás en PowerShell:

# .\\venv\\Scripts\\Activate.ps1

# Si estás en CMD:

# venv\\Scripts\\activate.bat

```

### 2. Instalar Dependencias

Con el entorno virtual activado, instala las librerías necesarias listadas en requirements.txt:

```

pip install -r requirements.txt

```

### 3. Estructura de Datos

Asegúrate de que tus archivos de datos originales (loans.csv y branches.csv) se encuentren dentro de la carpeta /data.

### 4. Ejecutar el Script Principal

Ejecuta el script de Python:

```

python src/main.py

```

El script realizará la limpieza, ejecutará la consulta SQL e imprimirá el resultado en la consola. Además, generará los archivos limpios y de documentación en las carpetas correspondientes.

## ☁️ Ejecución en Google Colab

Si deseas ejecutar el código en Google Colab, debes seguir un proceso diferente para manejar los archivos:

1. **Cargar el código Python**: Copia el contenido de src/main.py en una celda de código en Colab.

2. **Subir la carpeta `data`**: Debes crear y subir la carpeta completa `data` (incluyendo `loans.csv` y `branches.csv`) al sistema de archivos de Colab para que el script pueda acceder a las rutas (`data/loans.csv`, etc.).

3. **Instalar dependencias**: Ejecuta la instalación de `pandas` en una celda separada:

```

\!pip install pandas

```

4. **Ejecutar**: Ejecuta la celda que contiene el código de `main.py`.

> **Nota:** La función `print()` en Python es el reemplazo de `display()` en Colab si el código se importa a un entorno estándar de script.

---

## 📊 Resultados y Evidencia

Aquí se muestra la evidencia de la limpieza de datos (Actividad A) y el resultado de la consulta SQL agrupada por zona (Actividad B).

---

### A) Préstamos Limpios (`loans_clean.csv`)

Se puede observar la columna calculada **`total_payable`** y que no existen préstamos con `amount <= 0` (el préstamo 3 del ejemplo fue eliminado).

<img src="https://github.com/fcerronfernandez-afk/enigma-challenge/blob/master/public/loan_clean.png?raw=true" alt="Vista de los datos de préstamos limpios" />

---

### B) Total Prestado por Zona (Consulta SQL)

Resultado de la agregación de **`amount`** después de unir los préstamos limpios con la información de las sucursales (`zone`).

<img src="https://github.com/fcerronfernandez-afk/enigma-challenge/blob/master/public/query_result.png?raw=true" alt="Resultado de la consulta SQL por zona" />