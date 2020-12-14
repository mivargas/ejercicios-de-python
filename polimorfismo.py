class Coche():
	
	def desplazamiento(self):
		print("me desplazo usando 4 ruedas")


class Moto():
	def desplazamiento(self):
		print("me desplazo usando 2 ruedas")


class Camion():
	def desplazamiento(self):
		print("me desplazo usando 6 ruedas")
"""		
miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()
""" #precindir de esto que no es polimorfismo

def desplazamiento_vehiculo(vehiculo): #declarar una funcion generica fuera de cualquier clase
	vehiculo.desplazamiento()

miVehiculo=Coche() #declarar cualquie clase igual funcionara porque cambiara (polimorfismo)

desplazamiento_vehiculo(miVehiculo)# pasamos elobjeto instanciado como parametro 