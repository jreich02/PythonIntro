# Font and Text file
import pygame, sys

# colors
textBackgroundColor = (200, 200, 200)
textColor = (255, 0, 0)

# font
font = pygame.font.Font('Fragmentcore.otf', 25)

# text background
textRectSize = textWidth, textHeight = 200, 200
textRectPos = textRectX, textRectY = 32,32
gameText = pygame.Rect(textRectX, textRectY, textWidth, textHeight)