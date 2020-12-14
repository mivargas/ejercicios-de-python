def suma(num1, num2, num3):


	""" calcula las sumade 3 elementos
	pasados por parametro a esa funcion"""

	print(num1+num2+num3)


def resta(num1, num2):
	print(num1-num2)

def potencia(base, exponente):
	print(pow(base, exponente))

suma(2,4,7)
print(suma.__doc__) # imprimir la documentacion en consola

help(suma)