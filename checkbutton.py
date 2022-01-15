from tkinter import *


def show_message():
    print(val_check.get())


window = Tk()
window.title('Check Button')

val_check = IntVar()

check = Checkbutton(window,
                    text='CheckBox',
                    variable=val_check,
                    command=show_message).pack()


window = mainloop()
