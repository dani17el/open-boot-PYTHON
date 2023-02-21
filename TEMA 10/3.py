import tkinter
from tkinter import ttk

window = tkinter.Tk()

label1 = tkinter.Label(window, text="Posicionamiento absoluto", bg='blue', fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(window, text="Otro mas", bg='red', fg='yellow')
label2.place(x=25, y=30)

window.mainloop()