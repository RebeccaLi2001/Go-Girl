import pygame,sys,random,time,os
from pygame import mixer
from pygame.locals import *
from os import path


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


#https://newsroom.tomra.com/the-future-of-the-sea-how-the-ocean-economy-can-fight-plastic-pollution/
backgroundImg=pygame.image.load("background.jpg")
backgroundImg=pygame.transform.scale(backgroundImg, (1000, 500))

#key
#https://www.flaticon.com/free-icon/rec_1783356?term=circle%20dot&page=1&position=5
keyImg=pygame.image.load("key.png")
keyImg=pygame.transform.scale(keyImg, (80, 60))

high_score_file = "highScores.txt"


def background(x,y):
    screen.blit(backgroundImg,(x,y))

def key(x,y):
    screen.blit(keyImg,(x,y))

def pentagram(x,y):
    #image from https://www.flaticon.com/free-icon/stave_125051?term=pentagram&page=1&position=62
    pentagramImg=pygame.image.load("pentagram.png")
    pentagramImg=pygame.transform.scale(pentagramImg, (1000,50))
    screen.blit(pentagramImg,(x,y))

def note(x,y):
    #image from https://www.flaticon.com/free-icon/happy_1747870
    note1Img=pygame.image.load("note1.png")
    note1Img=pygame.transform.scale(note1Img, (30,30))
    screen.blit(note1Img,(x,y))

def bomb1(x,y):
    #image from https://www.flaticon.com/free-icon/bomb_595582?term=bomb&page=1&position=2
    bombImg=pygame.image.load("bomb.png")
    bombImg=pygame.transform.scale(bombImg, (30,30))
    screen.blit(bombImg,(x,y))

def candy1(x,y):
    #image from https://www.flaticon.com/free-icon/bomb_595582?term=bomb&page=1&position=2
    candyImg=pygame.image.load("candy.png")
    candyImg=pygame.transform.scale(candyImg, (30,30))
    screen.blit(candyImg,(x,y))

def candy(x,y):
    #image from https://www.flaticon.com/search?word=candy
    candyImg=pygame.image.load("candy.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    candyImg=pygame.transform.scale(candyImg, size)
    screen.blit(candyImg,(x,y))

def note1(x,y):
    #image from https://www.flaticon.com/free-icon/happy_1747870
    note1Img=pygame.image.load("note1.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    note1Img=pygame.transform.scale(note1Img, size)
    screen.blit(note1Img,(x,y))

def note2(x,y):
    #image from https://www.flaticon.com/free-icon/cute_1747829
    note2Img=pygame.image.load("note2.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    note2Img=pygame.transform.scale(note2Img, size)
    screen.blit(note2Img,(x,y))
     
def note3(x,y):
    #image from https://www.flaticon.com/free-icon/laughing_1747844
    note3Img=pygame.image.load("note3.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    note3Img=pygame.transform.scale(note3Img, size)
    screen.blit(note3Img,(x,y))

def note4(x,y):
    #image from https://www.flaticon.com/free-icon/ninja_1747854
    note4Img=pygame.image.load("note4.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    note4Img=pygame.transform.scale(note4Img, size)
    screen.blit(note4Img,(x,y))

def bomb(x,y):
    #image from https://www.flaticon.com/free-icon/bomb_595582?term=bomb&page=1&position=2
    bombImg=pygame.image.load("bomb.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    bombImg=pygame.transform.scale(bombImg, size)
    screen.blit(bombImg,(x,y))

def ice(x,y):
    #image from https://www.flaticon.com/free-icon/fish_2458233?term=ice&page=1&position=20
    iceImg=pygame.image.load("ice.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    iceImg=pygame.transform.scale(iceImg, size)
    screen.blit(iceImg,(x,y))

def thunder(x,y):
    #image from https://www.flaticon.com/free-icon/bomb_595582?term=bomb&page=1&position=2
    thunderImg=pygame.image.load("thunder.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    thunderImg=pygame.transform.scale(thunderImg, size)
    screen.blit(thunderImg,(x,y))

def candy(x,y):
    #image from https://www.flaticon.com/search?word=candy
    candyImg=pygame.image.load("candy.png")
    if 0<y<1000:
        size = (int(30+y/10),int(30+y/20))
    else:
        size = (30,30)
    candyImg=pygame.transform.scale(candyImg, size)
    screen.blit(candyImg,(x,y))