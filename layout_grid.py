from tkinter import *
from settings import Settings


window = Tk()
window_settings = Settings()
window.title(window_settings.title)
posx = int(window.winfo_screenwidth() / 2 - window_settings.screen_width / 2)
posy = int(window.winfo_screenheight() / 2 - window_settings.screen_height / 2)
window.geometry(
    f'{window_settings.screen_width}x{window_settings.screen_height}+{posx}+{posy}')
window.iconbitmap(window_settings.icon)

label1 = Label(window, text='Label1', font='Arial 20', bg='red')
label2 = Label(window, text='Label2', font='Arial 20', bg='green')
label3 = Label(window, text='Label3', font='Arial 20', bg='blue')

button1 = Button(window, text='Button1')
button2 = Button(window, text='Button2')
button3 = Button(window, text='Button3')

label1.grid(column=0)
label2.grid(column=1)
label3.grid(columnspan=3, sticky='we')
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

window = mainloop()
