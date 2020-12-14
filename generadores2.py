#yield from

""" yield
def devuelveCiudades(*ciudades): #el * indica que le vamos a pasar  un numero de valores a la vez una tupla en realidad
	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelveCiudades("Caracas", "Bogota", "Quito")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
"""

def devuelveCiudades(*ciudades): #el * indica que le vamos a pasar  un numero de valores a la vez una tupla en realidad
	for elemento in ciudades:
		"""for subelemento in elemento: #el yield from nos ayuda a ahorrarnos una segunda iteracion anidada
		y	yield from elemento"""
		yield from elemento

ciudades_devueltas=devuelveCiudades("Caracas", "Bogota", "Quito")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

