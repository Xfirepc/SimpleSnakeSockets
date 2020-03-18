
from lib.config import *
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders

snake = Snake()
apple = Apple()
borders = Borders()
 

while True:
    pygame.time.Clock().tick(3)
    screen.fill(stroke_color)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            snake.client.state['player_direction'] = event.key

        if event.type == QUIT:
            pygame.quit()
    
    if(snake.collisionBorders() or snake.collisionBody()):
        pygame.quit()

    if (apple.collisionSnake(snake)):
        snake.collisionApple()
        apple.setNewPosition()
        velocity = velocity + 1
    
    apple.render()
    snake.renderEnemies()
    borders.render()
    snake.render()
    
    snake.moveDirection()
    pygame.display.update()

