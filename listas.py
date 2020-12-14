mi_lista=["maria","pepe","marta", "antonio"]

print(mi_lista[3])

print(mi_lista[:])

print(mi_lista[0:3]) #solo mostrar los3 primeres elemento (indice, posicion) tambien ver cpmo (inclusive,exclusive)

print(mi_lista[:3]) #se asume que el primero es 0

print(mi_lista[2:]) #desde el indice 2 hasta el .

print(mi_lista[-2]) #posicion 2 de dercha a izquierda

mi_lista.append("camilo") #agregarelemento a la lista
print(mi_lista[:])

mi_lista.insert(2,"sandra") #agregar en la el espeacio de un indice determinado
print(mi_lista)


mi_lista.extend(["lucia", "teresa", "andres"]) #agrega varios elementos a la list
print(mi_lista[:])


print(mi_lista.index("antonio")) #ver el indice que tiene el elemento

print("teresa" in mi_lista) # ver si un elemento existe en la lista

mi_lista.remove("pepe") #elimina un elemento determinado de la list
print (mi_lista[:])

mi_lista.pop() #elimina el ultimo elemento de la lista
print(mi_lista)


mi_lista2= [3, True] #agregar listas
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)