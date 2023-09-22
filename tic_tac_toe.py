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
    
    

    
   

def noEmptySpaces():
    spaces = 9
    for x in range(3):
        for y in range(3):
            if buttons[x][y]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return True
    else:
        return False

def checkWinner():
    
    for x in range(3):
            if (buttons[x][0]['text'] == buttons[x][1]['text'] == buttons[x][2]['text'] != ""):
                return True
    for y in range(3):
            if (buttons[0][y]['text'] == buttons[1][y]['text'] == buttons[2][y]['text'] != ""):
                return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    
    elif noEmptySpaces():
        return "tie"
    else:
        return False

def nextTurn(x, y):
    global player
    
    if ((checkWinner() and buttons[x][y]['text'] == "") is False):

        if (player == players[0]):
            buttons[x][y]['text'] = "x"
            if checkWinner() is False:
                player = players[1]
                label.config(text= f"it's {player}'s turn")
            elif checkWinner() is True:
                label.config(text= f"{player} won the game!!")
            elif checkWinner() == 'tie':
                label.config(text= f"it's a tie")

        elif (player == players[1]):
            buttons[x][y]['text'] = "o"
            if checkWinner() is False:
                player = players[0]
                label.config(text= f"it's {player}'s turn")
            elif checkWinner() is True:
                label.config(text= f"{player} won the game!!")
            elif checkWinner() == 'tie':
                label.config(text= f"it's a tie")


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


for x in range(3):
    for y in range(3):
        buttons[x][y] = Button(frame, text="" , font= ('Arial', 30) , width= 4, height= 2,
                                command= lambda row=x, column=y: nextTurn(row,column) )
        buttons[x][y].grid(row= x, column= y )

window.mainloop()
