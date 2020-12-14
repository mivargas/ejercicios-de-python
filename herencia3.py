class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True


	def estado(self):
		print("Marca:", self.marca,"\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)


class Furgoneta(Vehiculos):
	
	def carga(self, cargar):
		self.cargado= cargar
		if self.cargado:
			return "La Furgoneta esta cargada"
		else:
			return "La Furgoneta no esta cargada"


class Moto(Vehiculos): #aqui estamos heredando de vehiculos(clase padre o super clase)
	hcaballito=""

	def caballito(self):
		self.hcaballito="voy haciendo el caballito"

	def estado(self): #para poder usar un metodo de la clase padre con atributos de la clase hija se debe sobre escribir el mismo metodo en la clase hija con el nuevo atributo que le pertrnece a est en este caso la variable caballito
		print("Marca:", self.marca,"\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\n", self.hcaballito)

class VElectricos(): #clase independiente
	def __init__(self):
		self.autonimia = 100

	def cargarEnergia(self):
		self.cargando=True
		
miMoto=Moto("Honda", "CRB") #al heredar hay que pasarlos parametros al constructor
miMoto.arrancar()

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectricos, Vehiculos):#herencia multiple (2 clases padre), hereda de las dos clases metodos y atributos
	pass

miBici = BicicletaElectrica() # no se le pasan los parametros marca y modelo porque se declaro primero en la herencia VElectricos (esto le da mas prioridad), al ser de forma contraria si deberia pasar esos parametros en la instancia