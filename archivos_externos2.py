from io import open

"""
archivo_texto=open("archivo.txt","r") #solo lectura

print(archivo_texto.read())
archivo_texto.seek(0) #volve a posicionar el puntero al inicio para que vuelva a leer  y haga la lectura nuevamente para poder volver a imprimir ya que una vez que lee por defecto el puntero queda al final y no  hay mas nada que leer 
print(archivo_texto.read())
"""

"""
archivo_texto=open("archivo.txt","r")

archivo_texto.seek(11) #elpuntero se posicionara en la posicion 11 y apartir de alli leera   
print(archivo_texto.read())
"""

"""
archivo_texto=open("archivo.txt","r")

print(archivo_texto.read(11)) #hara una lectura hasta la posicion 11 y se detendra

print(archivo_texto.read()) #aqui le decimos que lea a partir de donde quedo el puntero (quedo en el 11)
"""

"""
archivo_texto=open("archivo.txt","r")

archivo_texto.seek(len(archivo_texto.read())/2) #le decimimos que se posicione donde encuentre la mitad del documento contando los caracteres y dividiendo la cantidad entre dos

print(archivo_texto.read())
"""

"""
archivo_texto=open("archivo.txt","r")

archivo_texto.seek(len(archivo_texto.readline())) # situa al final de la primera linea

print(archivo_texto.read())
"""

"""
archivo_texto=open("archivo.txt","r+") #lectura y escritura

archivo_texto.write("comienzo del texto") #añade esto al inicio y lo hace remplazando las pocisiones que ocupara el texto
"""

"""
archivo_texto=open("archivo.txt","r+") 

print(archivo_texto.readlines()) #devuelve una lista con los saltos de linea
"""

archivo_texto=open("archivo.txt","r+") 

lista_texto=archivo_texto.readlines() #crear una lista (lectura por lineas)

lista_texto[1]="estalinea  ha sido incluida desde el exterior\n" #modifica el segundo elemento de la lista

archivo_texto.seek(0) #posicionamos el cursor al inicio del documento

archivo_texto.writelines(lista_texto) #hacemos escritura por linias partiendo desde donde se posiciono el puntero (esto para escribir el cambio de la segunda linea)

archivo_texto.close() # cerrar el documento para evitar consumo innecesario de recursos