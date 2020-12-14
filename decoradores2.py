def function_decoradora(funcion_parametro):

	def function_interior(*args, **kwargs): #numero indeterminado de prametros, el siguente argumento es para elementos clave valor
		#acciones adicionales que decoran

		print("vamos a realizar un calculo: ")

		funcion_parametro(*args, **kwargs)

		#acciones adicionales que decoran

		print("hemos terminado el calculo")


	return function_interior






@function_decoradora #esto quiere decir que la funcion suma sera decorada
def suma(num1, num2, num3):
	print(num1+num2+num3)

@function_decoradora
def resta(num1, num2):
	print(num1-num2)

@function_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))


suma(7,5,8)

resta(12,10)

potencia(base=5,exponente=3) #clave valor (kwargs)