for i in [1,2,3]:
	print("hola")

for estacion in ["verano", "otoño", "invierno", "primavera"]:
	print(estacion)

for x in ["pytho", "php", "ruby"]:
	print("hola", end=" ") #decir que en vez de salto de linea deje espacios

for e in "miguel@gmail.com": #aqui solo tomara encuenta el numero de caracteres para la cantidad de veces a imprimir
	print("chao")



miemail = input("ingres email: ")
email=False #validar un correo (elfor recorrera caracter por caracter hasta que encuenrtre el @ y cambie a true)

#for g in "miguel@gmail.com":
for g in miemail:

	if g=="@":

		email=True
if email==True: #o if email:
	print("email correcto")
else:
	print("el email es incorrecto")


#otra forma


miemail = input("ingres email: ")
contador=0 #validar un correo (elfor recorrera caracter por caracter hasta que encuenrtre el @ y cambie a true)

#for g in "miguel@gmail.com":
for g in miemail:

	if g=="@" or g==".":

		contador=contador+1
if contador==2: 
	print("email correcto")
else:
	print("el email es incorrecto")


#con range
for t in range(5):
	print(t)


"""
for k in range(5,10,3): ṕrint con range y notacion especias, inica en 5 llegara hasta el 9 y aumenta de 3 en 3
	print(f"la variable tiene como valor {k}")
"""