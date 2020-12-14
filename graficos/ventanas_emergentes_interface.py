from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("menu")

def infoAdicional():
	messagebox.showinfo("procesador de miguel", "procesador 2020")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	"""valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicaicion?")

	if valor=="yes":
		root.quit()
	"""

	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicaicion?")

	if valor==True:
		root.quit()


def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar, documento bloqueado")

	if valor==False:
		root.quit()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #separador
archivoMenu.add_command(label="Salir", command=cerrarDocumento) #command=salirAplicacion)

EdicionMenu=Menu(barraMenu, tearoff=0) # tearoff eliminar el lineado del menu
EdicionMenu.add_command(label="Copiar")
EdicionMenu.add_command(label="Cortar")
EdicionMenu.add_command(label="Pegar")

HerramientasMenu=Menu(barraMenu, tearoff=0)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de... ", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=EdicionMenu)

barraMenu.add_cascade(label="Herramientas", menu=HerramientasMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.mainloop()