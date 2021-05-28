from tkinter import *
from PIL import Image, ImageTk

root = Tk()

#widthXHeight 
root.geometry('1200x800')

adeeb = Label(text = 'Work under development')
adeeb.pack()

logo = PhotoImage(file="Gitlab.png")
#For JPG
# logo = Image.open("unity.jpg")
# photo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.pack()

root.mainloop()