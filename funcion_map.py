class Empleado():

	def __init__(self, nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario



	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

Empleado("juan", "director", 6700),
Empleado("ana", "presidente", 7500),
Empleado("antonio", "administrativo", 2100),
Empleado("sara", "analista", 1950),
Empleado("mario", "secratario", 1800)

]


def calculo_comision(empleado):
	
	if  empleado.salario <= 3000:
		empleado.salario=empleado.salario*1.03
	
	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados) #con map se aplica la funcion para cada elemento iterable

for empleado in listaEmpleadosComision:
	print(empleado)