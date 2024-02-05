from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()

root.title("Dice Game")

Head = Label(root, text="DICE GAME")
Head.pack()
Head.config(font=('Verdana',18))

imgList = ['one.jpg','two.jpg','three.jpg','four.jpg','five.jpg','six.jpg']

root.geometry('300x300')

frame = Frame(root,height=200,width=200)
frame.pack()

photoLabel = Label(frame)
photoLabel.pack(pady=10)


def rollDice():
    Rdice = random.choice(imgList)
    img = Image.open(r"C:\Users\ASUS\Desktop\Python projects\DICEGAME\DiceImg"+"\\"+Rdice)
    resized_img = img.resize((200,200))
    new_img = ImageTk.PhotoImage(resized_img)
    photoLabel.config(image=new_img)
    photoLabel.image=new_img


ROllBtn = Button(root,text='Click to Roll',background='sky blue' ,command=rollDice)
ROllBtn.pack(pady=10)

root.mainloop()