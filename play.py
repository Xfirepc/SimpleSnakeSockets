
from lib.config import *
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders
from lib.handlers.client import Client


snake = Snake()
apple = Apple()
borders = Borders()

while True:
    pygame.time.Clock().tick(velocity - 5)
    screen.fill(stroke_color)

    for event in pygame.event.get():
      
        if event.type == KEYDOWN:
            if event.key == K_UP and snake.direction != DOWN:
                snake.direction = UP
            if event.key == K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            if event.key == K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            if event.key == K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

        if event.type == QUIT:
            pygame.quit()

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

