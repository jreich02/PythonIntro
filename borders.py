# Border and Boundary code
import pygame, sys

# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700

# window name
pygame.display.set_caption("Pong-Game")
surface = pygame.display.set_mode(SCREEN_SIZE)

# Color of my window
screenColor = (200, 200, 200)

# Border Objects - Functiononal 
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

# Court lines - decorational
courtLineColor = (50, 0, 50)
courtLineSize = courtWidth, courtHeight = SCREEN_WIDTH, 10
# court line 1
courtLineOnePosition = courtLine1X, courtLine1Y = 0, 300
# court line 2
courtLineTwoPosition = courtLine2X, courtLine2Y = 0, 400

courtLineOne = pygame.Rect(courtLine1X, courtLine1Y, courtWidth, courtHeight)
courtLineTwo = pygame.Rect(courtLine2X, courtLine2Y, courtWidth, courtHeight)
