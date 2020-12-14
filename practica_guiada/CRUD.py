from tkinter import *
from tkinter import messagebox
import sqlite3

#***********************Funciones******************

def conexionBD():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE datosusuarios (
			id integer primary key autoincrement,
			nombreusuario varchar(50),
			password varchar(50),
			apellido varchar(50),
			direccion varchar(50),
			comentarios varchar(100))
			''')
		messagebox.showinfo("BD", "Base de datos creada con exito")

	except:

		messagebox.showwarning("¡ATENCION!", "La base de datos ya existe")

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete(1.0, END) #para el text decomentarios

def crear():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	"""miCursor.execute("INSERT INTO datosusuarios VALUES(NULL, '"+miNombre.get()+
		"', '"+miPass.get()+
		"', '"+miApellido.get()+
		"', '"+miDireccion.get()+
		"', '"+textoComentario.get("1.0", END)+
		"')")"""

	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)

	miCursor.execute("INSERT INTO datosusuarios VALUES(NULL, ?,?,?,?,?)", datos) #consulta parametrizada evita el sql inyection

	miConexion.commit()

	messagebox.showinfo("BD", "Registro insertado con exito")

def leer():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM datosusuarios WHERE id =" +miId.get())

	elUsuario=miCursor.fetchall()

	textoComentario.delete(1.0, END)

	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()


def actualizar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE datosusuarios SET nombreusuario='"+miNombre.get()+
		"', password='"+miPass.get()+
		"', apellido='"+miApellido.get()+
		"', direccion='"+miDireccion.get()+
		"', comentarios='"+textoComentario.get("1.0", END)+
		"' WHERE id="+miId.get())

	miConexion.commit()

	messagebox.showinfo("BD", "Registro actualizado con exito")


def eliminar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM datosusuarios WHERE id=" +miId.get())

	miConexion.commit()

	messagebox.showinfo("BD", "Registro borrado con exito")

#***********************menu******************
root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de... ")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#***************comienzo de campos************************
miFrame=Frame(root)
miFrame.pack()


miId= StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nswe")

textoComentario.config(yscrollcommand=scrollVert.set)


#***************Labels************************************

idLabel=Label(miFrame, text="Id")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Clave")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido")
ApellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#***************Botones************************************

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create")
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

root.mainloop()