import sqlite3

miConexion=sqlite3.connect("GestionProductos3")

miCursor=miConexion.cursor()



"""
miCursor.execute("SELECT * FROM productos WHERE seccion= 'ropa'") #consultar

productos=miCursor.fetchall()

print(productos)
"""

"""
miCursor.execute("UPDATE productos SET precio=22 WHERE nombre= 'pelota'") #actualizar
"""

miCursor.execute("DELETE FROM productos WHERE id= 4") #

miConexion.commit()



miConexion.close()
