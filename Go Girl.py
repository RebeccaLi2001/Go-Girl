#################################################
# 15-112 Term Project
# Project name: Rhythm master
# Your name:Yaxuan Li
# Your andrew id:yaxuanl 
#################################################

import pygame,sys,random,time,os
from pygame import mixer
from pygame.locals import *
from os import path
from basic import *

pygame.mixer.init(48100)
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (34,177,76)
orange = (255,165,0)
pink = (255,182,193)
purple = (128,0,128)
yellow = (255,255,0)
violet = (238,130,238)
lime = (0,255,0)
grey = (169,169,169)
gold = (255,215,0)

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Go Girl")

font1=pygame.font.SysFont(None,25)
font2=pygame.font.SysFont(None,50)
font3=pygame.font.SysFont(None,100)

clock = pygame.time.Clock()

#https://newsroom.tomra.com/the-future-of-the-sea-how-the-ocean-economy-can-fight-plastic-pollution/
backgroundImg=pygame.image.load("background.jpg")
backgroundImg=pygame.transform.scale(backgroundImg, (1000, 500))

#key
#https://www.flaticon.com/free-icon/rec_1783356?term=circle%20dot&page=1&position=5
keyImg=pygame.image.load("key.png")
keyImg=pygame.transform.scale(keyImg, (80, 60))

high_score_file = "highScores.txt"

#learn some functions from https://www.youtube.com/watch?v=aRMxsTWHiKs
def login():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                intro = False
        screen.fill(white)
        message("Welcome to Go Girl",violet,-100,"large")
        message("Please log in or sign up for your account",black,10,"small")
        message("You can enter your name and password in the terminal ",black,30,"small")
        player_name = input("Enter your name: ")
        password = input("Password: ")
        
        content = ""
        if os.path.isfile(player_name):
            with open(player_name,"r") as userDoc:
                content = userDoc.read()
                key = content.split("\n")[0][9:]
                while password != key:
                    print("Wrong password!")
                    password = input("Password: ")
                game_intro(player_name)
                    
        else:
            f = open(player_name,"w")
            content = "password:"+password
            high_score_file = "highScores.txt"
            f.write(content)
            f.close()
        game_intro(player_name)
        intro=False
        
        
