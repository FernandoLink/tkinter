from tkinter import *
from settings import Settings


window = Tk()
window.title('Login')

Label(window, text='User').grid(row=0, column=0, sticky=W)
Label(window, text='Password').grid(row=1, column=0, sticky=W)

user = Entry(window).grid(row=0, column=1)
passwd = Entry(window).grid(row=1, column=1)

cmd_button = Button(window, text='Login').grid(row=2, column=1, sticky=E)

window = mainloop()
