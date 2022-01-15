from tkinter import *
from settings import Settings


window = Tk()
window.title('Frame')

frame_login = Frame(window)

label_usr = Label(frame_login, text='User')
label_pwd = Label(frame_login, text='Password:')
entry_usr = Entry(frame_login)
entry_pwd = Entry(frame_login)
button = Button(frame_login, text='Entrar')

label_usr.grid(row=0, column=0)
label_pwd.grid(row=1, column=0)
entry_usr.grid(row=0, column=1)
entry_pwd.grid(row=1, column=1)
button.grid(row=2, column=1)
frame_login.grid()

entry_usr.focus()


window = mainloop()
