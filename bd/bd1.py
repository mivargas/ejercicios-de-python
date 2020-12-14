import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE productos(nombre varchar(50), precio integer, seccion varchar(20))") #comentar despues de ejecutar

miCursor.execute("INSERT INTO productos VALUES('Balón', 15,'Deportes')" )

miConexion.commit()



miConexion.close()
