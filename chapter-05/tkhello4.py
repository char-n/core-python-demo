# encoding=utf-8

from tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
label = Label(top, text='hello world', font='Helvetica -12 bold')
label.pack()

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=Y, expand=1)

button = Button(top, text='quit', command=top.quit, activeforeground='white', activebackground='red')
button.pack()

mainloop()