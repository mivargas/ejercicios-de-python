class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	def arrancar(self): #self hace refrencia al objeto de la clase este parametro siempre debe ir al trabajar con clases (funciones normales de PE no se usa)
		self.enMarcha = True

	def estado(self):
		if (self.enMarcha==True):
			return  "El coche en marcha"
		else:
			return "el coche esta parado"


miCoche = Coche() #instanciar una clase (nose una el new como en php y java)

print("el largo del coche es: ", miCoche.largoChasis)

print("el largo del coche tiene", miCoche.ruedas, "ruedas")

miCoche.arrancar() #ejecuta el metodo
print(miCoche.estado())

print("-----------------acontinuacion creamos elsegundo objeto-------------------------")

miCoche2=Coche()
print("el largo del coche es: ", miCoche2.largoChasis)

print("el largo del coche tiene", miCoche2.ruedas, "ruedas")
print(miCoche2.estado())
