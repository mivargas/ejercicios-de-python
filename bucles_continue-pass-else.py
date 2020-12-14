for letra in "python":
	if letra=="h":
		continue
	print("viendo la letra " + letra)


#utilidad ejemplo
nombre="curso de python"
print(len(nombre)) #toma en cuenta los espacios en blanco no deberia si queremos sber cantidad de letras


nombre="curso de python"
contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1
print(contador)


#pass
class ClassName(object):
	pass #dejar algo declarado para usar mas tarde
	

#else de un bucle

email=input("introduce email: ")
for i in email:
	if i=="@":
		arroba=True
		break;
else: #este else no funciona igal que el de un if solo se activa si terminael recorrido y no encuentra ningun @
	arroba=False

print(arroba)