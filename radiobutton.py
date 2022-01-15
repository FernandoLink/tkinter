from tkinter import *


def getradio():
    print(vara_rb.get(), varb_rb.get())


def raf1():
    print('Opção 1')


window = Tk()
window.title('Radio Button')

frameA = Frame(window)
frameA.pack()
frameB = Frame(window)
frameB.pack()

vara_rb = IntVar()
varb_rb = IntVar()

rb1 = Radiobutton(frameA, text='Opção A 1',
                  variable=vara_rb, value=1, command=raf1, indicatoron=0)
rb2 = Radiobutton(frameA, text='Opção A 2',
                  variable=vara_rb, value=2, indicatoron=0)
rb3 = Radiobutton(frameA, text='Opção A 3',
                  variable=vara_rb, value=3, indicatoron=0)
rb1.pack()
rb2.pack()
rb3.pack()
rb1.select()

rb1 = Radiobutton(frameB, text='Opção B 1',
                  variable=varb_rb, value=1, command=raf1)
rb2 = Radiobutton(frameB, text='Opção B 2',
                  variable=varb_rb, value=2)
rb3 = Radiobutton(frameB, text='Opção B 3',
                  variable=varb_rb, value=3)
rb1.pack()
rb2.pack()
rb3.pack()
rb1.select()

cmd = Button(window, text='Executar', command=getradio).pack()

window = mainloop()
