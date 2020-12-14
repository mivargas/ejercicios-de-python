from tkinter import *

root=Tk()
root.title("primer entry")

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()


nombreLabel=Label(miFrame, text="Nombre:")
#nombreLabel.place(x=80, y=100) #forma incorrecta para trabajar con varios elementos ya que se superponen
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) #row para fila column para columnas esto para ubicar de forma ordenada los elementos, sticky es para  la alineacion en este caso n,s,e,w,ne,se,sw,nw. pad es el padding y para el vertical x para el horizontal

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame, text="Contraseña:")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion de Habitación:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroNombre=Entry(miFrame) #declaramos la entrada de texto (textbox) y por parametro dentro de quien estara
#cuadroTexto.place(x=100, y=100) #forma incorrecta para trabajar con varios elementos ya que se superponen
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="center")# con esto cambio el color de la fuente que se escribira por entrada de teclado y desde donde se escribira en este caso desde el centro

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2, column=1)
cuadroPassword.config(show="*") #para ocultar caracteres

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

root.mainloop()