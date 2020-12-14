class Coche():

	def __init__(self): #usamos un constructor para hacer que los atributos tengan un valor por defecto

		self.largoChasis=250
		self.anchoChasis=120
		self.__ruedas=4 #aqui se encapsula una propiedad no importa que se busque de modificar el valor no podra hacerlo, solo se puededesde la misma clase
		self.__enMarcha=False # se puede modificar pero node manera direta, se hace gracias al metodo dentro de la misma clase al enviarle el "arrancamos" y en elmetodo igualrlo a enMarcha

	def arrancar(self, arrancamos):
		self.enMarcha=arrancamos

		if (self.enMarcha): # es lo mismo que decir ==True
			return  "El coche en marcha"
		else:
			return "el coche esta parado"
	
	def estado(self):
		print("el coche tiene", self.__ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de", self.largoChasis)

miCoche = Coche() 
print(miCoche.arrancar(True))
miCoche.ruedas=2 #para modificar un atributo esto se puede evitar (si es e vital importancia hacer que no san modificable) encapsular los atributos con el __ (seria como el private en php)
# miCoche.ruedas es lo mismo que decir miCoche.__ruedas
miCoche.estado()