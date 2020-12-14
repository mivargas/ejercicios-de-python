import pickle 

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

coche1=Vehiculos("mazda", "mx5")
coche2=Vehiculos("fiat", "34d")
coche3=Vehiculos("renault", "megane")

coches = [coche1,coche2,coche3]
fichero=open("losCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)


"""
#decodificacion 
fichero_apertura=open("losCoches","rb")

misCoches=pickle.load(fichero_apertura)

fichero_apertura.close()

for c in misCoches:
	print(c.estado())
"""