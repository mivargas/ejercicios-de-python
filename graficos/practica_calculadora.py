from tkinter import *

root=Tk()
root.title("Calculadora")

miFrame=Frame(root)
miFrame.pack()

operacion=""
resultado=0
#--------------------pantalla--------------------------
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#-------------------pulsaciones teclado-----------------------

def numeroPulsado(num):
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion=""
    else:
        #numeroPantalla.set(numeroPantalla.get() + "4") #prueba
        numeroPantalla.set(numeroPantalla.get() + num)


#---------------------funcion suma----------------------------
def suma(num):
    global operacion, resultado
    resultado+=int(num)
    operacion="suma"
    numeroPantalla.set(resultado)
    

#-------------------funcion del resultado-----------------------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0

#--------------------fila1--------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDividir=Button(miFrame, text="-/-", width=3)
botonDividir.grid(row=2, column=4)

#--------------------fila2--------------------------------

#boton4=Button(miFrame, text="4", width=3, command=numeroPulsado("4")) #llamada automatica ya al ejecutar el 4 se encuentra en el entri no esta bien asi
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4")) #lambda para que no sea automatico y llamar solo cuando se presiona el boton
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMultiplicar=Button(miFrame, text="x", width=3)
botonMultiplicar.grid(row=3, column=4)

#--------------------fila3--------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRestar=Button(miFrame, text="-", width=3)
botonRestar.grid(row=4, column=4)


#--------------------fila4--------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonSumar=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSumar.grid(row=5, column=3)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=4)
root.mainloop()