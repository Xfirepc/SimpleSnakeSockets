from lib.config import *
from lib.handlers.client import Client
import random

class Snake:
    def __init__(self):
        self.enemy = pygame.Surface((grid, grid))
        self.enemy.fill((204, 0, 153))

        self.skin = pygame.Surface((grid, grid))
        self.skin.fill(snake_color)
        self.body = [(200, 200), (200+grid, 200), (200+grid*2, 200), (200+grid*3, 200)]
        self.direction = 276

        self.client = Client()
        self.client.state['name'] = 'name' + str(random.randint(0, 1000))
        self.client.state['player_body'] = self.body
        self.client.state['player_direction'] = self.direction
        self.client.state['enemies'] = []

    def moveDirection(self):
        state = self.loadState()
        print(state)
        self.body = state['player_body']
        self.direction = state['player_direction']


    def collisionApple(self):
        self.body.append((-100, -100))


    def collisionBody(self):
        for j in range(1, len(self.body)):
            if(collision(self.body[0], self.body[j])):
                self.client.state['player_body'] = []
                return True
        return False

    def collisionBorders(self):
        if((self.body[0][0] < 10 or self.body[0][0] > SCREN_SIZE - grid*2 or self.body[0][1] < 10 or self.body[0][1] > SCREN_SIZE - grid*2)):
            self.client.state['player_body'] = []
            return True
        return False

    def loadState(self, key = False):
        self.client.sendStatus()
        if (key):
            return self.client.state[key]
        return self.client.state

    def renderEnemies(self):
        for enemy in self.client.state['enemies']:
            for pos in enemy:
                screen.blit(self.enemy, pos)

    def render(self):
        for pos in self.body:
            screen.blit(self.skin, pos)
