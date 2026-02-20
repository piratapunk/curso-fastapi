# Crear un Endpoint Dinámico con FastAPI para Obtener Hora por País y Formato

Resumen
Crear un endpoint en FastAPI que devuelva la hora en función del país permite ofrecer una API flexible y personalizable. A continuación, exploramos cómo construir esta funcionalidad con un endpoint dinámico y cómo incluir parámetros adicionales para definir el formato de la hora.

¿Cómo crear un endpoint que devuelva la hora del servidor?

Función inicial para la hora del servidor
En el archivo de sincronización (sync), creamos una función llamada time que retorne la hora actual del servidor. Para ello:

Importamos el módulo datetime desde la librería de Python.
En la función, utilizamos datetime.now() para obtener la hora actual.
Configurar la función como endpoint
Para que el endpoint sea accesible, decoramos la función con @app.get("/time"). Este decorador registra el endpoint para que esté disponible en la URL /time.

¿Cómo agregar variables en un endpoint?

Un endpoint estático es poco común en aplicaciones que requieren personalización. FastAPI permite recibir variables directamente en la URL, por lo que podemos modificar el endpoint para que acepte un código de país y devuelva la hora correspondiente en ese huso horario.

Añadir el código ISO del país
Modificamos el endpoint y añadimos un parámetro en la URL. Por ejemplo: @app.get("/time/{iso_code}"). Así, cuando el usuario indique el código de país, el sistema sabrá de qué huso horario obtener la hora.

Tipar la variable
Es esencial declarar el tipo de dato del parámetro iso_code. Al indicar iso_code: str, ayudamos a que FastAPI maneje correctamente el dato, garantizando que se trate de un texto. Esto también permite acceder a métodos específicos de cadenas de texto en Python, como .upper().

¿Cómo ajustar el formato de entrada del parámetro?

Para mejorar la usabilidad:

Convertimos iso_code a mayúsculas (iso_code.upper()). Así, la entrada será uniforme sin importar cómo el usuario ingrese el código.

Definimos un diccionario que contiene los husos horarios por país, en el que las claves están en mayúsculas. Esto asegura que, al consultar el diccionario, se encuentre el huso horario correcto.

¿Cómo devolver la hora en el huso horario del país?

Obtener el huso horario
Con el código ISO del país, utilizamos timezone.get(iso_code) para obtener la zona horaria correspondiente.

Formatear la hora según el huso horario
Importamos el módulo zoneinfo y configuramos la zona horaria del resultado. De este modo, al retornar datetime.now(tz=timezone), se muestra la hora correspondiente al país especificado.

¿Cómo agregar parámetros opcionales para formato de hora?

Finalmente, para que el usuario pueda decidir el formato de hora:

Añadimos un parámetro opcional (format_24) que indique si se desea la hora en formato de 24 horas.
En la lógica de la función, verificamos el parámetro y ajustamos el formato de salida para que muestre la hora en el formato deseado.
