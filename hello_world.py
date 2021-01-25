from tkinter import *

root = Tk()
root.geometry('200x100')
root.config(bg='#000')
root.resizable(0,0)

Label(font='candara 24',text='Hello World!',
    fg='#fff',bg='#000').pack(pady=20)

mainloop()