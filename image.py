from tkinter import *
from PIL import ImageTk, Image


window = Tk()
window.title('Image')

image_png = PhotoImage(file='images/traderlink.png')

path = 'images/traderlink.jpeg'
image_jpg = ImageTk.PhotoImage(Image.open(path))

img_png = Label(window, image=image_png).pack()
img_jpg = Label(window, image=image_jpg).pack()

window = mainloop()
