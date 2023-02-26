import pygame, sys
import random
import math
# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700

# Initialize game
pygame.init()

# window name
pygame.display.set_caption("Pong-Game")
surface = pygame.display.set_mode(SCREEN_SIZE)

# Color of my window
screenColor = (200, 200, 200)

# player lives and score: 
playerLives = 3
playerScore = 0

# player - rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 10
rectPos = rectX, rectY = 300, 650
rectSpeed = 0.5

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

# pong - rectangle vars
pongColor = (255, 255, 255)
pongSize = pongWidth, pongHeight = 25, 25
pongPos = pongX, pongY = 100, 100
pongXspeed, pongYspeed = 0.2, 0.5
pongSpeed = 0.8

gamePong = pygame.Rect(pongX, pongY, pongWidth, pongHeight)


# Border Objects
# ceiling object - rectangle vars
ceilingColor = (0, 0, 255)
ceilingSize = ceilingWidth, ceilingHeight = SCREEN_WIDTH, 25
ceilingPos = ceilingX, ceilingY =  0, 0
gameCeiling = pygame.Rect(ceilingX, ceilingY, ceilingWidth, ceilingHeight)

# left side - rectangle vars
leftSideColor = (0, 0, 255)
leftSideSize = leftSideWidth, leftSideHeight = 25, SCREEN_HEIGHT
leftSidePosition = leftSideX, leftSideY =  0, 25
leftSide = pygame.Rect(leftSideX, leftSideY, leftSideWidth, leftSideHeight)

#right side - rect vars
rightSideColor = (0, 0, 255)
rightSideSize = rightSideWidth, rightSideHeight = 25, SCREEN_HEIGHT
rightSidePosition = rightSideX, rightSideY = 675, 0
rightSide = pygame.Rect(rightSideX, rightSideY, rightSideWidth, rightSideHeight)

#floor
floorColor = (0, 0, 255)
floorSize = floorWidth, floorHeight = SCREEN_WIDTH, 25
floorPosition = floorX, floorY = 0, 675
gameFloor = pygame.Rect(floorX, floorY, floorWidth, floorHeight)

# Controller - keyboard Input
def move_rect(gameRect):
    gameRect.update(rectX, rectY, rectWidth, rectHeight)

#move pong 
def move_pong(gamePong, pongX, pongY):
    gamePong.update(pongX, pongY, pongWidth, pongHeight)
    
# Display - font and text
# colors
textBackgroundColor = (200, 200, 200)
textColor = (255, 0, 0)

font = pygame.font.Font('Fragmentcore.otf', 25)
textRectSize = textWidth, textHeight = 200, 200
textRectPos = textRectX, textRectY = 32,32 #50, 50 
gameText = pygame.Rect(textRectX, textRectY, textWidth, textHeight)

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
        randspeed = random.uniform(0.2, 1) * pongSpeed
        if pongXspeed >= 0:
            pongXspeed = randspeed
        if pongXspeed < 0:
            pongXspeed = randspeed
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
        if (playerLives != 0):
            pongYspeed *= -1
            playerLives = playerLives - 1
        else:
            pongYspeed*= 0 
            pongXspeed*= 0
    
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