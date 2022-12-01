from tkinter import *

root = Tk()
root.title("Здарова отец")
root.geometry('400x100')
button = Button(root, text="Изменить", height=15, width=3)


def change():
    button['text'] = "Изменено"
    button['bg'] = "#000000"
    button['activebackground'] = "#555555"
    button['fg'] = "#ffffff"
    button['activeforeground'] = "#ffffff"


button.config(command=change)
button.pack()
root.mainloop()
