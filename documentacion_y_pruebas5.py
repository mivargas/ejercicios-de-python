import math


def raizCuadrada(listaNumeros):
	
	"""
	la funcion devuelve una lista con la raiz cuadrada
	de los elementos numericos pasados por parametros en
	otra lista

	>>> lista=[]
	>>> for i in [4, 9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]



	>>> lista=[]
	>>> for i in [4, -9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
  		...
	ValueError: math domain error

	"""

	return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9,16,25,36]))

import doctest
doctest.testmod()









#manejar errores y execpciones en pruebas


"""

Traceback (most recent call last):
  File "documentacion_y_pruebas5.py", line 21, in <module>
    print(raizCuadrada([9,-16,25,36]))
  File "documentacion_y_pruebas5.py", line 19, in raizCuadrada
    return [math.sqrt(n) for n in listaNumeros]
  File "documentacion_y_pruebas5.py", line 19, in <listcomp>
    return [math.sqrt(n) for n in listaNumeros]
ValueError: math domain error


#esto de arriba se debe quitar no es documentacion esto se pone en la ultima prueba primera linea y ultima lo del medio se remplaza con ...porque las lineas delmedio pueden variar
"""