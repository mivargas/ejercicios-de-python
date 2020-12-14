"""
def area_triangulo(base, altura):
	return (base*altura)/2

area=area_triangulo(4,8)

print(area)
""" #funcion comun


#funcion lambda. Solo para funciones basicas como calculo no admite condicionales
area_triangulo=lambda base, altura:(base*altura)/2

area1=area_triangulo(6,9)

area2  =area_triangulo(2,10)

print(area1)
print(area2)


destacar_valor=lambda comision: "¡{}! €".format(comision)

comision_david=15585

print(destacar_valor(comision_david))