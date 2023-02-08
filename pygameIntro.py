import pygame, sys

# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize game
pygame.init()
pygame.display.set_caption("hi 4160/6160")
surface = pygame.display.set_mode(SCREEN_SIZE)

# Color of my window
screenColor = (200, 200, 200)

# Rectangle vars
rectColor = (255, 0, 0)
rectSize = rectWidth, rectHeight = 100, 100
rectPos = rectX, rectY = 100, 100
rectSpeed = 2

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

def move_rect(gameRect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gamerect.x > 0:
        gameRect.move_ip(-rectSpeed,0)
    elif keys[pygame.K_RIGHT] and gameRect.x < (SCREEN_WIDTH - rectWidth):
        gameRect.move_ip(rectSpeed,0)
    elif keys[pygame.K_UP]:
        gameRect.move_ip(0,-rectSpeed)
    elif keys[pygame.K_DOWN]:
        gameRect.move_ip(0,rectSpeed)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    move_rect(gameRect)

    gameRect.clamp_ip(suface.get_rect())

    surface.fill(screenColor)
    pygame.draw.rect(surface, rectColor, gameRect)
    pygame.display.update()

