
import pygame, sys
import random
import math

# Initialize game
pygame.init()

# import from files
from player import *
from pong import *
from borders import *
from text import *


# Controller - (Part 1 of 2)
# move player
def move_rect(gameRect):
    gameRect.update(rectX, rectY, rectWidth, rectHeight)

#move pong 
def move_pong(gamePong, pongX, pongY):
    gamePong.update(pongX, pongY, pongWidth, pongHeight)
    
    
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    # Controller - (Part 2 of 2)
    # Get and check keyboard input -> Allow player to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gameRect.x > 25:
        rectX -= rectSpeed
    elif keys[pygame.K_RIGHT] and gameRect.x < (SCREEN_WIDTH - rectWidth - 25):
        rectX += rectSpeed
    move_rect(gameRect)
    
    # Allow pong to move
    pongX+=pongXspeed
    pongY+=pongYspeed
    move_pong(gamePong, pongX, pongY)
    
        
    # Collision Detection
    
    # Collision - if pong collides with player rect
    collidePlayer = pygame.Rect.colliderect(gameRect, gamePong)
    if collidePlayer and pongY < rectY:
        # increase player score on collide
        if playerLives > 0 and pongY < rectY:
            playerScore = playerScore + 1
          
        if playerScore % 10 == 0:
            pongSpeed = pongSpeed + (playerScore // 10) * 0.1
            rectSpeed = rectSpeed + (playerScore // 10) * 0.1

        randspeed = random.uniform(pongSpeed/5, pongSpeed) * 0.95
        if pongXspeed >= 0:
            pongXspeed = randspeed
        if pongXspeed < 0:
            pongXspeed = -randspeed
        pongYspeed = math.sqrt(pongSpeed**2 - pongXspeed**2)
        #self.speed_change()
        pongYspeed *= -1
       
    # Collision - if pong collides with display ceiling
    collideCeiling = pygame.Rect.colliderect(gameCeiling, gamePong)
    if collideCeiling:
        #self.speed_change()
        pongYspeed*=-1
        
    # Collision - if pong collides with side borders
    collideLeftSide = pygame.Rect.colliderect(leftSide, gamePong)
    collideRightSide = pygame.Rect.colliderect(rightSide, gamePong)
    if collideLeftSide or collideRightSide:
        #self.speed_change()
        pongXspeed*=-1
    
    # Collision - if pong collides with floor
    collideFloor = pygame.Rect.colliderect(gameFloor, gamePong)
    if collideFloor:
        rePong = 1
        if(playerLives != 0):
            pongYspeed*=-1
            pongX = 100
            pongY = 100
            pongXspeed = 0.2
            pongYspeed = 0.5
            gamePong.update(pongX, pongY, pongWidth, pongHeight)
            playerLives = playerLives - 1
            
    # Game View
    # Rules of View
    # restrict - player rect to display
    gameRect.clamp_ip(surface.get_rect())
    # restrict - pong to display (while in play)
    gamePong.clamp_ip(surface.get_rect())
    
    # Populate View: 
    # draw background
    surface.fill(screenColor)
    
    # draw - text
    text = font.render('Lives: ' + str(playerLives) + ' Score: ' + str(playerScore) + ' High Score: ' + str(playerHighScore), True, textColor, textBackgroundColor)
    if(playerHighScore < playerScore):
        playerHighScore = playerScore
    surface.blit(text, gameText)
    
    # draw - player
    pygame.draw.rect(surface, rectColor, gameRect)
    
    # draw - pong
    pygame.draw.rect(surface, pongColor, gamePong)
    #if(rePong == 1):
        #pygame.draw.rect(surface, pongColor,gamePong)
    
    # draw - ceiling
    pygame.draw.rect(surface, ceilingColor, gameCeiling)
    
    # draw - leftside border
    pygame.draw.rect(surface, leftSideColor, leftSide)
    
    # draw - rightside border 
    pygame.draw.rect(surface, rightSideColor, rightSide)
    
    # draw - floor border
    pygame.draw.rect(surface, floorColor, gameFloor)
    
    # draw - display (updates till end of game)
    pygame.display.update()
    #close game once player is out of lives
    if(playerLives == 0):
        f = open('score.txt', 'w')
        f.write(str(playerHighScore))
        f.close()    
        pygame.display.close()