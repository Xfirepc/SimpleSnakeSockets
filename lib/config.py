import pygame, random
from pygame.locals import *


# This constants define player controls not change
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# This vars define the size screen and the grid try change
# whit numbers SCREEN_SIZE  = 800 and grid = 20
SCREN_SIZE = 600
grid = 10

# Collision function define the event if two elements have
# the same position x and y
def collision(c1, c2):
  return (c1[0] == c2[0]) and (c1[1] == c2[1])

# You can try to change this value, remember the velocity
# is incresead by the apple numbers ate
velocity = 15



# Try to change the colors of game with RGB codes
apple_color = (255, 0, 102)
backgroud_color =  (0, 0, 26)
snake_color = (181, 245, 31)
stroke_color = (255, 255, 255)


# This code is important to init pygame and set the screen size
# Don't touch this content, your game will can crash
pygame.init()
screen = pygame.display.set_mode((SCREN_SIZE, SCREN_SIZE))
pygame.display.set_caption('Snake')


