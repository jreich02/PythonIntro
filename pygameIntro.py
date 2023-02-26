import pygame, sys
# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize game
pygame.init()
#window name
pygame.display.set_caption("Pong-Game")
surface = pygame.display.set_mode(SCREEN_SIZE)


# Color of my window
screenColor = (200, 200, 200)

# pong - rectangle vars
pongColor = (255, 255, 255)
pongSize = pongWidth, pongHeight = 25, 25
pongPos = pongX, pongY = 100, 100
pongSpeed = pongXspeed, pongYspeed = 0.2, 0.5

gamePong = pygame.Rect(pongX, pongY, pongWidth, pongHeight)

# ceiling object - rectangle vars
ceilingColor = (0, 0, 255)
ceilingSize = ceilingWidth, ceilingHeight = SCREEN_WIDTH, 25
ceilingPos = ceilingX, ceilingY =  0, 0

gameCeiling = pygame.Rect(ceilingX, ceilingY, ceilingWidth, ceilingHeight)

# player - rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 10
rectPos = rectX, rectY = 200, 500
rectSpeed = 2

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
    
    #draw - display (keep drawing till end)
    pygame.display.update()