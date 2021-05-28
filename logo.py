#learning to attach JPG file 
from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.geometry('450x300')

root.minsize(200,200)
root.maxsize(460,320)

 
my_text = Label(text="Unity Engine\n Unleash the Power")
my_text.pack()

#adding JPG file
logo = Image.open("Unity1.jpg")
photo = ImageTk.PhotoImage(logo)

photo_label = Label(image=photo)
photo_label.pack()
root.mainloop()

