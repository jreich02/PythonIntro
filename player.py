# Player file
import pygame, sys
import os

# player lives and score: 
playerLives = 3
playerScore = 0
playerHighScore = 0

# player movement - rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 15
rectPos = rectX, rectY = 300, 600
rectSpeed = 0.5
gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

# Get player's old highscore (if it exists)
if os.path.getsize('score.txt') == 0:
   playerHighScore = 0
else:
    scores = []
f = open('score.txt')
for line in f.readlines():
    scores.append(int(line))
f.close()

highest = scores[0]
# iterate through score.txt to get highest score saved
for t in scores:
    if t > highest:
        highest = t
playerHighScore = highest
