def divide():
	try:

		n1=float(input("ingrese primer nunero: "))
		n2=float(input("ingrese segundo nunero: "))
		print("Resultado " + str(n1/n2))

	except ValueError: 
		print("caracteres no valido")

	except ZeroDivisionError: #se pueden presentar varias excepciones
		print("no se puede dividir por 0")

	print("operacion finalizada")

divide()


"""

def divide():
	try:

		n1=float(input("ingrese primer nunero: "))
		n2=float(input("ingrese segundo nunero: "))
		print("Resultado " + str(n1/n2))

	except:
		print(" ha ocurrido un error") #tambien puede ser uno general

	print("operacion finalizada")

divide()

"""



"""


def divide():
	try:

		n1=float(input("ingrese primer nunero: "))
		n2=float(input("ingrese segundo nunero: "))
		print("Resultado " + str(n1/n2))

	except ValueError: 
		print("caracteres no valido")

	except ZeroDivisionError: #se pueden presentar varias excepciones
		print("no se puede dividir por 0")

	finally: # lo que esta aqui se ejecutara siempre independiente mente si pasa por try o un except

		print("operacion finalizada")

divide()


"""