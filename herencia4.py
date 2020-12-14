class Persona():
	def __init__(self, nombre, edad, direccion):

		self.nombre = nombre
		self.edad = edad
		self.direccion = direccion

	def descripcion(self):
		print("Nombre:", self.nombre, "Edad:", self.edad, "Dirección", self.direccion)		


class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, direccion_empleado): # se añaden parametros donde iran los de la clase padre nombre, edad y direccion
	#def __init__(self, salario, antiguedad): # valores estaticos
		#super(Empleado, self).__init__("Antonio", 55, "Venezuela") #usar los atribulos delconstructor de la clase padre... esto con valores estaticos
		super(Empleado, self).__init__(nombre_empleado, edad_empleado, direccion_empleado) #argumentos de la clase padre(como fueron declarados arriba como parametro)	
		self.salario = salario
		self.antiguedad = antiguedad
		
	def descripcion(self): #sobrescribir el metodo descripcion de la clase padre
		super().descripcion() #usar super para poder usar el metodo de arriba (una especie de concatenacion)
		print("Salario:", self.salario, "Antigüedad:", self.antiguedad) #esto se unira al final de lo que devuelve el metodo descripcion original (el de la clase padre)

#antonio = Persona("Antonio", 55, "Venezuela")

#antonio = Empleado(1500, 5)con valores estaticos

antonio = Empleado(1500, 5, "Antonio", 55, "Venezuela")
antonio.descripcion()


#un objeto de la sub clase siempre sera un objeto de la super clase.
print(isinstance(antonio, Persona)) #esto se usa para comprobar si una clase pertenece una super clase... basicamente dice antonio es una persona?(mas a lo fondo quiere decir empledo es uns persona?)