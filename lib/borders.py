from lib.config import *


class Borders:
  def __init__(self):
    self.position = (grid, grid)
    self.skin = pygame.Surface((SCREN_SIZE - grid*2, SCREN_SIZE - grid*2))
    self.skin.fill(backgroud_color)

  def render(self, screen):
    screen.blit(self.skin, self.position)