def game_intro(player_name):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                intro = False
        screen.fill(white)
        message("Welcome to Go Girl",violet,-100,"large")
        message("You can choose to play easy, medium, or hard mode",black,10,"small")
        message("You can also design your own algorithm ",black,30,"small")
        
        location = pygame.mouse.get_pos()
        buttonX1 = 150
        buttonX2 = 450
        buttonX3 = 750
        buttonY = 400
        buttonWidth = 125
        buttonHeight = 50
        click = pygame.mouse.get_pressed()
        if buttonX1<location[0]<buttonX1+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Play",black,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
                chooseDifficulty(player_name)
            pygame.draw.rect(screen,pink,(buttonX1,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX1,buttonY,buttonWidth,buttonHeight))
        if buttonX2<location[0]<buttonX2+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Instruction",black,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
                instruction(player_name)
            pygame.draw.rect(screen,lime,(buttonX2,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,green,(buttonX2,buttonY,buttonWidth,buttonHeight))
        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Quit",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small",action="quit")
            pygame.draw.rect(screen,yellow,(buttonX3,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,orange,(buttonX3,buttonY,buttonWidth,buttonHeight))
        button("Play",black,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
        button("Instruction",black,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
        button("Quit",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")
        pygame.display.update()
        clock.tick(15)

#https://www.youtube.com/watch?v=t3eh6YiyCoQ
def text_objects(text,color,size):
    if size == "small":
        textSurface = font1.render(text, True, color)
    elif size == "medium":
        textSurface = font2.render(text, True, color)
    elif size == "large":
        textSurface = font3.render(text, True, color)
    return textSurface, textSurface.get_rect()


def instruction(player_name):
    instruction = True
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                instruction = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    instruction = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    os._exit(0)
        screen.fill(white)
        message("Instructions",violet,-200,"large")
        message("When the emoji approaches the black button, hit the space",black,-10,"small")
        message("You could control the position of the characer by using left and right button",black,10,"small")
        message("The candy stands for jelly belly, so your score may gain or lose points by tabbing space",black,30,"small")
        message("The bomb will decrease your score by 5",black,50,"small")
        message("The ice will decrease the overall speed",black,70,"small")
        message("You could end the game early by clicking the end button",black,90,"small")
        message("If you want to save your score in the ranking system, click the save button at the top right corner",black,110,"small")
        message("In the multiplayer mode, the user should use a and d to control left and right and hit s when the emoji approaches",black,130,"small")
        location = pygame.mouse.get_pos()
        buttonX = 450
        buttonY = 400
        buttonWidth = 125
        buttonHeight = 50
        click = pygame.mouse.get_pressed()
        if buttonX<location[0]<buttonX+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Back",black,buttonX,buttonY,buttonWidth,buttonHeight,size="small")
                game_intro(player_name)
            pygame.draw.rect(screen,pink,(buttonX,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX,buttonY,buttonWidth,buttonHeight))
        button("Back",black,buttonX,buttonY,buttonWidth,buttonHeight,size="small")
        pygame.display.update()

def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                pause = False
            
        location = pygame.mouse.get_pos()
        buttonX1 = 150
        buttonX2 = 450
        buttonX3 = 750
        buttonY = 400
        buttonWidth = 125
        buttonHeight = 50
        click = pygame.mouse.get_pressed()
        if buttonX1<location[0]<buttonX1+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                pause = False
            pygame.draw.rect(screen,pink,(buttonX1,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX1,buttonY,buttonWidth,buttonHeight))
        if buttonX2<location[0]<buttonX2+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Instruction",black,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
                instruction(player_name)
            pygame.draw.rect(screen,lime,(buttonX2,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,green,(buttonX2,buttonY,buttonWidth,buttonHeight))
        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Quit",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small",action="quit")
            pygame.draw.rect(screen,yellow,(buttonX3,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,orange,(buttonX3,buttonY,buttonWidth,buttonHeight))
        button("Continue",black,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
        button("Instruction",black,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
        button("Quit",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")
        message("You are paused",violet,-100,"large")
        pygame.display.update()

#https://www.youtube.com/watch?v=t3eh6YiyCoQ
def message(message,color,y_displace=0,size="large"):
    textSurf, textRect = text_objects(message,color,size)
    textRect.center = (screen_width/2),(screen_height/2)+y_displace
    screen.blit(textSurf, textRect)

#https://www.youtube.com/watch?v=kmXKFTu_IyQ
def button(message,color,x,y,width,height,size="small",action=None,score=0):
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and action!=None:
        if action == "quit":
            pygame.quit()
            os._exit(0)
        if action == "pause":
            pause()

    textSurf,textRect = text_objects(message,color,size)
    textRect.center = (x+width/2),(y+height/2)
    screen.blit(textSurf, textRect)

def end(player_name,score,score2=0,compete=False):
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                end = False
            
        location = pygame.mouse.get_pos()
        buttonX1 = 150
        buttonX2 = 450
        buttonX3 = 750
        buttonY = 400
        buttonWidth = 125
        buttonHeight = 50
        click = pygame.mouse.get_pressed()
        if buttonX1<location[0]<buttonX1+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Play",black,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
                chooseDifficulty(player_name)
            pygame.draw.rect(screen,pink,(buttonX1,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX1,buttonY,buttonWidth,buttonHeight))
        if buttonX2<location[0]<buttonX2+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Instruction",black,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
                instruction(player_name)
            pygame.draw.rect(screen,lime,(buttonX2,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,green,(buttonX2,buttonY,buttonWidth,buttonHeight))
        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Quit",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small",action="quit")
            pygame.draw.rect(screen,yellow,(buttonX3,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,orange,(buttonX3,buttonY,buttonWidth,buttonHeight))
        button("Play",black,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
        button("Instruction",black,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
        button("Quit",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")
        if compete == True:
            if score>score2:
                message("Female player win!",violet,-100,"large")
            elif score2>score:
                message("Male player win!",violet,-100,"large")
            else:
                message("It's a tie!",violet,-100,"large")
        else:
            message("Your final score: "+str(score),violet,-100,"large")

        buttonX = 850
        buttonY1 = 0
        buttonY2 = 70

        if compete!=True:
            if buttonX<location[0]<buttonX+buttonWidth and buttonY1<location[1]<buttonY1+buttonHeight:
                if click[0]==1:
                    button("Save",white,buttonX,buttonY1,buttonWidth,buttonHeight,size="small",score=score)
                    save(score,player_name)
                pygame.draw.rect(screen,grey,(buttonX,buttonY1,buttonWidth,buttonHeight))
            else:
                pygame.draw.rect(screen,black,(buttonX,buttonY1,buttonWidth,buttonHeight))
            button("Save",white,buttonX,buttonY1,buttonWidth,buttonHeight,size="small",score=score)

        
        pygame.display.update()

def save(score,player_name):
    set_high_score(high_score_file,player_name,score)
    file_name = "highScores.txt"
    draw_set_high_scores(screen,player_name,score,file_name)
    pygame.display.update()

def chooseDifficulty(player_name,design=None):
    begin = True
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                begin = False
        screen.fill(white)
        message("Let's choose the difficulty",violet,-140,"large")
        message("You can also design your own algorithm by clicking the design button",black,-50,"small")
        
        location = pygame.mouse.get_pos()
        buttonX1 = 150
        buttonX2 = 450
        buttonX3 = 750
        buttonX4 = 450
        buttonX5 = 825
        buttonY = 250
        buttonY2 = 350
        buttonWidth = 175
        buttonHeight = 50
        level1 = "easy"
        level2 = "medium"
        level3 = "difficult"
        click = pygame.mouse.get_pressed()
        if buttonX1<location[0]<buttonX1+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                gameLoop(player_name,level1,design)
            pygame.draw.rect(screen,grey,(buttonX1,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX1,buttonY,buttonWidth,buttonHeight))
        if buttonX2<location[0]<buttonX2+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                gameLoop(player_name,level2,design)
            pygame.draw.rect(screen,grey,(buttonX2,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX2,buttonY,buttonWidth,buttonHeight))
        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                gameLoop(player_name,level3,design)
            pygame.draw.rect(screen,grey,(buttonX3,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX3,buttonY,buttonWidth,buttonHeight))

        pygame.display.update()
        button(level1,white,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
        button(level2,white,buttonX2,buttonY,buttonWidth,buttonHeight,size="small")
        button(level3,white,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")
       
        if buttonX5<location[0]<buttonX5+buttonWidth and 0<location[1]<0+buttonHeight:
            if click[0]==1:
                button("Back",black,buttonX5,0,buttonWidth,buttonHeight,size="small")
                game_intro(player_name)
            pygame.draw.rect(screen,pink,(buttonX5,0,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX5,0,buttonWidth,buttonHeight))
        button("Back",black,buttonX5,0,buttonWidth,buttonHeight,size="small")

        if buttonX4<location[0]<buttonX4+buttonWidth and buttonY2<location[1]<buttonY2+buttonHeight:
            if click[0]==1:
                button("Play design",black,buttonX4,buttonY2,buttonWidth,buttonHeight,size="small")
                result=playDesign(player_name)
                gameLoop(player_name,design=result)
            pygame.draw.rect(screen,pink,(buttonX4,buttonY2,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX4,buttonY2,buttonWidth,buttonHeight))
        button("Play design",black,buttonX4,buttonY2,buttonWidth,buttonHeight,size="small")

        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY2<location[1]<buttonY2+buttonHeight:
            if click[0]==1:
                button("Design",black,buttonX3,buttonY2,buttonWidth,buttonHeight,size="small")
                designing(player_name)
            pygame.draw.rect(screen,pink,(buttonX3,buttonY2,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX3,buttonY2,buttonWidth,buttonHeight))
        button("Design",black,buttonX3,buttonY2,buttonWidth,buttonHeight,size="small")
        
        if buttonX1<location[0]<buttonX1+buttonWidth and buttonY2<location[1]<buttonY2+buttonHeight:
            if click[0]==1:
                button("Multiplayer",black,buttonX1,buttonY2,buttonWidth,buttonHeight,size="small")
                chooseModel(player_name)
            pygame.draw.rect(screen,pink,(buttonX1,buttonY2,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX1,buttonY2,buttonWidth,buttonHeight))
        button("Multiplayer",black,buttonX1,buttonY2,buttonWidth,buttonHeight,size="small")
        pygame.display.update()
        clock.tick(15)

def playDesign(player_name):

    design=[]
    song=input("Enter the name of the designed song:")
    f = open(player_name,"r")
    content = f.read()
    content = content+"\n"
    songList=content.split("\n")
    for i in range(len(songList)):
        if song == songList[i][:-1]:
            design=songList[i+1]
    if design==[]:
        print(f'No song named {song}found!')
        result=[[],[],[],[]]
    else: 
        result=eval(design)
    return result


def chooseModel(player_name):
    begin = True
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                begin = False
        screen.fill(white)
        message("Let's choose the model",violet,-140,"large")
        message("You can choose to collaborate or compete",black,-50,"small")
        
        location = pygame.mouse.get_pos()
        buttonX1 = 150
        buttonX2 = 450
        buttonX3 = 750
        buttonX4 = 450
        buttonY = 250
        buttonY2 = 350
        buttonWidth = 175
        buttonHeight = 50
        level1 = "Collaborate"
        level3 = "Compete"
        click = pygame.mouse.get_pressed()
        if buttonX1<location[0]<buttonX1+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                gameLoop(player_name,difficulty='difficult',user=2)
            pygame.draw.rect(screen,grey,(buttonX1,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX1,buttonY,buttonWidth,buttonHeight))
        
        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                gameLoop(player_name,difficulty='difficult',user=2,compete=True)
            pygame.draw.rect(screen,grey,(buttonX3,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX3,buttonY,buttonWidth,buttonHeight))

        pygame.display.update()
        button(level1,white,buttonX1,buttonY,buttonWidth,buttonHeight,size="small")
        button(level3,white,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")
        pygame.display.update()
        clock.tick(15)

def designing(player_name):
    design = True
    pen1X=[]
    pen2X=[]
    pen3X=[]
    pen4X=[]

    item="note"
    while design:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                design = False
        screen.fill(white)
        pen1=75
        pen2=175
        pen3=275
        pen4=375
        pentagram(0,pen1)
        pentagram(0,pen2)
        pentagram(0,pen3)
        pentagram(0,pen4)
        note1(400,10)
        candy1(500,10)
        bomb1(600,10)
        location = pygame.mouse.get_pos()
        buttonX = 450
        buttonX3 = 750
        buttonX2 = 150
        buttonX4 = 875
        buttonY = 450
        buttonY2 = 0
        buttonWidth = 125
        buttonHeight = 50
        click = pygame.mouse.get_pressed()
        if pen1<location[1]<pen1+30:
            if click[0]==1:
                pen1X.append([item,location[0]])
        if pen2<location[1]<pen2+30:
            if click[0]==1:
                pen2X.append([item,location[0]])
        if pen3<location[1]<pen3+30:
            if click[0]==1:
                pen3X.append([item,location[0]])
        if pen4<location[1]<pen4+30:
            if click[0]==1:
                pen4X.append([item,location[0]])
        if 400<location[0]<430 and 0<location[1]<50:
            if click[0]==1:
                item="note"
        if 500<location[0]<530 and 0<location[1]<50:
            if click[0]==1:
                item="candy"
        if 600<location[0]<630 and 0<location[1]<50:
            if click[0]==1:
                item="bomb"
        if buttonX<location[0]<buttonX+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Back",black,buttonX,buttonY,buttonWidth,buttonHeight,size="small")
                chooseDifficulty(player_name)
            pygame.draw.rect(screen,pink,(buttonX,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX,buttonY,buttonWidth,buttonHeight))
        button("Back",black,buttonX,buttonY,buttonWidth,buttonHeight,size="small")

        if buttonX3<location[0]<buttonX3+buttonWidth and buttonY<location[1]<buttonY+buttonHeight:
            if click[0]==1:
                button("Store",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")
                result=store(pen1X,pen2X,pen3X,pen4X,player_name)
                gameLoop(player_name,design=result)
            pygame.draw.rect(screen,pink,(buttonX3,buttonY,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,violet,(buttonX3,buttonY,buttonWidth,buttonHeight))
        button("Store",black,buttonX3,buttonY,buttonWidth,buttonHeight,size="small")

        for i in range(len(pen1X)):
            if pen1X[i][0]=="note":
                note(pen1X[i][1],pen1+10)
            elif pen1X[i][0]=="candy":
                candy1(pen1X[i][1],pen1+10)
            elif pen1X[i][0]=="bomb":
                bomb1(pen1X[i][1],pen1+10)
        for i in range(len(pen2X)):
            if pen2X[i][0]=="note":
                note(pen2X[i][1],pen2+10)
            elif pen2X[i][0]=="candy":
                candy1(pen2X[i][1],pen2+10)
            elif pen2X[i][0]=="bomb":
                bomb1(pen2X[i][1],pen2+10)
        for i in range(len(pen3X)):
            if pen3X[i][0]=="note":
                note(pen3X[i][1],pen3+10)
            elif pen3X[i][0]=="candy":
                candy1(pen3X[i][1],pen3+10)
            elif pen3X[i][0]=="bomb":
                bomb1(pen3X[i][1],pen3+10)
        for i in range(len(pen4X)):
            if pen4X[i][0]=="note":
                note(pen4X[i][1],pen4+10)
            elif pen4X[i][0]=="candy":
                candy1(pen4X[i][1],pen4+10)
            elif pen4X[i][0]=="bomb":
                bomb1(pen4X[i][1],pen4+10)
        
        pygame.display.update()

def store(pen1X,pen2X,pen3X,pen4X,player_name):
    speed=-15
    design=[]
    for elem in pen1X:
        elem[1]*=speed
    for elem in pen2X:
        elem[1]*=speed
    for elem in pen3X:
        elem[1]*=speed
    for elem in pen4X:
        elem[1]*=speed
    design.append(pen1X)
    design.append(pen2X)
    design.append(pen3X)
    design.append(pen4X)

    f = open(player_name,"r")
    content = f.read()
    content = content+"\n"
    nameOfSong=input("Enter the name of your design:")
    for songName in content.split("\n"):
        if nameOfSong == songName[:-1]:
            print("The name has been used. Try another one.")
            nameOfSong=input("Enter the name of your design:")

    f = open(player_name,"w")
    
    f.write(content)
    f.write(nameOfSong+":\n")
    f.write(str(design))
    f.close()
    return design

#https://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html#mergesort
def merge(A, B):
    # beautiful, but impractical for large N
    if ((len(A) == 0) or (len(B) == 0)):
        return A+B
    else:
        if (A[0] < B[0]):
            return [A[0]] + merge(A[1:], B)
        else:
            return [B[0]] + merge(A, B[1:])

#https://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html#mergesort
def mergeSort(L):
    if (len(L) < 2):
        return L
    else:
        # No need for complicated loops- just merge sort each half, then merge!
        mid = len(L)//2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left, right)

def levelGenerator(design):
    levelScore=0
    pen1=design[0]
    pen2=design[1]
    pen3=design[2]
    pen4=design[3]

    for elem in pen1:
        elem[1]=-elem[1]
        elem.append(1)
    for elem in pen2:
        elem[1]=-elem[1]
        elem.append(2)
    for elem in pen3:
        elem[1]=-elem[1]
        elem.append(3)
    for elem in pen4:
        elem[1]=-elem[1]
        elem.append(4)
    left=merge(pen1, pen2)
    right=merge(pen3, pen4)
    result=merge(left, right)
    result.sort(key=lambda value: value[1])
    for i in range(len(result)-1):
        difference=result[i+1][1]-result[i][1]
        if 0<=difference<30:
            levelScore+=90
        elif 30<=difference<70:
            levelScore+=85
        elif 70<=difference<100:
            levelScore+=80
        elif 100<=difference<300:
            levelScore+=70
        else:
            levelScore+=60
        levelScore=levelScore+(10*abs(result[i+1][2]-result[i][2]))
    length=0
    for i in range(len(result)):
        if result[i][0]=="note" or result[i][0]=="candy":
            length+=1
    levelScore/=(len(result)-1)
    output=(levelScore,length)
    return output

def marks(marks,compete=False):
    text = font2.render("Score: "+str(marks),True,lime)
    if compete == True:
        screen.blit(text,(0,450))
    else:
        screen.blit(text,(0,0))

def missed(miss):
    text = font2.render("Missed: "+str(miss),True,lime)
    screen.blit(text,(0,70))

def difficulty(levelScore):
    if levelScore>93:
        difficulty="Difficult"
    elif levelScore>75:
        difficulty="Medium"
    else:
        difficulty="Easy"
    result="Difficulty: "+(difficulty)
    text = font2.render(result,True,lime)
    screen.blit(text,(0,140))

def length(length):
    text = font2.render("Length: "+(length),True,lime)
    screen.blit(text,(0,210))

def gameLoop(player_name,difficulty=None,design=None,user=1,compete=False):

    running = True
    notPowerup = True
    score = 0
    score2 = 0
    accelarator = 10
    sign=""
    letter = None
    takeCandy = False
    note1Y = []
    note2Y = []
    note3Y = []
    note4Y = []
    bomb1Y = []
    bomb2Y = []
    bomb3Y = []
    bomb4Y = []
    candy1Y = []
    candy2Y = []
    candy3Y = []
    candy4Y = []
    ice1Y = []
    ice2Y = []
    ice3Y = []
    ice4Y = []
    column = 1
    playerX = 700
    player2X = 250
    playerY = 420
    playerCell = 150
    miss = 0
    count = 0
    missOther = 0
    frame = 0
    frame2 = 0

    
    #image from https://www.deviantart.com/yourii54/art/Pokemon-Character-1x1-RMXP-290253332
    sheet = pygame.image.load("player1.png")
    #image from https://pokemon3d.net/forum/threads/29/page-3
    sheet2 = pygame.image.load("player2.png") 
    #learn from https://www.youtube.com/watch?v=GR0zoMhpdiM
    whole = []
    for i in range (4):
        cells = []
        for j in range (4):
            width,height = (48,64)
            rect = pygame.Rect(i*width,j*height,width,height)
            image = pygame.Surface(rect.size).convert()
            image.blit(sheet,(0,0),rect)
            alpha = image.get_at((0,0))
            image.set_colorkey(alpha)
            cells.append(image)
        whole.append(cells)

    playerImg = whole[1][3]
    player = playerImg.get_rect()
    movementLeft = False
    movementRight = False
    #learn from https://www.youtube.com/watch?v=GR0zoMhpdiM
    whole2 = []
    for i in range (3):
        cells2 = []
        for j in range (4):
            width,height = (48,64)
            rect2 = pygame.Rect(i*width,j*height,width,height)
            image2 = pygame.Surface(rect2.size).convert()
            image2.blit(sheet2,(0,0),rect2)
            alpha = image2.get_at((0,0))
            image2.set_colorkey(alpha)
            cells2.append(image2)
        whole2.append(cells2)

    player2Img = whole2[0][0]
    player2 = player2Img.get_rect()
    movementLeft2 = False
    movementRight2 = False

    if design == None:
        if difficulty == "easy":
            design=[]
            i=0
            num=[]
            num1=[-100-random.choice([500*i for i in range(1,5)]) for i in range(5)]
            num2=[-300-random.choice([500*i for i in range(5,10)]) for i in range(5)]
            num3=[-500-random.choice([500*i for i in range(1,10)])for i in range(5)]
            num4=[-700-random.choice([500*i for i in range(8,10)])for i in range(5)]
            num.append(num1)
            num.append(num2)
            num.append(num3)
            num.append(num4)
            for i in range(4):
                line=[]
                for elem in num[i]:
                    L=[]
                    L.append('note')
                    L.append(elem)
                    if L not in line:
                        if len(design)!=0:
                            for item in design:
                                if line not in item:
                                    line.append(L)
                line.append(['candy',-500-random.choice([500*i for i in range(1,10)])])
                design.append(line)
                i+=1
            
        elif difficulty == "medium":
            design=[]
            i=0
            num=[]
            num1=[-100+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)]) for i in range(10)]
            num2=[-300+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)]) for i in range(10)]
            num3=[-400+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)])for i in range(10)]
            num4=[-500+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)])for i in range(10)]
            num.append(num1)
            num.append(num2)
            num.append(num3)
            num.append(num4)
            for i in range(4):
                line=[]
                for elem in num[i]:
                    L=[]
                    L.append('note')
                    L.append(elem)
                    if L not in line:
                        line.append(L)
                line.append(['ice',-400+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)])])
                line.append(['bomb',-400+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)])])
                line.append(['candy',-500+random.choice([-7*i for i in range(1,10)])*random.choice([15*i for i in range(1,10)])])
                design.append(line)
                i+=1

        elif difficulty == "difficult":
            design=[]
            i=0
            num=[]
            num1=[-100+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)]) for i in range(30)]
            num2=[-130+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)]) for i in range(30)]
            num3=[-120+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)]) for i in range(30)]
            num4=[-100+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)]) for i in range(30)]
            num.append(num1)
            num.append(num2)
            num.append(num3)
            num.append(num4)
            for i in range(4):
                line=[]  
                for elem in num[i]:
                    L=[]
                    L.append('note')
                    L.append(elem)
                    if L not in line:
                        line.append(L)
                line.append(['ice',-100+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)])])
                line.append(['bomb',-100+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)])])
                line.append(['candy',-120+random.choice([-5*i for i in range(7)])*random.choice([10*i for i in range(10)])])
                design.append(line)
                i+=1
            random.shuffle(design)
    
    for i in range (len(design[0])):
        if design[0][i][0] == "note":
            note1Y.append(design[0][i][1])
        if design[0][i][0] == "bomb":
            bomb1Y.append(design[0][i][1])
        if design[0][i][0] == "candy":
            candy1Y.append(design[0][i][1])
        if design[0][i][0] == "ice":
            ice1Y.append(design[0][i][1])

    note1X = [i for i in range (len(note1Y))]
    bomb1X = [i for i in range (len(bomb1Y))]
    candy1X = [i for i in range (len(candy1Y))]
    ice1X = [i for i in range (len(ice1Y))]

    for i in range (len(design[1])):
        if design[1][i][0] == "note":
            note2Y.append(design[1][i][1])
        if design[1][i][0] == "bomb":
            bomb2Y.append(design[1][i][1])
        if design[1][i][0] == "candy":
            candy2Y.append(design[1][i][1])
        if design[1][i][0] == "ice":
            ice2Y.append(design[1][i][1])

    note2X = [i for i in range (len(note2Y))]
    bomb2X = [i for i in range (len(bomb2Y))]
    candy2X = [i for i in range (len(candy2Y))]
    ice2X = [i for i in range (len(ice2Y))]

    for i in range (len(design[2])):
        if design[2][i][0] == "note":
            note3Y.append(design[2][i][1])
        if design[2][i][0] == "bomb":
            bomb3Y.append(design[2][i][1])
        if design[2][i][0] == "candy":
            candy3Y.append(design[2][i][1])
        if design[2][i][0] == "ice":
            ice3Y.append(design[2][i][1])

    note3X = [i for i in range (len(note3Y))]
    bomb3X = [i for i in range (len(bomb3Y))]
    candy3X = [i for i in range (len(candy3Y))]
    ice3X = [i for i in range (len(ice3Y))]

    for i in range (len(design[3])):
        if design[3][i][0] == "note":
            note4Y.append(design[3][i][1])
        if design[3][i][0] == "bomb":
            bomb4Y.append(design[3][i][1])
        if design[3][i][0] == "candy":
            candy4Y.append(design[3][i][1])
        if design[3][i][0] == "ice":
            ice4Y.append(design[3][i][1])

    note4X = [i for i in range (len(note4Y))]
    bomb4X = [i for i in range (len(bomb4Y))]
    candy4X = [i for i in range (len(candy4Y))]
    ice4X = [i for i in range (len(ice4Y))]

    levelScore,number=levelGenerator(design)

    if levelScore>93:
        difficulty="Difficult"
    elif levelScore>82:
        difficulty="Medium"
    else:
        difficulty="Easy"
    levelText = font2.render("Difficulty: "+difficulty,True,lime)
    if 0<=number<20:
        length="Short"
    elif 20<=number<50:
        length="Medium"
    else:
        length="Long"
    lengthText = font2.render("Length: "+length,True,lime)
    
    while running:
        background(0,0)
        for i in range(len(note1X)):
            note1Y[i]+=accelarator
            note1X[i]=-note1Y[i]/2.9+400
        for i in range(len(bomb1X)):
            bomb1Y[i]+=accelarator
            bomb1X[i]=-bomb1Y[i]/2.9+400
        for i in range(len(candy1X)):
            candy1Y[i]+=accelarator
            candy1X[i]=-candy1Y[i]/2.9+400
        for i in range(len(ice1X)):
            ice1Y[i]+=accelarator
            ice1X[i]=-ice1Y[i]/2.9+400

        for i in range(len(note2X)):
            note2Y[i]+=accelarator
            note2X[i]=-note2Y[i]/9+450
        for i in range(len(bomb2X)):
            bomb2Y[i]+=accelarator
            bomb2X[i]=-bomb2Y[i]/9+450
        for i in range(len(candy2X)):
            candy2Y[i]+=accelarator
            candy2X[i]=-candy2Y[i]/9+450
        for i in range(len(ice2X)):
            ice2Y[i]+=accelarator
            ice2X[i]=-ice2Y[i]/9+450

        for i in range(len(note3X)):
            note3Y[i]+=accelarator
            note3X[i]=note3Y[i]/9+500
        for i in range(len(bomb3X)):
            bomb3Y[i]+=accelarator
            bomb3X[i]=bomb3Y[i]/9+500
        for i in range(len(candy3X)):
            candy3Y[i]+=accelarator
            candy3X[i]=candy3Y[i]/9+500
        for i in range(len(ice3X)):
            ice3Y[i]+=accelarator
            ice3X[i]=ice3Y[i]/9+500

        for i in range(len(note4X)):
            note4Y[i]+=accelarator
            note4X[i]=note4Y[i]/2.9+570
        for i in range(len(bomb4X)):
            bomb4Y[i]+=accelarator
            bomb4X[i]=bomb4Y[i]/2.9+570
        for i in range(len(candy4X)):
            candy4Y[i]+=accelarator
            candy4X[i]=candy4Y[i]/2.9+570
        for i in range(len(ice4X)):
            ice4Y[i]+=accelarator
            ice4X[i]=ice4Y[i]/2.9+570
        
        location = pygame.mouse.get_pos()
        buttonX = 850
        buttonY1 = 0
        buttonY2 = 70
        buttonWidth = 125
        buttonHeight = 50
        click = pygame.mouse.get_pressed()
        if buttonX<location[0]<buttonX+buttonWidth and buttonY1<location[1]<buttonY1+buttonHeight:
            if click[0]==1:
                button("Pause",white,buttonX,buttonY1,buttonWidth,buttonHeight,size="small",action="pause")
            pygame.draw.rect(screen,grey,(buttonX,buttonY1,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX,buttonY1,buttonWidth,buttonHeight))
        button("Pause",white,buttonX,buttonY1,buttonWidth,buttonHeight,size="small")
        if buttonX<location[0]<buttonX+buttonWidth and buttonY2<location[1]<buttonY2+buttonHeight:
            if click[0]==1:
                button("End",white,buttonX,buttonY2,buttonWidth,buttonHeight,size="small")
                end(player_name,score,score2,compete)
            pygame.draw.rect(screen,grey,(buttonX,buttonY2,buttonWidth,buttonHeight))
        else:
            pygame.draw.rect(screen,black,(buttonX,buttonY2,buttonWidth,buttonHeight))
        button("End",white,buttonX,buttonY2,buttonWidth,buttonHeight,size="small")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if playerX<=550:
                        playerX += playerCell
                if event.key == pygame.K_LEFT:
                    if playerX>250:
                        playerX -= playerCell
                if user == 2:
                    if event.key == pygame.K_d:
                        if player2X<=550:
                            player2X += playerCell
                    if event.key == pygame.K_a:
                        if player2X>250:
                            player2X -= playerCell
                
                if event.key == pygame.K_SPACE:
                    for i in range (len(ice1X)): 
                        if playerY-30<ice1Y[i]< 30+playerY and playerX-30<ice1X[i]< 30+playerX:
                            count+=1
                            ice1Y[i]=1000
                            accelarator-=2
                    for i in range (len(ice2X)): 
                        if playerY-30<ice2Y[i]< 30+playerY and playerX-30<ice2X[i]< 30+playerX:
                            count+=1
                            ice2Y[i]=1000
                            accelarator-=2
                    for i in range (len(ice3X)): 
                        if playerY-30<ice3Y[i]< 30+playerY and playerX-30<ice3X[i]< 30+playerX:
                            count+=1
                            ice3Y[i]=1000
                            accelarator-=2
                    for i in range (len(ice4X)): 
                        if playerY-30<ice4Y[i]< 30+playerY and playerX-30<ice4X[i]< 30+playerX:
                            count+=1
                            ice4Y[i]=1000
                            accelarator-=2
                    
                    for i in range (len(bomb1X)): 
                        if playerY-30<bomb1Y[i]< 30+playerY and playerX-30<bomb1X[i]< 30+playerX:
                            count+=1
                            bomb1Y[i]=1000
                            score-=5
                    for i in range (len(bomb2X)): 
                        if playerY-30<bomb2Y[i]< 30+playerY and playerX-30<bomb2X[i]< 30+playerX:
                            count+=1
                            bomb2Y[i]=1000
                            score-=5
                    for i in range (len(bomb3X)): 
                        if playerY-30<bomb3Y[i]< 30+playerY and playerX-30<bomb3X[i]< 30+playerX:
                            count+=1
                            bomb3Y[i]=1000
                            score-=5
                    for i in range (len(bomb4X)): 
                        if playerY-30<bomb4Y[i]< 30+playerY and playerX-30<bomb4X[i]< 30+playerX:
                            count+=1
                            bomb4Y[i]=1000
                            score-=5

                    for i in range (len(note1X)): 
                        if playerY-30<note1Y[i]< 30+playerY and playerX-30<note1X[i]< 30+playerX:
                            count+=1
                            note1Y[i]=1000
                            score+=1
                    for i in range (len(note2X)): 
                        if playerY-30<note2Y[i]< 30+playerY and playerX-30<note2X[i]< 30+playerX:
                            count+=1
                            note2Y[i]=1000
                            score+=1
                    for i in range (len(note3X)): 
                        if playerY-30<note3Y[i]< 30+playerY and playerX-30<note3X[i]< 30+playerX:
                            count+=1
                            note3Y[i]=1000
                            score+=1
                    for i in range (len(note4X)): 
                        if playerY-30<note4Y[i]< 30+playerY and playerX-30<note4X[i]< 30+playerX:
                            count+=1
                            note4Y[i]=1000
                            score+=1
                    for i in range (len(candy1X)): 
                        if playerY-30<candy1Y[i]< 30+playerY and playerX-30<candy1X[i]< 30+playerX:
                            count+=1
                            candy1Y[i]=1000
                            score+=random.choice([-2,3,-4,5])
                    for i in range (len(candy2X)): 
                        if playerY-30<candy2Y[i]< 30+playerY and playerX-30<candy2X[i]< 30+playerX:
                            count+=1
                            candy2Y[i]=1000
                            score+=random.choice([-2,3,-4,5])
                    for i in range (len(candy3X)): 
                        if playerY-30<candy3Y[i]< 30+playerY and playerX-30<candy3X[i]< 30+playerX:
                            count+=1
                            candy3Y[i]=1000
                            score+=random.choice([-2,3,-4,5])
                    for i in range (len(candy4X)): 
                        if playerY-30<candy4Y[i]< 30+playerY and playerX-30<candy4X[i]< 30+playerX:
                            count+=1
                            candy4Y[i]=1000
                            score+=random.choice([-2,3,-4,5])     
                    
                    

                if event.key == pygame.K_s:
                    if user == 2:
                        for i in range (len(note1X)): 
                            if playerY-30<note1Y[i]< 30+playerY and player2X-30<note1X[i]< 30+player2X:
                                count+=1
                                note1Y[i]=1000
                                if compete == True:
                                    score2+=1
                                else:
                                    score+=1
                        for i in range (len(note2X)): 
                            if playerY-30<note2Y[i]< 30+playerY and player2X-30<note2X[i]< 30+player2X:
                                count+=1
                                note2Y[i]=1000
                                if compete == True:
                                    score2+=1
                                else:
                                    score+=1
                        for i in range (len(note3X)): 
                            if playerY-30<note3Y[i]< 30+playerY and player2X-30<note3X[i]< 30+player2X:
                                count+=1
                                note3Y[i]=1000
                                if compete == True:
                                    score2+=1
                                else:
                                    score+=1
                        for i in range (len(note4X)): 
                            if playerY-30<note4Y[i]< 30+playerY and player2X-30<note4X[i]< 30+player2X:
                                count+=1
                                note4Y[i]=1000
                                if compete == True:
                                    score2+=1
                                else:
                                    score+=1
                        for i in range (len(candy1X)): 
                            if playerY-30<candy1Y[i]< 30+playerY and player2X-30<candy1X[i]< 30+player2X:
                                count+=1
                                candy1Y[i]=1000
                                if compete == True:
                                    score2+=random.choice([-2,3,-4,5])
                                else:
                                    score+=random.choice([-2,3,-4,5])
                        for i in range (len(candy2X)): 
                            if playerY-30<candy2Y[i]< 30+playerY and player2X-30<candy2X[i]< 30+player2X:
                                count+=1
                                candy2Y[i]=1000
                                if compete == True:
                                    score2+=random.choice([-2,3,-4,5])
                                else:
                                    score+=random.choice([-2,3,-4,5])
                        for i in range (len(candy3X)): 
                            if playerY-30<candy3Y[i]< 30+playerY and player2X-30<candy3X[i]< 30+player2X:
                                count+=1
                                candy3Y[i]=1000
                                if compete == True:
                                    score2+=random.choice([-2,3,-4,5])
                                else:
                                    score+=random.choice([-2,3,-4,5])
                        for i in range (len(candy4X)): 
                            if playerY-30<candy4Y[i]< 30+playerY and player2X-30<candy4X[i]< 30+player2X:
                                count+=1
                                candy4Y[i]=1000
                                if compete == True:
                                    score2+=random.choice([-2,3,-4,5])
                                else:
                                    score+=random.choice([-2,3,-4,5])
                        for i in range (len(bomb1X)): 
                            if playerY-50<bomb1Y[i]< 30+playerY and player2X-50<bomb1Y[i]< 30+player2X:
                                count+=1
                                bomb1Y[i]=1000
                                if compete == True:
                                    score2-=5
                                else:
                                    score-=5
                        for i in range (len(bomb2X)): 
                            if playerY-50<bomb2Y[i]< 30+playerY and player2X-50<bomb2Y[i]< 30+player2X:
                                count+=1
                                bomb2Y[i]=1000
                                if compete == True:
                                    score2-=5
                                else:
                                    score-=5
                        for i in range (len(bomb3Y)): 
                            if playerY-50<bomb3Y[i]< 30+playerY and player2X-50<bomb3Y[i]< 30+player2X:
                                count+=1
                                bomb3Y[i]=1000
                                if compete == True:
                                    score2-=5
                                else:
                                    score-=5
                        for i in range (len(bomb4X)): 
                            if playerY-50<bomb4X[i]< 30+playerY and player2X-50<bomb4X[i]< 30+player2X:
                                count+=1
                                bomb4X[i]=1000
                                if compete == True:
                                    score2-=5
                                else:
                                    score-=5

        # partially learn from https://www.youtube.com/watch?v=GR0zoMhpdiM
        playerImg = whole[frame][3]
        frame += 1
        if frame >= len(whole):
            frame = 1
            
        if movementLeft:
            playerImg = whole[frame][1]
            frame += 1
            if frame >= 3:
                movementLeft = False
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]!=0:
                movementLeft = True
                frame = 1
                
            
        if movementRight:
            playerImg = whole[frame][2]
            frame += 1
            if frame >= 3:
                movementRight = False
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]!=0:
                movementRight = True
                frame = 1

        player2Img = whole2[frame2][0]
        frame2 += 1
        if frame2 >= 2:
            frame2 = 0
            
        if movementLeft2:
            player2Img = whole2[frame2][1]
            frame2 += 1
            if frame2 >= 2:
                movementLeft2 = False
                frame2 = 0
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]!=0:
                movementLeft2 = True
                frame2 = 0
                
            
        if movementRight2:
            player2Img = whole2[frame2][3]
            frame2 += 1
            if frame2 >= 2:
                movementRight2 = False
                frame2 = 0
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]!=0:
                movementRight2 = True
                frame2 = 0

        pygame.draw.polygon(screen,black,((400,0),(450,0),(330,500),(160,500)))
        pygame.draw.polygon(screen,grey,((450,0),(500,0),(500,500),(330,500)))
        pygame.draw.polygon(screen,black,((500,0),(550,0),(670,500),(500,500)))
        pygame.draw.polygon(screen,grey,((550,0),(600,0),(850,500),(670,500)))
        keyX=[235,385,535,685]
        keyY=420
        
        for i in range(len(keyX)):
            key(keyX[i],keyY)
        for i in range(len(note1X)):
            if 500<note1Y[i]<550:
                miss+=1
                note1Y[i]=1000
            note1(note1X[i],note1Y[i])
        for i in range(len(note2X)):
            if 500<note2Y[i]<550:
                miss+=1
                note2Y[i]=1000
            note2(note2X[i],note2Y[i])
        for i in range(len(note3X)):
            if 500<note3Y[i]<550:
                miss+=1
                note3Y[i]=1000
            note3(note3X[i],note3Y[i])
        for i in range(len(note4X)):
            if 500<note4Y[i]<550:
                miss+=1
                note4Y[i]=1000
            note4(note4X[i],note4Y[i])
        for i in range(len(bomb1X)):
            if 500<bomb1Y[i]<550:
                missOther+=1
                bomb1Y[i]=1000
            bomb(bomb1X[i],bomb1Y[i])
        for i in range(len(bomb2X)):
            if 500<bomb2Y[i]<550:
                missOther+=1
                bomb2Y[i]=1000
            bomb(bomb2X[i],bomb2Y[i])
        for i in range(len(bomb3X)):
            if 500<bomb3Y[i]<550:
                missOther+=1
                bomb3Y[i]=1000
            bomb(bomb3X[i],bomb3Y[i])
        for i in range(len(bomb4X)):
            if 500<bomb4Y[i]<550:
                missOther+=1
                bomb4Y[i]=1000
            bomb(bomb4X[i],bomb4Y[i])
        for i in range(len(candy1X)):
            if 500<candy1Y[i]<550:
                missOther+=1
                candy1Y[i]=1000
            candy(candy1X[i],candy1Y[i])
        for i in range(len(candy2X)):
            if 500<candy2Y[i]<550:
                missOther+=1
                candy2Y[i]=1000
            candy(candy2X[i],candy2Y[i])
        for i in range(len(candy3X)):
            if 500<candy3Y[i]<550:
                missOther+=1
                candy3Y[i]=1000
            candy(candy3X[i],candy3Y[i])
        for i in range(len(candy4X)):
            if 500<candy4Y[i]<550:
                missOther+=1
                candy4Y[i]=1000
            candy(candy4X[i],candy4Y[i])
        for i in range(len(ice1X)):
            if 500<ice1Y[i]<550:
                missOther+=1
                ice1Y[i]=1000
            ice(ice1X[i],ice1Y[i])
        for i in range(len(ice2X)):
            if 500<ice2Y[i]<550:
                missOther+=1
                ice2Y[i]=1000
            ice(ice2X[i],ice2Y[i])
        for i in range(len(ice3X)):
            if 500<ice3Y[i]<550:
                missOther+=1
                ice3Y[i]=1000
            ice(ice3X[i],ice3Y[i])
        for i in range(len(ice4X)):
            if 500<ice4Y[i]<550:
                missOther+=1
                ice4Y[i]=1000
            ice(ice4X[i],ice4Y[i])
        #if miss>=5:
            #end(player_name,score)
        if score>30:
            accelarator = 15
        if score>50:
            accelarator = 20
        if count+miss+missOther == number:
            end(player_name,score,score2,compete)
        if user ==2:
            screen.blit(player2Img,(player2X,playerY))
        marks(score)
        if compete == True:
            marks(score2,compete)
        missed(miss)
        screen.blit(levelText,(0,140))
        screen.blit(lengthText,(0,210))
        screen.blit(playerImg,(playerX,playerY))
        pygame.display.update()
        clock.tick(100)

