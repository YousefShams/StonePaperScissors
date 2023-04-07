from tkinter import *
from PIL import ImageTk
import math
import random



fontf="Calibri"
bg="#100f1f"


def fullScreen (event) :
    window.attributes("-fullscreen", True)
def smallScreen (event) :
    window.attributes("-fullscreen", False)

window = Tk()
window.attributes("-fullscreen", True)
window.geometry("1000x800")
window["background"] =bg
window.title("Stone, Paper and Scissors!")

playerScore=0
computerScore=0



#Helper Functions    
def isPlayerScissors(computerChoice):
    if computerChoice=="paper":
        return 1
    elif computerChoice=="stone":
        return -1
    else:
        return 0
    
def isPlayerStone(computerChoice):
    if computerChoice=="paper":
        return -1
    elif computerChoice=="stone":
        return 0
    else:
        return 1
    
def isPlayerPaper(computerChoice):
    if computerChoice=="paper":
        return 0
    elif computerChoice=="stone":
        return 1
    else:
        return -1


def getImage (player, choice , winOrLost):
    return ImageTk.PhotoImage(file=f"./images/{player}/{choice+winOrLost}.jpg")


def updateImages_ShowScore(playerChoice,computerChoice, score):
    
    global playerScore, computerScore
    
    if score==1:
        playerChoiceImage=getImage("player",playerChoice,"win")
        computerChoiceImage=getImage("computer",computerChoice,"lost")
        playerScore+=1
        scoreText="Player Wins!"
    elif score==-1:
        playerChoiceImage=getImage("player",playerChoice,"lost")
        computerChoiceImage=getImage("computer",computerChoice,"win")
        computerScore+=1
        scoreText="Computer Wins :("
    else:
        playerChoiceImage=getImage("player",playerChoice,"win")
        computerChoiceImage=getImage("computer",computerChoice,"win")
        scoreText="Match Draw :|"
    
    
    playerImage.configure(image=playerChoiceImage)
    playerImage.image=playerChoiceImage
    computerImage.configure(image=computerChoiceImage)
    computerImage.image=computerChoiceImage
    gameTitle.configure(text=scoreText, fg="cyan")
    compVsPlayerText.configure(text=f"Player  {playerScore}                          vs               {computerScore}  Computer")

#Main Function
def StartGame(playerChoice):
    
    choices=["stone","scissors", "paper"]
    randomIndex = random.randint(0,2) #function that return random index (0 ,1 or 2 in this case)
    computerChoice=choices[randomIndex]

    
    if playerChoice=="stone":
        score = isPlayerStone(computerChoice)
        updateImages_ShowScore(playerChoice, computerChoice, score)
        
        
    elif playerChoice=="paper":
        score = isPlayerPaper(computerChoice)
        updateImages_ShowScore(playerChoice, computerChoice, score)
        
    else:
        score = isPlayerScissors(computerChoice)
        updateImages_ShowScore(playerChoice, computerChoice, score)

def RestartGame():
    gameTitle.configure(text="Stone, Paper and Scissors", fg="white")
    global playerScore, computerScore
    playerScore=0
    computerScore=0
    compVsPlayerText.configure(text=f"Player  0                         vs                0  Computer")

def QuitGame():
    window.destroy()









#Creating Some Frames
#you can imagine the frame as a box that contains some elements like : (text,images and so on...)

f1 = Frame(background=bg) #1
f2 = Frame(background=bg) #2
f3 = Frame(background=bg) #3
f4 = Frame(background=bg) #3




#Creating Elements for Frame1
gameTitle =Label(f1 ,text="Stone, Paper and Scissors", bg=bg,  fg="white", font=fontf+ " 40 bold", pady=50)


#Creating Elements for Frame2
compVsPlayerText= Label(f2, text=f"Player  0                         vs               0  Computer", 
                        background=bg , foreground="white", font=(fontf, 30, "bold"), pady=20)

playerImg=ImageTk.PhotoImage(file="./images/player/stonewin.jpg")
computerImg=ImageTk.PhotoImage(file="./images/computer/stonewin.jpg")
playerImage= Label(f2, image=playerImg,width=350, height=250)
computerImage= Label(f2, image=computerImg,width=350,height=250)


#Creating Elements for Frame3
scissorsBtn= Button(f3, text="Scissors", font=fontf+ " 30 bold",borderwidth = 0, command=lambda: StartGame("scissors"))
stoneBtn= Button(f3, text="Stone", font=fontf+ " 30 bold",borderwidth = 0,command=lambda: StartGame("stone"))
paperBtn= Button(f3, text="Paper", font=fontf+ " 30 bold",borderwidth = 0, command=lambda: StartGame("paper"))

#Creating Elements for Frame4
playAgainBtn= Button(f4, text="Play Again?", font=fontf+ " 30 bold",borderwidth = 0,bg="cyan", command=lambda :RestartGame())
quitBtn= Button(f4, text="Quit", font=fontf+ " 30 bold",borderwidth = 0, bg="red", command=lambda : QuitGame())


#Adding the frames to the window
f1.pack(fill="x")
f2.pack()
f3.pack()
f4.pack()

#Adding the title to the window
gameTitle.pack()

#Adding the some text and the two images of the player and the computer player to the window
compVsPlayerText.pack()
playerImage.pack(side=LEFT, padx=50)
computerImage.pack(side=LEFT)

#Adding the play buttons to the window
scissorsBtn.pack(side=LEFT,padx=10,pady=50)
stoneBtn.pack(side=LEFT,padx=10)
paperBtn.pack(side=LEFT,padx=10)
playAgainBtn.pack(side=LEFT,padx=10)
quitBtn.pack(side=LEFT,padx=10)




window.bind("<Escape>", smallScreen)
window.bind("<f>", fullScreen)
window.mainloop()


