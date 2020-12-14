class Empleado():

	def __init__(self, nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario



	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

Empleado("juan", "director", 75000),
Empleado("ana", "presidente", 85000),
Empleado("antonio", "administrativo", 45000),
Empleado("sara", "analista", 25000),
Empleado("mario", "secratario", 15000)

]


salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)


for empledo_salario in salarios_altos:
	print(empledo_salario)