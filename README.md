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




