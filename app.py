import flet as ft
import openai, sys, json, os


# key provider
def keyProvider():
    try:
        key = "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"
        openai.api_key = key
        return key
    except KeyError:
        sys.stderr.write("""
        We have a problem...
        """)
        exit(1)

#ImageGenerator
def imageGenerator(req,e=0):
    temp_key = keyProvider()
    try:
        con = 1
        todos = req
        response = openai.Image.create(
                prompt=todos,
                n=1,
                # size="1024x1024"
            )
        image_url = response['data'][0]['url']
        return image_url
    except:
        print("problem...")





#Chatbot------------------------
def chatbot(peticion, e=0):
    # key
    temp_key = keyProvider()
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": peticion}
    ]
)
    respuesta = response["choices"][0]["message"]["content"]
    return respuesta


#Clase generadora de interface

# Definición de la clase imageApp que hereda de ft.UserControl
class imageApp(ft.UserControl):
    
    # Método que construye la aplicación
    def build(self):
        # Crear un cuadro de texto para ingresar solicitudes
        self.new_request = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        # Crear una columna para mostrar las solicitudes y las imágenes generadas
        self.request = ft.Column()

        # Devolver una columna que contiene todos los controles necesarios para la aplicación
        return ft.Column(
            width=600,
            controls=[
                # Crear una fila que contiene el cuadro de texto y el botón para enviar solicitudes
                ft.Row(
                    controls=[
                        self.new_request,
                        ft.FloatingActionButton("Send", on_click=self.add_rq),
                    ],
                ),
                # Agregar la columna para mostrar las solicitudes y las imágenes generadas
                self.request,
            ],
        )

    # Método que se llama cuando se agrega una nueva solicitud
    def add_rq(self, e):
        # Crear un nuevo control de texto con la solicitud ingresada por el usuario
        # y agregarlo a la columna de solicitudes
        texto1 = ""
        texto = "You: \n", self.new_request.value
        for i in texto:
            texto1 += i
        self.request.controls.append(ft.Text(texto1))
        
        # Generar una imagen a partir de la solicitud ingresada por el usuario
        imagen_generada = imageGenerator(self.new_request.value)
        
        # Crear un nuevo control de texto con el nombre del generador de imágenes (PixelAi)
        # y un nuevo control de imagen con la imagen generada, y agregar ambos a la columna de solicitudes
        texto = ft.Text("PixelAi: "), ft.Image(src=f"{imagen_generada}",width=600)
        for i in texto:
            self.request.controls.append(i)
        
        # Limpiar el cuadro de texto para ingresar nuevas solicitudes
        self.new_request.value = ""
        # Actualizar la aplicación para mostrar las nuevas solicitudes y las imágenes generadas
        self.update()



# Definición de la clase TodoApp que hereda de ft.UserControl
class TodoApp(ft.UserControl):
    
    # Método que construye la aplicación
    def build(self):
        # Crear un cuadro de texto para ingresar nuevas tareas
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        # Crear una columna para mostrar las tareas agregadas
        self.tasks = ft.Column()

        # Devolver una columna que contiene todos los controles necesarios para la aplicación
        return ft.Column(
            width=600,
            controls=[
                # Crear una fila que contiene el cuadro de texto y el botón para agregar tareas
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton("Send", on_click=self.add_request),
                    ],
                ),
                # Agregar la columna para mostrar las tareas
                self.tasks,
            ],
        )

    # Método que se llama cuando se agrega una nueva tarea
    def add_request(self, e):
        # Crear un nuevo control de texto con la tarea ingresada por el usuario
        # y agregarlo a la columna de tareas
        texto1 = ""
        texto = "You: \n", self.new_task.value
        for i in texto:
            texto1 += i
        self.tasks.controls.append(ft.Text(texto1))
        
        # Crear un nuevo control de texto con la respuesta del ChatBot a la tarea ingresada
        # y agregarlo a la columna de tareas
        texto = "ChatBot: ", chatbot(self.new_task.value)
        texto1 = ""
        for i in texto:
            texto1 += i
        self.tasks.controls.append(ft.Text(texto1))
        
        # Limpiar el cuadro de texto para ingresar nuevas tareas
        self.new_task.value = ""
        # Actualizar la aplicación para mostrar las nuevas tareas agregadas
        self.update()


#main
def main(page: ft.Page):
    page.title = "Chatbot with API of chatgpt"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    lv = ft.ListView(auto_scroll=True)


    # create application instance
    todo = TodoApp()
    image=imageApp()

    # election1=election

    def chatBot(e):
        page.dialog.open = False
        page.remove(todo)
        lv.controls.append(todo)
        page.add(lv)
        page.update()
    
    def imageBot(e):
        page.dialog.open = False
        page.remove(todo)
        lv.controls.append(image)
        page.add(lv)
        page.update()



    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        actions=[ft.ElevatedButton(text="Join chat with the chatbot", on_click=chatBot),
                 ft.ElevatedButton(text="Join chat with the image generator", on_click=imageBot)],
                actions_alignment="end"
    )

    page.add(todo)


ft.app(target=main,assets_dir="assets")
