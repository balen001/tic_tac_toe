from cgitb import text
from tkinter import *
import random
from tkinter import simpledialog





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



window.mainloop()
