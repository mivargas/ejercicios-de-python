def areaTriagulo(base, altura):

	"""
	Calcula el area de un triagulo dado

	>>> areaTriagulo(3,6)
	8.0

	"""

	return (base*altura)/2


#print(areaTriagulo(2,4))

import doctest

doctest.testmod()

#dara un error porque debe devolver 9.0 no 8.0