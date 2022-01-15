from tkinter import *
from settings import Settings


def button_click(message):
    print(message)


window = Tk()
window_settings = Settings()
window.title(window_settings.title)
posx = int(window.winfo_screenwidth() / 2 - window_settings.screen_width / 2)
posy = int(window.winfo_screenheight() / 2 - window_settings.screen_height / 2)
window.geometry(
    f'{window_settings.screen_width}x{window_settings.screen_height}+{posx}+{posy}')
window.iconbitmap(window_settings.icon)

button = Button(window,
                text='Button',
                command=lambda: button_click('Trader Link')
                ).pack()

window = mainloop()
