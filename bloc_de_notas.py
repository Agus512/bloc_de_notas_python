import tkinter as tk
from tkinter import filedialog

#Funciones call back


#Funciones archivo
def nuevo_archivo():
    area_de_texto.delete(1.0,tk.END)


def abrir_archivo():
    global ruta_archivo
    ruta_archivo= filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Archivos de textos", "*.txt"),("Archivos de python", "*.py"),("Todos los archivos","*.*")])

    area_de_texto.delete(1.0, tk.END)
    with open(ruta_archivo,"r", encoding="utf-8") as file:
        area_de_texto.insert(tk.INSERT, file.read())
    print(ruta_archivo)

def guardar_archivo():
    global ruta_archivo
    if ruta_archivo:
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as file:
                file.write(area_de_texto.get(1.0, tk.END))
        except:
            print("No se puede guardar el archivo")

def guardar_como():
    nueva_ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de textos", "*.txt"),("Archivos de python", "*.py"),("Todos los archivos","*.*")])

    if nueva_ruta:
        with open(nueva_ruta, "w", encoding="utf-8") as file:
            file.write(area_de_texto.get(1.0, tk.END))

    print(nueva_ruta)



#Funciones edicion

def copiar():
    area_de_texto.event_generate(("<<Copy>>"))

def pegar():
    area_de_texto.event_generate(("<<Paste>>"))

def cortar():
    area_de_texto.event_generate(("<<Cut>>"))


def dev():
    pass


#........FIN FUNCIONES.............

#Creamos parte grafica con tkinter
ventana = tk.Tk()
ventana.title("Bloc de notas")
ventana.geometry("800x600")

ruta_archivo=("")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

#Menu archivo
archivo= tk.Menu(menu)
menu.add_cascade(label="Archivo",menu=archivo)

#Menu edicion
edicion= tk.Menu(menu)
menu.add_cascade(label="Edicion",menu=edicion)

#Menu de credito
desarrollado = tk.Menu(menu)
menu.add_cascade(label="DEV",menu=desarrollado)

#Expandir y achicar ventana
area_de_texto= tk.Text(ventana)
area_de_texto.pack(fill=tk.BOTH, expand=True)

#Comandos de menu archivo
archivo.add_command(label="Nuevo", command= nuevo_archivo)
archivo.add_command(label="Abrir", command= abrir_archivo)
archivo.add_command(label="Guardar", command= guardar_archivo)
archivo.add_command(label="Guardar como", command= guardar_como)

#Comandos de menu edicion
edicion.add_command(label="Copiar",command= copiar)
edicion.add_command(label="Pegar",command= pegar)
edicion.add_command(label="Cortar",command= cortar)

desarrollado.add_command(label="Sarmiento Agustin",command=dev)




#inicializamos el mainloop
ventana.mainloop()
