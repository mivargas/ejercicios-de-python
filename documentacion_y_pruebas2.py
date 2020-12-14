def areaTriagulo(base, altura):

	"""
	Calcula el area de un triagulo dado

	>>> areaTriagulo(3,6)
	'El area del triagulo es: 9.0'

	>>> areaTriagulo(4,5)
	'El area del triagulo es: 10.0'

	>>> areaTriagulo(9,3)
	'El area del triagulo es: 13.5'

	"""

	return "El area del triagulo es: " +str((base*altura)/2)



import doctest

doctest.testmod()