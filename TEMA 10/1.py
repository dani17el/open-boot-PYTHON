import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="Hola!", bg="yellow", fg="blue")
label_saludo.pack(ipadx=30, ipady=30, side='left')

label_adios = tkinter.Label(window, text="Adios", bg="red", fg="white")
label_adios.pack(ipadx=30, ipady=30,)

window.mainloop()