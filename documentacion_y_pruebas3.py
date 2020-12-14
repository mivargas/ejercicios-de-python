def compruebaMail(mailUser):

	"""
	la funcion comprueba mail evalua un mail
	recibido en busca de la arroba. Si tiene una @
	es correcto, si tiene mas de una @ es incorrecto,
	si tiene una @ al final es incorrecto
	

	>>> compruebaMail('juan@cursos.com')
	True

	>>> compruebaMail('juancursos.com@')
	False

	>>> compruebaMail('juancursos.com')
	False

	>>> compruebaMail('juan@cursos@.com')
	False

	"""



	arroba=mailUser.count('@')

	if arroba!=1 or mailUser.rfind('@')==(len(mailUser)-1) or mailUser.find('@')==0:
		return False
	else:
		return True
	


import doctest

doctest.testmod()