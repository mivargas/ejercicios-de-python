from setuptools import setup

setup(

	name="paquetecalculos",
	version="1.0",
	description="paquete de redondeo y potencia",
	author="miguel",
	author_email="miguelvargas619@gmail.com", #opcional
	url="w.com", #opcional
	packages=["paquetes/calculo","paquetes/calculo.sub_paquete_otros"] #este es escencial
	#packages=["calculo","calculo.sub_paquete_otros"] #lo ideal es que estuviera en una carpeta mas cercana a la raiz en eeste caso fuera de paquetes

	)