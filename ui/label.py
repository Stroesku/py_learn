from tkinter import *

root = Tk()
# label1 = Label(text="Виджет", font='Arial 32')
# label2 = Label(text="и его свойство font", font=("Comic Sans MS", 24, "bold"))
#
# label1.pack()
# label2.pack()
# root.mainloop()
# ------------------------------------

entry = Entry(width=50)


def insert():
    entry.insert(0, "FFFF")


button = Button(text = "Insert", command=insert)
entry.pack()
button.pack()

root.mainloop()
