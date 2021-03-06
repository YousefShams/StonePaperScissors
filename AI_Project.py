


from tkinter import *
from PIL import ImageTk
import random





#our default (rgb) colour
bg="#100f1f"

#default font
myFont=("Calibri", 30, "bold")

def fullScreen (event) :
    window.attributes("-fullscreen", True)
def smallScreen (event) :
    window.attributes("-fullscreen", False)

def RestartGame():
    #TODO: implement this function
    pass

def QuitGame():
    #TODO: implement this function
    pass

def getImage (player, choice , winOrLost):
    return ImageTk.PhotoImage(file=f"./images/{player}/{choice+winOrLost}.jpg")




window = Tk()
window.attributes("-fullscreen", True)
window.geometry("1000x800")
window["background"] =bg
window.title("Stone, Paper and Scissors!")

playerScore=0
computerScore=0

#Creating Some Frames
#you can imagine the frame as a box that contains some elements like : (text,images and so on...)

f1 = Frame(background=bg) #1
f2 = Frame(background=bg) #2
f3 = Frame(background=bg) #3
f4 = Frame(background=bg) #3




#Creating Elements for Frame1
gameTitle =Label(f1 ,text="Stone, Paper and Scissors", bg=bg,  fg="white", font=("Cooper Black", 40, "bold"), pady=50)


#Creating Elements for Frame2
compVsPlayerText= Label(f2, text=f"Player  0                         vs               0  Computer", 
                        background=bg , foreground="white", font=myFont, pady=20)

playerImg=getImage("player","stone","win")
computerImg=getImage("computer","stone","win")
playerImage= Label(f2, image=playerImg,width=350, height=250)
computerImage= Label(f2, image=computerImg,width=350,height=250)


#Creating Elements for Frame3
scissorsBtn= Button(f3, text="Scissors", font=myFont, borderwidth = 0, command=lambda: StartGame("scissors"))
stoneBtn= Button(f3, text="Stone", font=myFont, borderwidth = 0, command=lambda: StartGame("stone"))
paperBtn= Button(f3, text="Paper", font=myFont, borderwidth = 0, command=lambda: StartGame("paper"))

#Creating Elements for Frame4
playAgainBtn= Button(f4, text="Play Again?", font=myFont, borderwidth = 0, bg="cyan", command=lambda :RestartGame())
quitBtn= Button(f4, text="Quit", font=myFont, borderwidth = 0, bg="red", command=lambda : QuitGame())


#Adding the frames to the window
f1.pack(fill="x")
f2.pack()
f3.pack()
f4.pack()

#Adding the title to the window
gameTitle.pack()

#Adding some text and the two images of the player and the computer player to the window
compVsPlayerText.pack()
playerImage.pack(side=LEFT, padx=50)
computerImage.pack(side=LEFT)

#Adding the buttons to the window
scissorsBtn.pack(side=LEFT,padx=10,pady=50)
stoneBtn.pack(side=LEFT,padx=10)
paperBtn.pack(side=LEFT,padx=10)
playAgainBtn.pack(side=LEFT,padx=10)
quitBtn.pack(side=LEFT,padx=10)



# bind function on window take two arguments first one is a keyboard key, the second is
# a name of function that gets excuted when that key is pressed
window.bind("<Escape>", smallScreen)
window.bind("<f>", fullScreen)

#mainloop on window makes the window shows up and excutes all tkinter code
window.mainloop()



def StartGame(playerChoice):
    
    choices=["stone","scissors", "paper"]
    #TODO: implement this function
    


def isPlayerScissors(computerChoice):
    #TODO: Implement this function
    #note : you can delete the hint next line, if you can do it yourself
    #hint: if compChoice is paper return -1 (for losing), if scissors return 0 (for a draw), if stone return 1 (for winnig) 
    pass
    
def isPlayerStone(computerChoice):
    #TODO: Implement this function
    pass
    
def isPlayerPaper(computerChoice):
    #TODO: Implement this function 
    pass


def updateImages_ShowScore(playerChoice,computerChoice, score):
    #TODO: update the playerImage and computerImage using .configure() function, you can search for it or ask in the ground if you got stuck
    #increment the playerScore or computerScore denpending on who won, and update the gameTitle text with .configure(), with something like:
    #player win! , computer wins :( or match draw 
    global playerScore, computerScore
