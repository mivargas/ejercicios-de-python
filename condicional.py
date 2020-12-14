"""
print("programa de notas")

nota_alumno= input("Introduce la nota del almuno: ")

def evaluacion(nota):
	valoracion = "aprobado"
	if nota < 5:
		valoracion = "reprobado"

	return valoracion

#print(evaluacion(5))
print(evaluacion(int(nota_alumno))) # HAY QUEINDICARLE QUE PASAREMOS UN NUMERICO


print("Verificacion de acceso")

edad_usuario= int(input("edad del usuario: "))

if edad_usuario<18:
	print("no puedes pasar")
elif edad_usuario>100:
	print("edad incorrecta")
else:
	print("puedes pasar")

print("fin del calculo")
"""



"""
#condiciones encadenadas o concatenadas
salario_presiente = int(input("Introduce el salario del presidente: ")) #ambos print son validos para conctenar un string con un entero
print("EL salario del presidente es %s"  %salario_presiente) 
print("EL salario del presidente es "  + str(salario_presiente))

salario_director = int(input("Introduce el salario del director: ")) #ambos print son validos para conctenar un string con un entero
print("EL salario del director es %s"  %salario_director) 
print("EL salario del director es "  + str(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe_area: ")) #ambos print son validos para conctenar un string con un entero
print("EL salario del jefe_area es %s"  %salario_jefe_area) 
print("EL salario del jefe_area es "  + str(salario_jefe_area))

salario_admin = int(input("Introduce el salario del administrativo: ")) #ambos print son validos para conctenar un string con un entero
print("EL salario del administrativo es %s"  %salario_admin) 
print("EL salario del administrativo es "  + str(salario_admin))

if salario_admin<salario_jefe_area<salario_director<salario_presiente:
	print("todo funciona bien")
else:
	print("algo anda mal")

"""


print("programa de becados")

distancia = int(input("Indique la distancia al instituto del aspirante a beca(Km): "))
print("Kilometros de distancia: %s" %distancia)

hermanos = int(input("Cantidad de hermanos del aspirante a beca: "))
print("Número de hermanos: %s" %hermanos)


salario_familiar = int(input("salario damiliar(euros): "))
print("Salario: %s" %salario_familiar)

#operador and
"""
if distancia>40 and hermanos >2 and salario_familiar <= 20000:
	print("el estudiante clasifica para una beca")

else:
	print("el estudiante no clasifica para una beca")
"""

if distancia>40 and hermanos >2 or salario_familiar <= 20000:
	print("el estudiante clasifica para una beca")

else:
	print("el estudiante no clasifica para una beca")



print("programa de asignaturas")
print("asignaturas: Informatica, Administacion, Mecanica")

opcion = input("ingrese asignatura: ")
asignatura = opcion.lower()

if asignatura in ("informatica", "administacion", "mecanica"):
	print("asignatura elegida: " + asignatura)
else:
	print("la asignatura %s no esta contemplada" %asignatura)