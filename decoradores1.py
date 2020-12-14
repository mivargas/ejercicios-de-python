def function_decoradora(funcion_parametro):

	def function_interior():
		#acciones adicionales que decoran

		print("vamos a realizar un calculo: ")

		funcion_parametro()

		#acciones adicionales que decoran

		print("hemos terminado el calculo")


	return function_interior






@function_decoradora #esto quiere decir que la funcion suma sera decorada
def suma():
	print(15+20)

def resta():
	print(30-10)


suma()

resta()