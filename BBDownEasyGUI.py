import tkinter as tk
import subprocess
import os
import webbrowser

def read_text(selected_exe):
    global url
    selected = var.get()
    if selected == "Seleccione":
        return
    url = selected
    print(".exe cargado!:", url)
    entry_exe.delete(0, tk.END)
    entry_exe.insert(0, url)
    label_loaded.config(text="Cargado correctamente: {}".format(url))

def run_exe():
    if os.path.exists(url):
        subprocess.Popen([url, entry_param1.get(), entry_param2.get()])
    else:
        print("El archivo no existe en la carpeta actual")

def open_docs():
    webbrowser.open_new("https://docs.google.com/document/d/1XcQ9lzWzLcbDGTV6IsACja0arwLurvx_x1vhgBE9-Ng/")

root = tk.Tk()
root.title("BBDownEasyGUI")
root.geometry("505x255")
root.config(bg="#cccccc")

executables = ['Seleccione', 'BBDown.exe']

label_exe = tk.Label(root, text="Ejecutable:", bg="#cccccc")
label_exe.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
entry_exe = tk.Entry(root)
entry_exe.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

var = tk.StringVar(root)
var.set(executables[0])

dropdown = tk.OptionMenu(root, var, *executables, command=lambda x: read_text(x))
dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label_loaded = tk.Label(root, text="", bg="#cccccc")
label_loaded.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label_param1 = tk.Label(root, text="Parámetro 1:", bg="#cccccc")
label_param1.grid(row=3, column=0, padx=10, pady=10, sticky="E")
entry_param1 = tk.Entry(root)
entry_param1.grid(row=3, column=1, padx=10, pady=10, sticky="W")

label_text = tk.Label(root, text="Ingresa -tv", height=1, width=35)
label_text.grid(row=3, column=2, rowspan=3, padx=10, pady=10)

label_param2 = tk.Label(root, text="Parámetro 2:", bg="#cccccc")
label_param2.grid(row=4, column=0, padx=10, pady=10, sticky="E")
entry_param2 = tk.Entry(root)
entry_param2.grid(row=4, column=1, padx=10, pady=10, sticky="W")

label_text2 = tk.Label(root, text="Ingresa la url del video", height=1, width=35)
label_text2.grid(row=3, column=2, rowspan=1, padx=10, pady=10)

btn_run = tk.Button(root, text="Descargar el video!", command=run_exe, bg="#cccccc")
btn_run.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

btn_open_docs = tk.Button(root, text="Docs", command=open_docs, bg="#cccccc", height=1, width=6)
btn_open_docs.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="E")

label_text3 = tk.Label(root, text="𝑏𝑦 𝐽𝑎𝑟𝑢𝑛𝑎 𝑤𝑖𝑡𝘩 🧡", bg="#cccccc", height=1, width=13)
label_text3.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

root.mainloop()


