# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:36:04 2020

@author: aprietoabollado
"""

from tkinter import *
from tkinter import filedialog as FileDialog

ruta = "" # La utilizaremos para almacenar la ruta de un fichero

# Funciones

def nuevo():
	global ruta # Hay que definirla como una variable global, ya que las funciones tienen propio
				# namespace
	
	mensaje.set("Nuevo fichero")
	ruta = ""
	texto.delete(1.0, "end")
	root.title("Mi Editor")
	


def abrir():
	global ruta
	
	mensaje.set("Abrir fichero")
	ruta = FileDialog.askopenfilename(initialdir=".",
		   filetype=(("Ficheros de texto", "*.txt"),),
		   title="Abrir un fichero de texto" )
	if ruta != "":
		fichero = open(ruta, "r")
		contenido = fichero.read()
		texto.delete(1.0, "end")
		texto.insert("insert", contenido)
		fichero.close()
		root.title("Mi Editor - " + ruta)

def guardar():
	global ruta
	mensaje.set("Guardar fichero")
	if ruta != "":
		contenido = texto.get(1.0, "end-1c")
		fichero = open(ruta, "w+")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado correctamente")
	else:
		guardar_como()

def guardar_como():
	global ruta
	mensaje.set("Guardar fichero como")
	fichero = FileDialog.asksaveasfile(title = "Guardar fichero", mode = "w", defaultextension=".txt")
	if fichero is not None:
		ruta = fichero.name
		contenido = texto.get(1.0, "end-1c")
		fichero = open(ruta, "w+")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado correctamente")
	else:
		mensaje.set("Guardado cancelado")
		ruta = ""

root = Tk()
root.title("Mi Editor")

# Menú superior
menubar = Menu(root)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como...", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command = root.destroy)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)



root.mainloop()