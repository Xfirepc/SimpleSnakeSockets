from lib.config import *

class Apple:
  def __init__(self):
    self.body = [(200, 200), (220, 200), (240, 200), (260, 200)]
    self.skin = pygame.Surface((grid, grid))
    self.skin.fill(apple_color)
    self.position = self.getRandomPosition()

  def collisionSnake(self, snake):
    if collision(snake.body[0], self.position):
      return True
    return False

  def setNewPosition(self):
    self.position = self.getRandomPosition()

  def getRandomPosition(self):
    x = random.randint(grid, SCREN_SIZE - grid*2)
    y = random.randint(grid, SCREN_SIZE - grid*2)
    return (x//grid*grid, y//grid*grid)

  def render(self):
    screen.blit(self.skin, self.position)
