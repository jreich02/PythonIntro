import pygame, sys
# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize game
pygame.init()
pygame.display.set_caption("hi 4160/6160")
surface = pygame.display.set_mode(SCREEN_SIZE)

# Color of my window
screenColor = (200, 200, 200)

# pong - rectangle vars
pongColor = (255, 255, 255)
pongSize = pongWidth, pongHeight = 25, 25
pongPos = rectX, rectY = 100, 100
pongSpeed = 1

gamePong = pygame.Rect(rectX, rectY, pongWidth, pongHeight)

# player - rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 25
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
def move_pong(gamePong):
    gamePong.move_ip(0, pongSpeed)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    # Allow player to move
    move_rect(gameRect)
    # Allow pong to move
    move_pong(gamePong)
    

    gameRect.clamp_ip(surface.get_rect())
    #draw stuff to screen
    surface.fill(screenColor)
    #draw - player
    pygame.draw.rect(surface, rectColor, gameRect)
    #draw - pong
    pygame.draw.rect(surface, pongColor, gamePong)
    #draw - display
    pygame.display.update()