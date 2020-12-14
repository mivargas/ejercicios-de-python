import re
#clase de caracteres
"""
lista_nombres=['ana gomez',
			   'maria martin',
			   'sandra lopez',
			   'santiago martin']

for elemento in lista_nombres:
	if re.findall('^sandra', elemento): #circunflejo es  para de devuelva el elemento conpleto de todo lo que inice en la lista con sandra, si hay masde una sandra me devolvera todas las que encuentre junto con su apellido
		print(elemento)

	if re.findall('martin$', elemento): #circunflejo es  para de devuelva el elemento conpleto de todo lo que termine en la lista con sandra, si hay masde una sandra me devolvera todas las que encuentre junto con su apellido
		print(elemento)

"""


"""
lista_nombres=['http://misitio.es',
			   'ftp://misitio.es',
			   'http://misitio.com',
			   'ftp://misitio.com']

for elemento in lista_nombres:
	if re.findall('^ftp', elemento): #circunflejo es  para de devuelva el elemento conpleto de todo lo que inice en la lista con sandra, si hay masde una sandra me devolvera todas las que encuentre junto con su apellido
		print(elemento)

	if re.findall('es$', elemento): #circunflejo es  para de devuelva el elemento conpleto de todo lo que termine en la lista con sandra, si hay masde una sandra me devolvera todas las que encuentre junto con su apellido
		print(elemento)

"""

""" 
lista_nombres=['http://misitio.es',
			   'http://mañana.es',
			   'http://misitio.com']

for elemento in lista_nombres:
	if re.findall('[ñ]', elemento): #busqueda por caracter me devolvera el elemento o lementos eneteros que contengan ese cracter
		print(elemento)

"""

lista_nombres=['hombre',
			   'mujeres',
			   'mascotas',
			   'niños',
			   'niñas',
			   'camion',
			   'camión']

for elemento in lista_nombres:
	if re.findall('niñ[oa]s', elemento): #busqueda por caracter me devolvera el elemento o lementos eneteros que contengan esoscaracteres (variacion)
		print(elemento)

	if re.findall('cami[oó]n', elemento): #busqueda por caracter me devolvera el elemento o lementos eneteros que contengan esoscaracteres (variacion)
		print(elemento)