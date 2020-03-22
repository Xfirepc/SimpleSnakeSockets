from lib.config import *
from lib.handlers.client import Client
import random       

initial_body = [(200, 200), (200 + grid, 200), (200 + grid * 2, 200), (200 + grid * 3, 200)]

class Snake:
    def __init__(self):
        self.client = Client()
        self.body = initial_body
        self.score = 0
        self.direction = 0
        self.enemy = pygame.Surface((grid, grid))
        self.enemy.fill((0, 0, 255))
        self.skin = pygame.Surface((grid, grid))
        self.skin.fill(snake_color)
        self.initState()

    def initState(self):
        self.score = 0
        self.direction = 276
        self.body = initial_body
        self.client.state['apples'] = []
        self.client.state['enemies'] = []
        self.client.state['player_eat'] = False
        self.client.state['last_direction'] = 275
        self.client.state['player_body'] = self.body
        self.client.state['player_direction'] = self.direction
        self.client.state['name'] = 'name' + str(random.randint(0, 1000))

    def setProp(self, key, value):
        self.client.state[key] = value

    def getProp(self, key):
        return self.client.state[key]

    def moveDirection(self):
        state = self.loadState()
        self.body = state['player_body']
        self.direction = state['player_direction']

    def collisionApple(self):
        self.score = self.score + 1
        self.client.state['player_body'].append((-100, -100))

    def collisionBody(self):
        for j in range(1, len(self.body)):
            if collision(self.body[0], self.body[j]):
                self.client.state['player_body'] = []
                return True
        return False

    def collisionBorders(self):
        if self.body[0][0] < 10 or self.body[0][0] > SCREN_SIZE - grid*2 or self.body[0][1] < 10 or self.body[0][1] > SCREN_SIZE - grid*2:
            self.client.state['player_body'] = []
            return True
        return False

    def loadState(self, key=False):
        self.client.sendStatus()
        if key:
            return self.client.state[key]
        return self.client.state

    def renderEnemies(self, screen):
        for enemy in self.client.state['enemies']:
            for pos in enemy:
                screen.blit(self.enemy, pos)

    def render(self, screen):
        for pos in self.body:
            screen.blit(self.skin, pos)
