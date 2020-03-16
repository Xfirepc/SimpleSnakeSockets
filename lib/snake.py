from lib.config import *

class Snake:
  def __init__(self):
    self.body = [(200, 200), (200+grid, 200), (200+grid*2, 200), (200+grid*3, 200)]
    self.skin = pygame.Surface((grid, grid))
    self.skin.fill(snake_color)
    self.direction = 276

  def collisionApple(self):
    self.body.append((-100, -100))

  def moveDirection(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i] = (self.body[i-1][0], self.body[i-1][1])

    if self.direction == 273:  
      self.body[0] = (self.body[0][0], self.body[0][1] - grid)
    if self.direction == 274:
      self.body[0] = (self.body[0][0], self.body[0][1] + grid)
    if self.direction == 275:
      self.body[0] = (self.body[0][0] + grid, self.body[0][1])
    if self.direction == 276:
      self.body[0] = (self.body[0][0] - grid, self.body[0][1])

  def collisionBody(self):
    for j in range(1, len(self.body)):
      if(collision(self.body[0], self.body[j])):
        return True
    return False

  def collisionBorders(self):
    return (self.body[0][0] < 10 or self.body[0][0] > SCREN_SIZE - grid*2 or self.body[0][1] < 10 or self.body[0][1] > SCREN_SIZE - grid*2)

  def render(self):
    for pos in self.body:
      screen.blit(self.skin, pos)
