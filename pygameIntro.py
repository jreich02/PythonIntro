
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


# Controller - keyboard Input
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

    # Allow player to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gameRect.x > 0:
        rectX -= rectSpeed
    elif keys[pygame.K_RIGHT] and gameRect.x < (SCREEN_WIDTH - rectWidth):
        rectX += rectSpeed
    move_rect(gameRect)
    
    # Allow pong to move
    pongX+=pongXspeed
    pongY+=pongYspeed
    move_pong(gamePong, pongX, pongY)
    
        
    # Collision
    # Collision - if pong collides with player rect
    collidePlayer = pygame.Rect.colliderect(gameRect, gamePong)
    if collidePlayer:
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
        playerScore += 1
       
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
        if(playerLives != 0):
            pongYspeed *= -1
            playerLives = playerLives - 1
            
    # Game Display and Draw
    # restrict - rect to display
    gameRect.clamp_ip(surface.get_rect())
    
    # restrict - pong to display
    gamePong.clamp_ip(surface.get_rect())
    
    # draw stuff to screen
    surface.fill(screenColor)
    
    # draw - text
    text = font.render('Lives: ' + str(playerLives) + ' Score: ' + str(playerScore), True, textColor, textBackgroundColor)
    surface.blit(text, gameText)
    
    # draw - player
    pygame.draw.rect(surface, rectColor, gameRect)
    
    # draw - pong
    pygame.draw.rect(surface, pongColor, gamePong)
    
    # draw - ceiling
    pygame.draw.rect(surface, ceilingColor, gameCeiling)
    
    # draw - leftside
    pygame.draw.rect(surface, leftSideColor, leftSide)
    
    # draw - rightside
    pygame.draw.rect(surface, rightSideColor, rightSide)
    
    # draw - floor
    pygame.draw.rect(surface, floorColor, gameFloor)
    
    # draw - display (keep drawing till end)
    pygame.display.update()