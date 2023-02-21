from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Honda", variable=opcion,
            value='Honda', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Toyota", variable=opcion,
            value='Toyota', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Chevrolet", variable=opcion,
            value='Chevrolet', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Kia", variable=opcion,
            value='Kia', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()