import tkinter as tk
import subprocess
import os
import webbrowser

def read_text(selected_exe):
    global url
    selected = var.get()
    if selected == "Select":
        return
    url = selected
    print("Executable loaded!", url)
    entry_exe.delete(0, tk.END)
    entry_exe.insert(0, url)
    label_loaded.config(text="Successfully loaded: {}".format(url))

def run_exe():
    if os.path.exists(url):
        subprocess.Popen([url, entry_param1.get(), entry_param2.get()])
    else:
        print("File does not exist in the current folder")

def open_docs_us():
    webbrowser.open_new("https://docs.google.com/document/d/1H-UZlhf1KnoLo1C0FrkkUy3B1jNyVCgHoErziogNJ84/")

def open_docs_es():
    webbrowser.open_new("https://docs.google.com/document/d/1XcQ9lzWzLcbDGTV6IsACja0arwLurvx_x1vhgBE9-Ng")

root = tk.Tk()
root.title("BBDownEasyGUI")
root.resizable(False, False)
root.geometry("465x255")
root.config(bg="#cccccc")

executables = ['Select', 'BBDown.exe']

label_exe = tk.Label(root, text="Executable:", bg="#cccccc")
label_exe.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
entry_exe = tk.Entry(root)
entry_exe.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

var = tk.StringVar(root)
var.set(executables[0])

dropdown = tk.OptionMenu(root, var, *executables, command=lambda x: read_text(x))
dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label_loaded = tk.Label(root, text="", bg="#cccccc")
label_loaded.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label_param1 = tk.Label(root, text="Parameter 1:", bg="#cccccc")
label_param1.grid(row=3, column=0, padx=10, pady=10, sticky="E")
entry_param1 = tk.Entry(root)
entry_param1.grid(row=3, column=1, padx=10, pady=10, sticky="W")

label_text = tk.Label(root, text="Enter the parameter (Visit DOCS)", height=1, width=29)
label_text.grid(row=3, column=2, rowspan=3, padx=10, pady=10)

label_param2 = tk.Label(root, text="Parameter 2:", bg="#cccccc")
label_param2.grid(row=4, column=0, padx=10, pady=10, sticky="E")
entry_param2 = tk.Entry(root)
entry_param2.grid(row=4, column=1, padx=10, pady=10, sticky="W")

label_text2 = tk.Label(root, text="Enter the url of the video", height=1, width=29)
label_text2.grid(row=3, column=2, rowspan=1, padx=10, pady=10)

btn_run = tk.Button(root, text="¡Download the video!", command=run_exe, bg="#cccccc")
btn_run.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

btn_open_docs_us = tk.Button(root, text="Docs-US", command=open_docs_us, bg="#cccccc", height=1, width=8)
btn_open_docs_us.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

btn_open_docs_es = tk.Button(root, text="Docs-ES", command=open_docs_es, bg="#cccccc", height=1, width=8)
btn_open_docs_es.grid(row=5, column=2, columnspan=3, padx=10, pady=10)

label_text3 = tk.Label(root, text="𝐽𝑎𝑟𝑢𝑛𝑎", bg="#cccccc", height=1, width=9)
label_text3.grid(row=5, column=2, columnspan=3, padx=0, pady=10, sticky="E")

root.mainloop()


