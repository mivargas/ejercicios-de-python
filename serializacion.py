import pickle #importar la libreria para la serializacion binaria

""" #crear fichero
lista_nombres=["pedro", "ana", "mario", "isabel"] # lista para volvar los datos (dump)

fichero_binario=open("lista_nombres", "wb") #se crea el archivo (fichero) con escritura binaria (wb)

pickle.dump(lista_nombres, fichero_binario) #funcion para volcar la lista 

fichero_binario.close() #cerrar el fichero

del (fichero_binario) #borrar el fichero del espacion en memoria
"""


#recuperar fichero
fichero=open("lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista)