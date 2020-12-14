from io import open

archivo_texto=open("archivo.txt","w") #creacion y apertura (sino existe el archivo lo crea, de lo contrario solo lo abre). la w es de escritura tambien hay metodos para solo lectura y append (agregar contenido al documento)

frase= "Buen dia paa estudiar python \n el viernes" 

archivo_texto.write(frase)

archivo_texto.close()


archivo_texto=open("archivo.txt","r") #solo lectura

texto=archivo_texto.read()

archivo_texto.close()

print(texto)


"""
archivo_texto=open("archivo.txt","r") #solo lectura

lineas_texto=archivo_texto.readlines() #leer linea por linea,esto se almacena en una lista

archivo_texto.close()

#print(lineas_texto) # la lista
print(lineas_texto[1]) #un elemento de la lista en ete caso en segunda pisicion
"""

"""
archivo_texto=open("archivo.txt","a") #solo "a" es de append para añadir

archivo_texto.write("\n siempre es una buena ocacion para estudiar python")

archivo_texto.close()

"""
