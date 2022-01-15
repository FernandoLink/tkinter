from tkinter import *
from settings import Settings


def button_click():
    celsius = (float(entry.get())-32) * 5/9
    var_text.set(f'{str(round(celsius,1))} °C')


window = Tk()
window_settings = Settings()
window.title(window_settings.title)
window.iconbitmap(window_settings.icon)

var_text = StringVar()

label1 = Label(window, text='Graus Fahrenheit:')
entry = Entry(window)
button = Button(window, text='Executar', command=button_click)
label2 = Label(window, textvariable=var_text)

label1.grid()
entry.grid()
button.grid()
label2.grid()

window = mainloop()
