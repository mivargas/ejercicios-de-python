from tkinter import *

root=Tk()
root.title("Radio")

varOpcion=IntVar()

def imprimir():
	print(varOpcion.get()) #para ver por cosola
	if varOpcion.get()==1:
		etiqueta.config(text="has elegido masculino")
	else:
		etiqueta.config(text="has elegido femenino")

Label(root, text="Genero:").pack()
Radiobutton(root, text="Maculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack() 

root.mainloop()