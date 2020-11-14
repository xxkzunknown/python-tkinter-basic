from tkinter import *
import tkinter

app = tkinter.Tk()
app.title("Script by Mowgli")
label_welcome = tkinter.Label(app, text="Redd le pd")
app.geometry("640x480")

def fermerfenetre():
    exit()

label_welcome.pack()

btn = tkinter.Button(app, text="Fermer la fenêtre", command=fermerfenetre)
btn.place(x=0, y=0)

print(label_welcome.cget("text"))

app.configure(bg='red')
app.resizable(width=False, height=False)
app.mainloop()