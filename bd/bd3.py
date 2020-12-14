import sqlite3

miConexion=sqlite3.connect("GestionProductos2")

miCursor=miConexion.cursor()

"""  #GestionProductos
miCursor.execute('''CREATE TABLE productos(
	codigo varchar(4) PRIMARY KEY, 
	nombre varchar(50), 
	precio integer, 
	seccion varchar(20))
	''')


misProductos=[
("AR01", "pelota", 29, "Juguetes"),
("AR02", "carrito", 33, "Juguetes"),
("AR03", "martillo", 93, "ferreteria"),
("AR04", "pantalon", 12, "ropa"),

]
"""

miCursor.execute('''CREATE TABLE productos(
	id integer PRIMARY KEY AUTOINCREMENT, 
	nombre varchar(50), 
	precio integer, 
	seccion varchar(20))
	''')


misProductos=[
("pelota", 29, "Juguetes"),
("carrito", 33, "Juguetes"),
("martillo", 93, "ferreteria"),
("pantalon", 12, "ropa"),

]

miCursor.executemany("INSERT INTO productos VALUES(NULL,?,?,?)", misProductos)

miConexion.commit()



miConexion.close()
