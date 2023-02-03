# BBDownEasyGui

Interfaz sencilla que facilita las descargas desde BiliBili.com, usando de intermediario la Herramienta BBDown (Mira su repo aquí https://github.com/nilaoda/BBDown)

Sin fines de lucro y solo para automatizar las descargas 👍

# Uso
Antes de empezar a usar la GUI, necesitas tener BBDown y FFmpeg, visita esta guia en donde detallo de mejor manera la instalación de estas dependencias:
https://docs.google.com/document/d/1XcQ9lzWzLcbDGTV6IsACja0arwLurvx_x1vhgBE9-Ng

Acá solo explicare el uso del GUI, visita los docs para instalar las otras dependencias.

Tener el .exe en la misma carpeta que BBDown.exe, procedemos a abrirlo:

![5](https://user-images.githubusercontent.com/106907367/216330714-397fdf8b-930c-4b52-a3a6-7251aee2059f.PNG)

Deberiamos ver algo como esto. Importante NO cerrar el CMD que se abre de fondo, por ahí veremos el progreso de descarga.

Seguido esto, lo que haremos será cargar nuestro ejecutable (que en este caso es el BBDown de la misma carpeta)

![1 1](https://user-images.githubusercontent.com/106907367/216331158-39e4b4a4-fd80-4ee3-b614-d0ee3df4abf6.PNG)

![1 2](https://user-images.githubusercontent.com/106907367/216331184-a570bb1f-e846-4d20-be60-38e4bc0cdb00.PNG)

Una vez que en la consola nos salga ".exe cargado!", será que el BBDown esta listo para ser ejecutado.

Ahora nos quedan los 2 parametros para agregar. En el primero vamos a introducir la ULR del video en cuestión.
* El formato de ingreso de la url es filtrando despues de "/video/". 
* Ejemplo: "https://www.bilibili.com/video/BV1TG4y1Q7Bw/?vd_source=25b47ea4aaceb21f75a622726184c4c8". De este link lo unico que nos interesa es "BV1TG4y1Q7Bw" para ingresar en la casilla de parametro 1.

![1 3](https://user-images.githubusercontent.com/106907367/216333062-c2db18a1-e2aa-4745-bde8-6eb3e191e353.PNG)

Y en el segundo parametro, tenemos que ingresar los comandos disponibles que tiene la herramienta.

![1 4](https://user-images.githubusercontent.com/106907367/216333465-5cbcc26f-2b22-445b-a095-b2ddddea6772.PNG)

* Para descargar en 1080p, solo necesitas agregar el -tv (Por eso a la derecha dejo un mensaje de "poner el -tv"), pero si podemos poner OTRO tipo de parametros. 
* Acá te dejo algunos de los que he testeado personalmente y me han funcionado de manera correcta (Se irá actualizando en la medida que descubra más BiliBili)

![screenshot-docs google com-2023 02 02-10_09_02](https://user-images.githubusercontent.com/106907367/216334054-97ec5edd-5789-4cd8-acdf-9cd6714dc66d.png)
 
 Gracias Snowy por recomendar el parametro de los subtitulos 🧡
 
 Una vez los 2 parametros listos solo faltaria en clickear el boton de "¡Descargar Video!"
 
 Si seguiste al pie de la letra todo, deberías estar viendo algo como esto:
 
![6](https://user-images.githubusercontent.com/106907367/216335183-439faebc-c2ad-4a2e-ba19-bd532edbe2ab.PNG)

Uan vez que dejen de salir caracteres un poco raros, puedes volver a la carpeta donde dejaste los .exe y pum! Debería estar el video en 1080p 👍

![7](https://user-images.githubusercontent.com/106907367/216335577-991db13b-143d-4679-93f5-e1d36caf0ed7.PNG)

* Lo mas probable si bajaste un archivo MUY grande, es que este se demore en aparecer en formato mp4 y en su caso tendrás una carpeta con archivos sueltos. Solo tienes que esperar un tiempo (Dependiendo de tu PC) para que aparezca el archivo .MP4 con todo. (Ty Zhika por el aviso).

# Erorres y Actualizaciones

* Tratare de mantener actualizada la guia tanto esta y como la del DOCS (que esta ultima está más detallada, visitenla)
* Puede que sufras o sientas como se lagea el pc despues de hacer una descarga muy grande (+ 1GB), es normal ya que se está haciendo el post procesado por atrás.

* En caso de errores con la interfaz u otras dudas o sugerencias, me puedes contactar vía discord: Jaruna#2496

No soy programador, pero estare aceptando feedbacks y trabajando para mejorar 👍





