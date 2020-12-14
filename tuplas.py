mi_tupla = ("miguel", 3, 8, 1992, 8)
print(mi_tupla[2]) #v ver un elemento en especifico

indice = mi_tupla.index(3) #en tuplas solo disponibles par python 2.7 en adelnte
print(indice)

milista=list(mi_tupla) #convertir tupla a lista
print(milista)


mi_lista= ["hola", 4, False] #lista a tupla
mitupla= tuple(mi_lista)
print(mitupla)

print("miguel" in mi_tupla) # ver si existe un elemento

print(len(mi_tupla)) #contar elemento de la tupla

print(mi_tupla.count(8)) #contar cuantos cantidad de elementos repetidos

tupla_uni = ("miguel",) #tupla unitaria, debe tener una coma
print(tupla_uni)

nombre, dia, mes, anio, otro = mi_tupla #desempacquetado de tupla
print(nombre)
print(dia)
print(mes)
print(anio)
print(otro)