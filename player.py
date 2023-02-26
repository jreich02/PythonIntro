# Player file
import pygame, sys
import errno
# player lives and score: 
playerLives = 3
playerScore = 0
playerHighScore = 0

# Get player's old highscore (if it exists)
try:
    f = open('score.txt','rt')
