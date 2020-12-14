import re
#rangos

"""
lista_nombres=['ana',
			   'pedro',
			   'mascotas',
			   'maria',
			   'rosa',
			   'sandra',
			   'celia']

for elemento in lista_nombres:
	if re.findall('^[o-t]', elemento): #buscar nombres que caracter inicial este en ese rango, nota es sensible a mayusculas y minusculas (rango:o p q r s t)
		print(elemento)

"""

"""
lista_nombres=['ma1',
			   'se1',
			   'ba1',
			   'ma3',
			   'va1',
			   'va2',
			   'ma4']

for elemento in lista_nombres:
	if re.findall('ma[0-3]', elemento): # devuelve ma1 y ma 3
		print(elemento)


	if re.findall('ma[^0-3]', elemento): # rango negado (para negar el rango tambien se usa el acento circunflejo dentro del rango) devuelve ma4
		print(elemento)
"""

"""
lista_nombres=['ma1',
			   'se1',
			   'ba1',
			   'ma3',
			   'va1',
			   'va2',
			   'ma4',
			   'maA',
			   'maB',
			   'maC']

for elemento in lista_nombres:
	if re.findall('ma[0-3A-B]', elemento): # rango variado
		print(elemento)
"""


lista_nombres=['ma.1',
			   'se1',
			   'ba1',
			   'ma3',
			   'va1',
			   'va2',
			   'ma:4',
			   'ma.A',
			   'maB',
			   'ma:C']

for elemento in lista_nombres:
	if re.findall('ma[.:]', elemento): # rango variado
		print(elemento)