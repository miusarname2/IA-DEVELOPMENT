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

#### Introducción
Esta aplicación implementa un chatbot y un generador de imágenes a partir de texto utilizando la API de OpenAI y la librería flet.

#### Requerimientos
Antes de utilizar esta aplicación se deben instalar los siguientes paquetes en Python:

##### openai
##### flet
Además, se debe contar con una clave de API de OpenAI para poder utilizar los servicios de la API. La clave de API debe ser almacenada en la variable key en el archivo app.py.

#### Uso
La aplicación cuenta con dos interfaces: una para generar imágenes a partir de texto y otra para utilizar el chatbot.

#### ImageGenerator
Para utilizar la interfaz del generador de imágenes se debe ejecutar el siguiente código:

```
from app import imageApp

app = imageApp()
app.show()
```

Una vez iniciada la aplicación, se debe ingresar una solicitud en el cuadro de texto y presionar el botón "Send". La aplicación generará una imagen a partir de la solicitud ingresada y la mostrará en la columna de solicitudes.

#### ChatBot
Para utilizar la interfaz del chatbot se debe ejecutar el siguiente código:

```
from app import TodoApp


app = TodoApp()
app.show()
```

Una vez iniciada la aplicación, se debe ingresar una tarea en el cuadro de texto y presionar el botón "Send". La aplicación utilizará el chatbot de OpenAI para generar una respuesta a la tarea ingresada y la mostrará en la columna de tareas.

## English
### 🧐 Context
During the journey of the creation of the projects to "show" with MVP an AI was developed that we "decided" to call Creative AI or "CreativAI"
### How to download?
You can go to the realeses "section" and download depending on your operating system (only available for Windows and/or Linux)
#### What if I don't have Windows or Linux? 😲
Just download the code and in the first section more specifically here:

```
def keyProvider():
     try:
         key="YOUR_APIKEY"
         openai.api_key = key
         return key
     except KeyError:
         sys.stderr.write("""
         We have a problem...
         """)
         exit(1)
```

and we put your API key in the part where it says "YOUR_APIKEY" and replace it with your API code for example:


```
def keyProvider():
     try:
         key="sk-123456789abcdefghjilamni"
         openai.api_key = key
         return key
     except KeyError:
         sys.stderr.write("""
         We have a problem...
         """)
         exit(1)
```

and then open a terminal and run:


```
pip install openai

```

and then


```
pip install freight

```

for later

```

pip install pyinstall

```

and once you have everything you need you can "compile" your app, and if everything goes well you must put in the terminal


```

flet pack app.py

```
and this will generate a dist folder in this will be the executable

### Additional documentation

#### Introduction
This application implements a chatbot and an image generator from text using the OpenAI API and the flet library.

#### Requirements
Before using this application the following Python packages must be installed:

##### openai
##### freight
In addition, you must have an OpenAI API key in order to use the API services. The API key must be stored in the key variable in the app.py file.

#### Use
The application has two interfaces: one to generate images from text and another to use the chatbot.

#### ImageGenerator
To use the image generator interface, the following code must be executed:

```
from app import imageApp

app = imageApp()
app.show()
```

Once the application is launched, a request must be entered in the text box and the "Send" button pressed. The app will generate an image from the entered request and display it in the requests column.

#### ChatBot
To use the chatbot interface, the following code must be executed:

from app import TodoApp

```
app = AllApp()
app.show()
```

Once the application is started, a task must be entered in the text box and the "Send" button pressed. The app will use the OpenAI chatbot to generate a response to the entered task and display it in the task column.

# 日本

### 🧐 コンテキスト
MVP で「見せる」ためのプロジェクト作成の旅の中で、Creative AI または「CreativAI」と呼ぶことに「決定」した AI が開発されました。
＃＃＃ ダウンロードする方法？
お使いのオペレーティング システムに応じて、realeses の「セクション」に移動してダウンロードできます (Windows および/または Linux でのみ利用可能)。
#### Windows または Linux を使用していない場合はどうすればよいですか? 😲
コードをダウンロードするだけで、最初のセクションでより具体的には次のようになります。

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


そして、「YOUR_APIKEY」と書かれている部分に API キーを配置し、API コードに置き換えます。例:


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

次に、ターミナルを開いて実行します。


```
pip install openai

```

その後


```
pip install flet

```

後で

```

flet pack app.py

```

必要なものがすべて揃ったら、アプリを「コンパイル」できます。すべてがうまくいけば、ターミナルに配置する必要があります


```

fletpack app.py

```
これによりdistフォルダーが生成され、これが実行可能ファイルになります

### 追加のドキュメント

#### 序章
このアプリケーションは、OpenAI API と flet ライブラリを使用して、テキストからチャットボットと画像ジェネレーターを実装します。

#### 要件
このアプリケーションを使用する前に、次の Python パッケージをインストールする必要があります。

##### 開けない
##### 貨物
さらに、API サービスを使用するには、OpenAI API キーが必要です。 API キーは、app.py ファイルのキー変数に格納する必要があります。

＃＃＃＃ 使用
アプリケーションには 2 つのインターフェイスがあります。1 つはテキストから画像を生成するためのもので、もう 1 つはチャットボットを使用するためのものです。

#### イメージジェネレーター
イメージ ジェネレーター インターフェイスを使用するには、次のコードを実行する必要があります。

```
from app import imageApp

app = imageApp()
app.show()
```

アプリケーションが起動したら、テキスト ボックスにリクエストを入力し、[送信] ボタンを押す必要があります。 アプリは、入力されたリクエストから画像を生成し、リクエスト列に表示します。

#### チャットボット
チャットボット インターフェイスを使用するには、次のコードを実行する必要があります。


```
from app import TodoApp


app = TodoApp()
app.show()
```

アプリケーションが起動したら、タスクをテキスト ボックスに入力し、[送信] ボタンを押す必要があります。 アプリは OpenAI チャットボットを使用して、入力されたタスクへの応答を生成し、タスク列に表示します。

