
from lib.config import *
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders

snake = Snake()
apple = Apple(snake.client)
borders = Borders()
 

while True:
    pygame.time.Clock().tick(5)
    screen.fill(stroke_color)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            snake.client.state['player_direction'] = event.key

        if event.type == QUIT:
            pygame.quit()
    
    if(snake.collisionBorders() or snake.collisionBody()):
        pygame.quit()

    apple.setNewPosition(snake.client.state['apples'])
    if (apple.collisionSnake(snake)):
        snake.client.state['player_eat'] = True
        snake.collisionApple()
        apple.setNewPosition(snake.client.state['apples'])
        velocity = velocity + 1

    borders.render()
    apple.render()
    snake.renderEnemies()
    snake.render()
    snake.moveDirection()
    pygame.display.update()

