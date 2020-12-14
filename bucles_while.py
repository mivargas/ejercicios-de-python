import math
i=1

while i <= 10:
	print("ejecucion " + str(i))
	i+=1
print("fin de la ejecucion")

edad= int(input("introduce edad: "))

while edad<8 or edad>100:
	print("edad no valida")
	edad=int(input("introduce nuevamente la edad: "))

print("gracias por usar el programa")
print("edad es %s" %edad)



print("calculo raiz cuadrada")
numero= int(input("ingrese numero: "))

intentos = 0

while numero<0:
	print("no ingrese numeros negativos")

	if intentos==2:
		print("demasiados intentos fallidos, fin de ejecucion...")
		break;
	
	
	numero= int(input("por favor ingrese nuevamente el numero: "))
	if numero<0:
		intentos+=1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de %s es %d" %(numero,solucion))


