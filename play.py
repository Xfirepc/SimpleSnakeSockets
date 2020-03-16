
from lib.config import *
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders
from lib.handlers.client import Client

snake = Snake()
apple = Apple()
borders = Borders()

Player = Client()

while True:
    pygame.time.Clock().tick(10)
    screen.fill(stroke_color)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            Player.sendData(event.key)

        if event.type == QUIT:
            pygame.quit()

    snake.direction = Player.getDirection()
    
    if(snake.collisionBorders() or snake.collisionBody()):
        pygame.quit()

    if (apple.collisionSnake(snake)):
        snake.collisionApple()
        apple.setNewPosition()
        velocity = velocity + 1
    
    borders.render()
    apple.render()
    snake.render()
    
    snake.moveDirection()
    pygame.display.update()

