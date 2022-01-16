from tkinter import *


def executar():
    print(spinbox1.get(), spinbox2.get(), spinbox3.get())


window = Tk()
window.title('SpinBox')
window.geometry('300x200')

spinbox1 = Spinbox(window, from_=0, to=10)
spinbox1.pack()
spinbox2 = Spinbox(window, values=(10, 20, 30, 40), wrap=True)
spinbox2.pack()
spinbox3 = Spinbox(window, values=(
    'Fernando', 'Valéria', 'Luiza', 'Henrique'))
spinbox3.pack()

cmd = Button(window, text='Clique', command=executar)
cmd.pack()

window = mainloop()
