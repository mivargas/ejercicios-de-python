class Coche():
	
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	def arrancar(self, arrancamos):
		self.enMarcha=arrancamos

		if (self.enMarcha): # es lo mismo que decir ==True
			return  "El coche en marcha"
		else:
			return "el coche esta parado"
	
	def estado(self):
		print("el coche tiene", self.ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de", self.largoChasis)

miCoche = Coche() 
print(miCoche.arrancar(True))
miCoche.estado()