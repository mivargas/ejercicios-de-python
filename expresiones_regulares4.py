import re
#match busca al inico

"""
nombre="Sandra López"

nombre2="Antonio Gómez"

nombre3="María López"

if re.match("Sandra", nombre, re.IGNORECASE): #el tercer parametroes para que no distinga entre mayusculas y minusculas
	print("hemos encontrado el nombre")

else:
	print("no lo hemos encontrado")

"""

"""
nombre="Jara López"

nombre2="Antonio Gómez"

nombre3="Lara López"

if re.match(".ara", nombre, re.IGNORECASE): # elpunto es sustitucion en este caso buscara cualquier nombre que tenha ara el primer cracter puede ser el que sea en ete caso encuentra lara y jara
	print("hemos encontrado el nombre")

else:
	print("no lo hemos encontrado")

"""

"""
ombre="Jara López"

nombre2="235333"

nombre3="a235333"

if re.match("\d", nombre2,): # la \d indica digito es para encontrar numeros
	print("hemos encontrado el digito")

else:
	print("no lo hemos encontrado")
""" 

################sear busca en toda la cadena a diferencia de match que es alinicio

"""
nombre="Jara López"

nombre2="Antonio Gómez"

nombre3="Lara López"

if re.search("lópez", nombre, re.IGNORECASE): # elpunto es sustitucion en este caso buscara cualquier nombre que tenha ara el primer cracter puede ser el que sea en ete caso encuentra lara y jara
	print("hemos encontrado el nombre")

else:
	print("no lo hemos encontrado")

"""

nombre="jkdnksdnkdskfnmsdkfnsdk71lfvdfk"

nombre2="dfghfhfdlsdlglsmggdgs"

nombre3="jkdnks71dnkdskfnmsdkfnsdkvdgfddfvdfk"

if re.search("71", nombre, re.IGNORECASE): # elpunto es sustitucion en este caso buscara cualquier nombre que tenha ara el primer cracter puede ser el que sea en ete caso encuentra lara y jara
	print("hemos encontrado el el 71")

else:
	print("no lo hemos encontrado")