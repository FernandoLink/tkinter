from tkinter import *


def click_button():
    label1['text'] = entry1.get()
    label2['text'] = entry2.get()
    label3['text'] = entry3.get()

window = Tk()
window.title('Focus Tab Order')

entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)
label1 = Label(window)
label2 = Label(window)
label3 = Label(window)
button = Button(window, text='Executar', command=click_button)

# a forma que colocar no grid é que define o tab order
entry1.grid()
entry2.grid()
entry3.grid()
label1.grid()
label2.grid()
label3.grid()
button.grid()

entry1.focus()

window = mainloop()
