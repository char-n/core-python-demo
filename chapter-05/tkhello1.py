# encoding=utf-8

import tkinter

top = tkinter.Tk()
# label = tkinter.Label(top, text='hello world')
button = tkinter.Button(top, text='hello world', command=top.quit)
button.pack()
tkinter.mainloop()
