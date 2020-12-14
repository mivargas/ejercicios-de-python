mi_diccionario = {"Alemania":"Berlin", "Francia":"paris", "Reino_unido":"Londres", "Espana":"Madrid"}
print(mi_diccionario)

print(mi_diccionario["Francia"])

mi_diccionario["Italia"]="Lisboa" #agregar
print(mi_diccionario)

mi_diccionario["Italia"]="Roma" #modificar
print(mi_diccionario)

del mi_diccionario["Reino_unido"] #eliminar
print(mi_diccionario)

mitupla = ("Venezuela", "Colombia", "Mexico") #asignar claves por medio de una tupla
midiccionario= {mitupla[0]:"Caracas", mitupla[1]:"Bogota", mitupla[2]:"Mexico"}
print(midiccionario)
print(midiccionario["Venezuela"])
print(midiccionario[mitupla[0]])

mi_diccionario2={"nombre":"miguel", "edad":23, "color":"blanco", "cusos":["php", "python", "java"], "educacion":{"escuela":"cristobal rojas", "liceo":"rafael uraneta", "universidad":"iutoms"}}
print(mi_diccionario2) #diccionarios que incluyen listas y diccionarios

print(mi_diccionario2.keys()) # imprime las claves
print(mi_diccionario2.values()) # imprime valores
print(len(mi_diccionario2)) #cuenta elementos
