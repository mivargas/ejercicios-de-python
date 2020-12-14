import math

def evalua_edad(edad):
	if(edad<0):
		raise TypeError("no se permiten edades negarivas") #esto es util cuando necesitamos provocar una excepcion nosotros mismos ( en este caso la edad negativa no se deberia permitir) y necesitamos que el programa no ejecute mas lineas de codigo a paritir de alli, es decir que caiga.
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	else: 
		return "cuidate"

#print(evalua_edad(-5))


def evalua_edad2(edad):
	if(edad<0):
		raise MiPropioErrors("no se permiten edades negarivas") #se pueden crear errores propios pero esto se debe manejar con objetos en clases porque sino arroba un doble error (ese objeto MipropioError no esta declarado)
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	else: 
		return "cuidate"

#print(evalua_edad2(-5))

def calcula_raiz(num1):
	if num1<0:
		raise ValueError("el numero no puede ser negativo")

	else:
		return math.sqrt(num1)

op1 = int(input("ingresa numero: "))

try:
	print(calcula_raiz(op1))
except ValueError as errorNumeroNegativo: 
	print(errorNumeroNegativo)

print("programa terminado")


"""
datos arrojados para capturar la execpcion:
-indica que debemos jacerlo en la linea 41

ingresa numero: -144
Traceback (most recent call last):
  File "excepciones3.py", line 41, in <module>
    print(calcula_raiz(op1))
  File "excepciones3.py", line 34, in calcula_raiz
    raise ValueError("el numero no puede ser negatovo")
ValueError: el numero no puede ser negatovo


"""