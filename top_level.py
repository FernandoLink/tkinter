from tkinter import *


def open_form():
    top = Toplevel()
    top.title('Novo Formulário')
    top.geometry('200x100')
    label = Label(top, text='Label na Toplevel')
    label.pack()


window = Tk()
window.title('SpinBox')
window.geometry('300x200')

btn = Button(window, text='Novo', command=open_form)
btn.pack()

window = mainloop()
