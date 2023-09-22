from cgitb import text
from tkinter import *
import random
from tkinter import simpledialog



def newGame():
    global player, players
    

    player = random.choice(players)

    label.config(text= player + "'s turn", font=('Arial', 25))
    

    for x in range(3):
        for y in range(3):
            buttons[x][y]['text'] = ""
    
    

    
   








def askUsernames():
    global player, players
    firstPlayer = simpledialog.askstring(title="Name of players", prompt="Enter the name of the first player:")
    secondPlayer = simpledialog.askstring(title="Name of players", prompt="Enter the name of the second player:")


    if firstPlayer and secondPlayer is not None:
        players = [firstPlayer, secondPlayer]
        player = random.choice(players)
    else:
        return






window = Tk()

window.title("Tic-tac toe")


Players = None
player = None


window.withdraw()

askUsernames()

window.wm_deiconify()

window.attributes("-topmost", True)
    
buttons = [[0,0,0], [0,0,0],[0,0,0]]

label = Label(text= player + "'s turn", font=('Arial', 25))
label.pack(side= 'top')

resetBtn = Button(text="New game", font=('Arial', 25), command=newGame)
resetBtn.pack(side='bottom')

frame = Frame(window)
frame.pack()




window.mainloop()
