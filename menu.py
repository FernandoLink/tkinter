from tkinter import *


def file_new():
    print('New')


window = Tk()
window.title('Menu')

my_menu = Menu(window)

file_menu = Menu(my_menu, tearoff=0)
file_menu.add_command(label='New', command=file_new)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Close')
file_menu.add_separator()
file_menu.add_command(label='Exit')
my_menu.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(my_menu, tearoff=0)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
my_menu.add_cascade(label='Edit', menu=edit_menu)

window.config(menu=my_menu)

window = mainloop()
