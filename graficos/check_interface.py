from tkinter import *

root=Tk()
root.title("checks")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opciones_viaje():
	
	opcionEscojida=""

	if playa.get()==1:
		opcionEscojida+=" playa"

	if montana.get()==1:
		opcionEscojida+=" montaña"

	if turismoRural.get()==1:
		opcionEscojida+=" turismo rutal"

	textoFinal.config(text=opcionEscojida)

foto=PhotoImage(file="avion.png")

Label(root, image=foto).pack()

 
frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opciones_viaje).pack()
Checkbutton(frame, text="montaña", variable=montana, onvalue=1, offvalue=0, command=opciones_viaje).pack()
Checkbutton(frame, text="turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opciones_viaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()