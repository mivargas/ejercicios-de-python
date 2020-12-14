from tkinter import *

root=Tk()
root.title("primer label")

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="umg.png")

miLabel=Label(miFrame, image=miImagen)

#miLabel=Label(miFrame, text="Hola alumos de Python", fg="red", font=("Comic Sans MS",18)) #fg es color de fuente y font("tipo", tamaño de fuente)
#miLabel.pack()# no debe usarse o el frame solo se ajustara al tamañol del label
miLabel.place(x=100, y=200) # se usa para en lugar del pack y ubicamos en un sitio del frame con coordenadas
#Label(miFrame, text="hola alumos de Python").place(x=100, y=200) # en caso de solo usar un label puede simplificarse asi

root.mainloop()