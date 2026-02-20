# Creación de Entornos Virtuales y Configuración de FastAPI

Resumen
Para trabajar con un framework en Python como FastAPI, siempre es recomendable emplear entornos virtuales. Estos entornos permiten gestionar las dependencias de un proyecto sin interferir con otros. A continuación, se explican los pasos clave para crear y configurar un entorno virtual y desarrollar una primera API básica.

¿Cómo crear un entorno virtual para FastAPI?

Crear el entorno virtual:

Abre la terminal y navega a la carpeta donde se encuentra tu proyecto. Utiliza el módulo venv de Python para crear un entorno virtual:
python -m venv vm
Esto generará un entorno virtual en una carpeta llamada vm dentro de tu proyecto.
Activar el entorno virtual:

En sistemas Unix, ejecuta el siguiente comando:
source vm/bin/activate
Esto permite aislar las dependencias de tu proyecto dentro del entorno virtual.
¿Cómo instalar FastAPI y sus dependencias?

Instalar FastAPI:

Con el entorno virtual activo, instala FastAPI:
pip install "fastapi[standard]"
Si recibes errores de interpretación, agrega comillas dobles para evitar problemas con las llaves {} que incluyen dependencias adicionales para la ejecución de FastAPI en entornos locales.
Verificar las dependencias instaladas:

Tras la instalación, puedes listar las dependencias para observar los paquetes añadidos, como Jinja (templates), Markdown (manejo de texto) y Uvicorn (para ejecutar aplicaciones como servidor web).
¿Cómo crear un primer endpoint con FastAPI?

Configurar la estructura de archivos:

Crea una carpeta para el proyecto:
mkdir curso_fastapi_project
Dentro de esta carpeta, crea un archivo main.py para definir el primer endpoint.
Desarrollar la API en main.py:

Abre el archivo en tu editor y añade el siguiente código básico:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
return {"mensaje": "Hola, Mundo"}
La función root define un endpoint básico que devuelve un mensaje JSON. Utiliza el decorador @app.get("/") para indicar que este endpoint responde a solicitudes GET en la ruta raíz (/).
¿Cómo ejecutar y probar la API en desarrollo?

Iniciar el servidor:

Usa Uvicorn para ejecutar la aplicación:
uvicorn main:app --reload
El parámetro --reload activa el modo de desarrollo, permitiendo recargar la API automáticamente cada vez que guardes cambios en el código.
Verificar en la terminal:

Al ejecutar, Uvicorn muestra la URL de acceso a la API y la documentación generada automáticamente en /docs. Puedes acceder a la API en http://localhost:8000 y la documentación en http://localhost:8000/docs.
