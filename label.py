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


label = Label(window,
              text='Label',
              bg='red',
              fg='#CCCCCC',
              font='Arial 20 bold italic',
              width=15,
              height=4,
              borderwidth=2,
              relief='groove',  # solid flat raised sunken ridge groove
              anchor=CENTER  # N S W E NW NE SW SE CENTER
              ).pack()

padding = Label(window,
                text='Padding\nExemplo de Padding\nAlinhamento',
                font='Arial 20',
                bd=1,
                relief='solid',
                padx=50,
                pady=50,
                justify=LEFT,  # RIGHT LEFT CENTER
                anchor=W
                ).pack()

text = StringVar()
text.set('Novo texto')

label2 = Label(window)
label2['textvariable'] = text
label2['font'] = 'Arial 20'
label2.pack()

text.set('textvariable')

window = mainloop()
