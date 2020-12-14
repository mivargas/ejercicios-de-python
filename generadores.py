def generaNumerosPares(limite):

	num=1

	milista=[]

	while num<limite:
		milista.append(num*2)

		num+=1

	return milista

print(generaNumerosPares(10))




def generaNumerosParesG(limite):

	num=1

	while num<limite:
		yield num*2

		num+=1

devuelvepares=generaNumerosParesG(10)

"""for i in devuelvepares:
		print(i)"""	

print(next(devuelvepares))
print("aqui hay mas codigo...")


print(next(devuelvepares))
print("aqui hay mas codigo...")


print(next(devuelvepares))
print("aqui hay mas codigo...")

