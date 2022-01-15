from tkinter import *
from settings import Settings


def button_click():
    var_text.set('O teu nome é ' + entry.get())


window = Tk()
window_settings = Settings()
window.title(window_settings.title)
window.iconbitmap(window_settings.icon)

var_text = StringVar()

label1 = Label(window, text='Escreve o teu nome:')
entry = Entry(window)
button = Button(window, text='Executar', command=button_click)
label2 = Label(window, textvariable=var_text)

label1.grid()
entry.grid()
button.grid()
label2.grid()

window = mainloop()
