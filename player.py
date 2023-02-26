# Player file
import pygame, sys
import os

# player lives and score: 
playerLives = 3
playerScore = 0
playerHighScore = 0

# player movement - rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 10
rectPos = rectX, rectY = 300, 650
rectSpeed = 0.5
gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

# Get player's old highscore (if it exists
try:
    f = open('score.txt','rt')
except IOError as e:
    print('error')
    

