from tkinter import *


window = Tk()
window.title('Message')

msg = Message(window, text='Este é um texto do message Widget.', width=200)
msg.pack()

window = mainloop()
