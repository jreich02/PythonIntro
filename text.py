# Font and Text file
import pygame, sys

# colors
textBackgroundColor = (200, 200, 200)
textColor = (255, 0, 0)

# font
font = pygame.font.Font('Fragmentcore.otf', 25)


# active game text
textRectSize = textWidth, textHeight = 200, 200
textRectPos = textRectX, textRectY = 200,32
gameText = pygame.Rect(textRectX, textRectY, textWidth, textHeight)

