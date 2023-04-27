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

class imageApp(ft.UserControl):
    def build(self):
        self.new_request = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.request = ft.Column()

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_request,
                        ft.FloatingActionButton("Send", on_click=self.add_rq),
                    ],
                ),
                self.request,
            ],
        )

    def add_rq(self, e):
        # self.tasks.controls.append(ft.Checkbox(label=self.new_task.value))
        texto1 = ""
        texto = "You: \n", self.new_request.value
        for i in texto:
            texto1 += i
        self.request.controls.append(ft.Text(texto1))
        print(self.new_request.value)
        texto = ft.Text("PixelAi: "), ft.Image(src=f"{imageGenerator(self.new_request.value)}",width=600)
        texto1 = ""
        for i in texto:
            self.request.controls.append(i)
        self.new_request.value = ""
        self.update()


#clase generadoras de chatbot interface
class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = ft.Column()

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton("Send", on_click=self.add_request),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_request(self, e):
        # self.tasks.controls.append(ft.Checkbox(label=self.new_task.value))
        texto1 = ""
        texto = "You: \n", self.new_task.value
        for i in texto:
            texto1 += i
        self.tasks.controls.append(ft.Text(texto1))
        texto = "ChatBot: ", chatbot(self.new_task.value)
        texto1 = ""
        for i in texto:
            texto1 += i
        self.tasks.controls.append(ft.Text(texto1))
        self.new_task.value = ""
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
