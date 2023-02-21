from tkinter import *

master = Tk()
elemento = StringVar()
listbox = Listbox(master)

for item in ["Jona", "Dani", "Fatima", "Luis", "Valentina"]:
    listbox.insert(END, item)

listbox.pack()
label = Label(text="Lista de nombres")
label.pack()

master.mainloop()