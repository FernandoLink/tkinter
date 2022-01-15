from tkinter import *


def getval():
    print(slide.get())


window = Tk()
window.title('Scale')
window.geometry('300x200')

slide = Scale(window, from_=0, to=100, orient=HORIZONTAL, resolution=0.5)
slide.pack()

cmd = Button(window, text='Ver Valor', command=getval)
cmd.pack()

window = mainloop()
