from tkinter import *

root = Tk()
root.title("Здарова отец")
root.geometry('400x100')
button = Button(root, text="Hello", height=10, width=20)
button.pack()


def printer(event):
    print("Hello world")


# setOnClickListener
button.bind("<Button-1>", printer)
root.mainloop()
