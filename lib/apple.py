from lib.config import *


class Apple:
  def __init__(self, client):
    self.client = client
    self.skin = pygame.Surface((grid, grid))
    self.skin.fill(apple_color)
    self.position = []

  def collisionSnake(self, snake):
    if len(self.position) > 0:
      if collision(snake.body[0], self.position):
        return True
    return False

  def setNewPosition(self, position):
    self.position = position

  def render(self, screen):
    if len(self.position) > 0:
      screen.blit(self.skin, self.position)
