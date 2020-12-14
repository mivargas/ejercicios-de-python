from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("dialogo")

def abreFichero():

    fichero=filedialog.askopenfilename(title="Abrir", initialdir="/", filetypes=(("Archivos de excel","*.xls"), ("Archivos de texto", "*.docx"), ("Todos los archivos", "*.*")))
    print(fichero)


Button(root, text="Abrir fichero", command=abreFichero).pack()    
    
root.mainloop()