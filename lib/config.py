import pygame, random
from pygame.locals import *


# This constants define player controls not change
ENTER = 13
UP = 273
RIGHT = 275
DOWN = 274
LEFT = 276

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
TIMER = 16

# Try to change the colors of game with RGB codes
apple_color = (255, 0, 102)
background_color = (0, 0, 26)
snake_color = (5, 232, 250)
# snake_color = (181, 245, 31)
color_enemies = (255, 153, 0)
stroke_color = (255, 255, 255)
player_text_color = (5, 232, 250)
enemies_text_color = (255, 102, 255)


def getRandomPosition():
  x = random.randint(grid, SCREN_SIZE - grid * 2)
  y = random.randint(grid, SCREN_SIZE - grid * 2)
  return (x // grid * grid, y // grid * grid)