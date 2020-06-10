from tkinter import *
root = Tk()
myframe = Frame(root, width=500, height = 400)
myframe.pack()

root.config(bg = "sky blue")
root.resizable(False, False)
root.geometry("500x400")
root.title("another lesson")

myimage = PhotoImage(file = "seed.png")
mylabel = Label(myframe, image= myimage)
mylabel.place(x=1, y=140)

root.mainloop()
