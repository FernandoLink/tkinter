from tkinter import *


class NameWidget(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label = Label(self, text='Nome: ')
        entry = Entry(self)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)


window = Tk()
window.title('Login')
frame1 = NameWidget(window).grid()
frame2 = NameWidget(window).grid()
frame3 = NameWidget(window).grid()
frame4 = NameWidget(window).grid()
window = mainloop()
