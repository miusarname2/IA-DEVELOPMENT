<img src="https://img.shields.io/badge/Current%20Version-V0.1.0-green" alt="Descripción de la imagen">

# 🤖 CreativAI 🤖

## Español
### 🧐 Contexto
Durante el trayecto de la creación de los proyectos para " mostrar " con MVP se desarrollo una AI que "decidimos" llamar Creativa AI o "CreativAI"
### ¿Como descargar?
Puedes ir a la "sección" de realeses y descargar dependiendo de tu sistema operativo(solo disponible para Windows y/o Linux)
#### ¿Y si no tengo ni Windows ni linux? 😲
Solo descarga el codigo y en la primera seccion más especificamente aca:

```
def keyProvider():
    try:
        key = "YOUR_APIKEY"
        openai.api_key = key
        return key
    except KeyError:
        sys.stderr.write("""
        We have a problem...
        """)
        exit(1)
```

y ponemos tu clave de API en la parte en la que dice "YOUR_APIKEY" y lo reemplazas por tu codigo de API por poner ejemplo:


```
def keyProvider():
    try:
        key = "sk-123456789abcdefghjilamni"
        openai.api_key = key
        return key
    except KeyError:
        sys.stderr.write("""
        We have a problem...
        """)
        exit(1)
```

y luego abres una terminal y ejecutas:


```
pip install openai

```

y luego


```
pip install flet

```

para despues 

```

pip install pyinstall

```

y una vez tengas todo lo necesario puedes "compilar" tu app, y si todo sale bien debes poner en la terminal


```

flet pack app.py

```
y esto generara un una carpeta dist en esta estara el ejecutable

### Documentacion extra

Introducción
Esta aplicación implementa un chatbot y un generador de imágenes a partir de texto utilizando la API de OpenAI y la librería flet.

Requerimientos
Antes de utilizar esta aplicación se deben instalar los siguientes paquetes en Python:

openai
flet
Además, se debe contar con una clave de API de OpenAI para poder utilizar los servicios de la API. La clave de API debe ser almacenada en la variable key en el archivo app.py.

Uso
La aplicación cuenta con dos interfaces: una para generar imágenes a partir de texto y otra para utilizar el chatbot.

ImageGenerator
Para utilizar la interfaz del generador de imágenes se debe ejecutar el siguiente código:

scss
Copy code
from app import imageApp

app = imageApp()
app.show()
Una vez iniciada la aplicación, se debe ingresar una solicitud en el cuadro de texto y presionar el botón "Send". La aplicación generará una imagen a partir de la solicitud ingresada y la mostrará en la columna de solicitudes.

ChatBot
Para utilizar la interfaz del chatbot se debe ejecutar el siguiente código:

scss
Copy code
from app import TodoApp

app = TodoApp()
app.show()
Una vez iniciada la aplicación, se debe ingresar una tarea en el cuadro de texto y presionar el botón "Send". La aplicación utilizará el chatbot de OpenAI para generar una respuesta a la tarea ingresada y la mostrará en la columna de tareas.



