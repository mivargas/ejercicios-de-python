import re


cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
"""
print(re.search("aprender", cadena)) #encuentra coincidencia en la cadena con lapalabra
"""
textoBuscar="aprender"

"""
if re.search(textoBuscar, cadena) is not None: # una forma mas sofisticada que laanterior
	print("He encontrado el texto")

else:

	print("No he encontraod el texto")

"""

textoEncontrado=re.search(textoBuscar, cadena) # se almacena objeto devuelto en una variable pare usar los siguentes metodos:
"""
print(textoEncontrado.start()) #se obtiene el caracter donde comieza
print(textoEncontrado.end()) #se obtiene el caracter donde termina
print(textoEncontrado.span()) # devueve una tupla de donde comienza y donde termina (una combinacion de los dos metodos anteriores)
"""

textoBuscar2="Python"

print(re.findall(textoBuscar2, cadena)) #devuelve lista con concidencias

print(len(re.findall(textoBuscar2, cadena)))