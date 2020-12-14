class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo= modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True


	def estado(self):
		print("Marca:", self.marca,"\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)


class Moto(Vehiculos): #aqui estamos heredando de vehiculos(clase padre o super clase)
	pass

miMoto=Moto("Honda", "CRB") #al heredar hay que pasarlos parametros al constructor
miMoto.arrancar()

miMoto.estado()