#https://www.youtube.com/watch?v=XVLiE6R1NPk
def get_high_scores(file_name):
    content = ""
    if os.path.isfile(file_name):
        with open(file_name,"r") as content_file:
            content = content_file.read()
    else:
        f = open(file_name,"w")
        content = "high:player1:0,mid:player2:0,low:player3:0"
        f.write(content)
        f.close()
    content_list = content.split(",")
    to_return = {}
    for element in content_list:
        variable = element.split(":")
        to_return[variable[0]]=[variable[1],variable[2]]
    return to_return

#https://www.youtube.com/watch?v=XVLiE6R1NPk
def write_high_scores(file_name,scores):
    f = open(file_name,"w")
    to_write = ""
    for name in ("high","mid","low"):
        to_write += name
        to_write += ":"
        to_write += str(scores.get(name)[0])
        to_write += ":"
        to_write += str(scores.get(name)[1])
        to_write += ","

    to_write = to_write[:-1]
    f.write(to_write)
    f.close()

#https://www.youtube.com/watch?v=XVLiE6R1NPk
def set_high_score(file_name,player_name,score):
    scores = get_high_scores(file_name)
    if int(score)>=int(scores.get("high")[1]):
        scores["low"][0] = scores["mid"][0]
        scores["low"][1] = scores["mid"][1]
        scores["mid"][0] = scores["high"][0]
        scores["mid"][1] = scores["high"][1]
        scores["high"][0] = player_name
        scores["high"][1] = score
    elif int(score)>=int(scores.get("mid")[1]):
        scores["low"][0] = scores["mid"][0]
        scores["low"][1] = scores["mid"][1]
        scores["mid"][0] = player_name
        scores["mid"][1] = score
    elif int(score)>=int(scores.get("low")[1]):
        scores["low"][0] = player_name
        scores["low"][1] = score
    write_high_scores(file_name,scores)

#https://www.youtube.com/watch?v=XVLiE6R1NPk
def draw_set_high_scores(screen,player_name,high_score,file_name):
    scores = get_high_scores(file_name)
    #text1 = font2.render("Save Your Score of"+str(high_score),True,black)
    #screen.blit(text1,(200,100))
    text2 = font2.render("Congratulations!! ",True,white)
    screen.blit(text2,(200,200))
    score1 = font2.render("1st: "+scores.get("high")[0]+'--'+scores.get("high")[1],True,white)
    screen.blit(score1,(200,250))
    score1 = font2.render("2nd: "+scores.get("mid")[0]+'--'+scores.get("mid")[1],True,white)
    screen.blit(score1,(200,300))
    score1 = font2.render("3rd: "+scores.get("low")[0]+'-'+scores.get("low")[1],True,white)
    screen.blit(score1,(200,350))

login() 