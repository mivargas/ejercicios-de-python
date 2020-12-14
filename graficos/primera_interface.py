from tkinter import *

raiz=Tk()
raiz.title("Este es el titulo de la ventana")
#raiz.resizable(0,0) #evitar cambiar el tamaño de la ventana por defecto (0 es false eso quiere decir false de ancho y false de alto)
#raiz.iconbitmap('/home/miguel/Documentos/graficos/favicon.ico') #un icon de no funcionar usar el metodo de abajo

img = PhotoImage(file='favicon.ico')

raiz.tk.call('wm', 'iconphoto', raiz._w, img)

#raiz.geometry("650x350") #ancho y alto de la venta

raiz.config(bg="green") #color de fondo 

miFrame= Frame()
#miFrame.pack() #para incluir el frame en la ventana
#miFrame.pack(side="left" #se queda anclado en la izquierda)
#miFrame.pack(side="left", anchor="s") # a la izquierda y se mantenga abajo s,n,o,w los puntos cardenales
#miFrame.pack(fill="x") #solo para el ancho total (horizontal)
#miFrame.pack(fill="y", expand="True") #solo para el alto total (vertical)
miFrame.pack(fill="both", expand="True") #se expande total a lo alnto y ancho
miFrame.config(bg="red")

miFrame.config(width="650", height="350") #la raiz se ajusta al tamaño del frame por eso se quita el geometric

miFrame.config(bd=35) #para un borde en tamaño se complementa con el de abajo
miFrame.config(relief="groove") #tipo borde

miFrame.config(cursor="pirate") #cambiar cursosr solo sobre el frame (tambien hay otro llamado hand2)
#raiz.config(cursor="hand2") #esto en caso de querer que fuera del frame el cursor sea diferente tambien se puede aplicar a la raiz las mismas etiquetas que el frame para estilizar

raiz.mainloop()