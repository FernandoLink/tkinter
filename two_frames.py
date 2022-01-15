from tkinter import *
from settings import Settings


window = Tk()
window.title('Two Frames')

frame_name = Frame(window)
frame_address = Frame(window)

label_first_name = Label(frame_name, text='First Name:')
label_last_name = Label(frame_name, text='Last Name:')
entry_first_name = Entry(frame_name)
entry_last_name = Entry(frame_name)

label_address = Label(frame_address, text='Address:')
label_city = Label(frame_address, text='City:')
entry_address = Entry(frame_address)
entry_city = Entry(frame_address)

button = Button(window, text='Salvar')

label_first_name.grid(row=0, column=0)
label_last_name.grid(row=1, column=0)
entry_first_name.grid(row=0, column=1)
entry_last_name.grid(row=1, column=1)

label_address.grid(row=0, column=0)
label_city.grid(row=1, column=0)
entry_address.grid(row=0, column=1)
entry_city.grid(row=1, column=1)

frame_name.grid(row=0, column=0)
frame_address.grid(row=0, column=1)

button.grid()


window = mainloop()
