import pygame, sys
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

# pong - rectangle vars
pongColor = (255, 255, 255)
pongSize = pongWidth, pongHeight = 25, 25
pongPos = pongX, pongY = 100, 100
pongSpeed = pongXspeed, pongYspeed = 0.2, 0.5

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

# player - rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 10
rectPos = rectX, rectY = 300, 650
rectSpeed = 1

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

# Controller - keyboard Input
def move_rect(gameRect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gameRect.x > 0:
        gameRect.move_ip(-rectSpeed,0)
    elif keys[pygame.K_RIGHT] and gameRect.x < (SCREEN_WIDTH - rectWidth):
        gameRect.move_ip(rectSpeed,0)
    #elif keys[pygame.K_UP]:
        #gameRect.move_ip(0,-rectSpeed)
    #elif keys[pygame.K_DOWN]:
        #gameRect.move_ip(0,rectSpeed)

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
    move_rect(gameRect)
    
    # Allow pong to move
    pongX+=pongXspeed
    pongY+=pongYspeed
    move_pong(gamePong, pongX, pongY)
    
    #Collision - if pong collides with player rect
    collidePlayer = pygame.Rect.colliderect(gameRect, gamePong)
    if collidePlayer:
        pongYspeed *= -1
        
    #Collision - if pong collides with display ceiling
    collideCeiling = pygame.Rect.colliderect(gameCeiling, gamePong)
    if collideCeiling:
        pongYspeed*=-1
        
    #Collision - if pong collides with side borders
    collideLeftSide = pygame.Rect.colliderect(leftSide, gamePong)
    collideRightSide = pygame.Rect.colliderect(rightSide, gamePong)
    if collideLeftSide or collideRightSide:
        pongXspeed*=-1
    
    #Collision - if pong collides with floor
    collideFloor = pygame.Rect.colliderect(gameFloor, gamePong)
    if collideFloor:
        if (playerLives != 0):
            pongYspeed*= -1
            playerLives = playerLives - 1

    #restrict - rect to display
    gameRect.clamp_ip(surface.get_rect())
    
    #restrict - pong to display
    gamePong.clamp_ip(surface.get_rect())
    
    #draw stuff to screen
    surface.fill(screenColor)
    
    #draw - player
    pygame.draw.rect(surface, rectColor, gameRect)
    
    #draw - pong
    pygame.draw.rect(surface, pongColor, gamePong)
    
    #draw - ceiling
    pygame.draw.rect(surface, ceilingColor, gameCeiling)
    
    #draw - leftside
    pygame.draw.rect(surface, leftSideColor, leftSide)
    
    #draw - rightside
    pygame.draw.rect(surface, rightSideColor, rightSide)
    
    #draw - floor
    pygame.draw.rect(surface, floorColor, gameFloor)
    
    #draw - display (keep drawing till end)
    pygame.display.update()