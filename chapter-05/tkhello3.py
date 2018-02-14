# enconding=utf-8

import tkinter

top = tkinter.Tk()

label = tkinter.Label(top, text='hello world')
label.pack()

button = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
button.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
