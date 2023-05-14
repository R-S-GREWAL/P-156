from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Pokemon Game")
root.geometry("600x600")
root.configure(background = "gray29")

img = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1 = Label(root, text = "Player 1", font = ("Comic Sans MS", 25), bg = "cadet blue", fg = "gray7")
player1.place(relx = 0.2, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2",  font = ("Comic Sans MS", 25), bg = "cadet blue", fg = "gray7")
player2.place(relx = 0.8, rely = 0.3, anchor = CENTER)

player1score = Label(root, bg = "medium purple", fg = "black")
player1score.place(relx = 0.2, rely = 0.5, anchor = CENTER)

player2score = Label(root, bg = "medium purple", fg = "black")
player2score.place(relx = 0.8, rely = 0.5, anchor = CENTER)



root.mainloop()