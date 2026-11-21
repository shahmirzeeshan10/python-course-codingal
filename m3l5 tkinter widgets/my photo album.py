from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk
window=Tk()
window.title("my photo album")
window.geometry("400x400")
title=Label(window, text="my photo album",bg="purple",fg="white")
title.pack(pady=10)
img=Image.open("penguin.png")
img=img.resize((250,150))
photo=Imagetk.PhotoImage(img)
pic=Label(window,image=photo)
pic.pack(pady=5)
def show_message():
    messagebox.showinfo("great!","you clicked the photo")
btn1=Button(window,text="click to react",command=show_message)
btn1.pack(pady=5)
window.mainloop()



