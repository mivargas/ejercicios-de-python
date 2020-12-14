from tkinter import *

root=Tk()
root.title("menu")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #separador
archivoMenu.add_command(label="Salir")

EdicionMenu=Menu(barraMenu, tearoff=0) # tearoff eliminar el lineado del menu
EdicionMenu.add_command(label="Copiar")
EdicionMenu.add_command(label="Cortar")
EdicionMenu.add_command(label="Pegar")

HerramientasMenu=Menu(barraMenu, tearoff=0)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de... ")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=EdicionMenu)

barraMenu.add_cascade(label="Herramientas", menu=HerramientasMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.mainloop()