#########################################
# Programmer: Ben Sadeh
# Date: November 8, 2021
# File Name: popTheBalloon.py
# Description: Pop the balloons as they float up the the top of the screen.
#########################################

import pygame
pygame.init()
from time import sleep

from math import sqrt
from random import randint, choice

HEIGHT = 600
WIDTH  = 800
surface =pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)                   
BLACK = (  0,  0,  0)
outline=0

backgroundPic=pygame.image.load("Images/birthday.jpg")
backgroundPic=pygame.transform.scale(backgroundPic,(800,600))
bakgroundPic=backgroundPic.convert_alpha()

balloon1=pygame.image.load("Images/blueBalloon.png")
balloon2=pygame.image.load("Images/redBalloon.png")
balloon3=pygame.image.load("Images/greenBalloon.png")
balloons=[balloon1,balloon2,balloon3]


font = pygame.font.SysFont("Ariel Black",60)
textX, textY = 0,0                       

counter=0
textX1,textY1=WIDTH/2,0

textX2,textY2=WIDTH/2 - 250,HEIGHT/2

flownAway=0

numBaloons=20


#-------------------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#------------------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2) 

#------------------------------------------------#
# function that redraws all objects     #
#------------------------------------------------#
def redraw():
    surface.blit(backgroundPic,(0,0))
    for i in range(numBaloons):
        if visible[i]:
            surface.blit(balloonCLR[i],(balloonX[i],balloonY[i]))
    text = font.render("Timer: "+str(time), 1, BLACK)
    surface.blit(text,(textX, textY))
    text1 = font.render("Counter: "+str(counter), 1, BLACK)
    surface.blit(text1,(textX1, textY1))
    pygame.display.update()
       
#--------------------------------------------------#
# the main program begins here          #
#--------------------------------------------------#
exitFlag = False
visible=[True]*numBaloons
balloonX=[0]*numBaloons
balloonY=[0]*numBaloons
balloonR=[0]*numBaloons
balloonSPEED=[0]*numBaloons
balloonCLR=[0]*numBaloons
WHITE=255,255,255


# initialize the coordinates and the size of the balloon
for i in range(numBaloons):
    balloonR[i] = randint(60,100) 
    balloonX[i] = randint(0, WIDTH-balloonR[i])                  
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonSPEED[i] = randint(1,5)
    balloon=choice(balloons)
    balloon=pygame.transform.scale(balloon,(balloonR[i],balloonR[i]))
    balloonCLR[i] = balloon



while not exitFlag:                    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:   
            exitFlag = True 

        if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY) = pygame.mouse.get_pos()
            
            for i in range(numBaloons):
                if distance(cursorX, cursorY, balloonX[i]+balloonR[i], balloonY[i]+balloonR[i])< balloonR[i] and visible[i]:
                    visible[i]=False
                    counter+=1
                    
                    
            
                
    for i in range(numBaloons):
        if visible[i]:
            balloonY[i] = balloonY[i] - balloonSPEED[i]

    time=pygame.time.get_ticks()//1000

    for i in range(numBaloons):
        if visible[i] and balloonY[i]<=0:
            flownAway+=1
            visible[i]=False

    if flownAway+counter==numBaloons:
        exitFlag=True
       
    redraw()
    pygame.time.delay(20)

text2 = font.render("GAME OVER", 1, BLACK)
surface.blit(text2,(textX2+100, textY2-100))
balloonsPopped=font.render("Balloons Popped: "+str(counter), 1, BLACK)
surface.blit(balloonsPopped,(textX2+50, textY2+50))
pygame.display.update()
sleep(30)
    

pygame.quit()
