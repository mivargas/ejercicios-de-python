import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE productos(nombre varchar(50), precio integer, seccion varchar(20))") #comentar despues de ejecutar

#miCursor.execute("INSERT INTO productos VALUES('Balón', 15,'Deportes')" )

variosProductos=[
	("Camiseta",10, "Deportes"),
	("Jarron",90, "Ceramica"),
	("Camion",20, "Jugyetes")
]

#miCursor.executemany("INSERT INTO productos VALUES(?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM productos")

Todosproductos=miCursor.fetchall()
#print(Todosproductos)

for producto in Todosproductos:
	print("nombre articulo:", producto[0], "Seccion:", producto[2])

miConexion.commit()



miConexion.close()
