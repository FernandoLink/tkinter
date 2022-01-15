from tkinter import *


def exec():
    print(list.get(ACTIVE))

window = Tk()
window.title('Check Button')

list = Listbox(window, selectmode=EXTENDED)
list.pack()

list.insert(0, 'Primeiro item da lista')
list.insert(2, 'Segundo item da lista')
list.insert(3, 'Terceiro item da lista')
list.insert(4, 'Quarto item da lista')

nomes = ['Fernando', 'Valéria', 'Luiza', 'Henrique', 'Arlete']
for nome in nomes :
    list.insert(END, nome)


list.delete(END)

cmd = Button(window, text='Clique', command=exec).pack()

window = mainloop()
