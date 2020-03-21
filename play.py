
from lib.config import *
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders

# This code is important to init pygame and set the screen size
# Don't touch this content, your game will can crash
pygame.init()
screen = pygame.display.set_mode((SCREN_SIZE, SCREN_SIZE))
pygame.display.set_caption('Snake')

snake = Snake()
apple = Apple(snake.client)
borders = Borders()

while True:
    pygame.time.Clock().tick(TIMER)
    direction = snake.getProp('player_direction')

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if (event.key == UP and direction != DOWN) or (event.key == DOWN and direction != UP):
                snake.setProp('player_direction', event.key)
            if (event.key == LEFT and direction != RIGHT) or (event.key == RIGHT and direction != LEFT):
                snake.setProp('player_direction', event.key)

        if event.type == QUIT:
            pygame.quit()

    if snake.collisionBorders() or snake.collisionBody():
        pygame.quit()

    apple.setNewPosition(snake.getProp('apples'))

    if apple.collisionSnake(snake):
        snake.setProp('player_eat', True)
        snake.collisionApple()
        apple.setNewPosition(snake.getProp('apples'))

    screen.fill(stroke_color)
    borders.render(screen)
    apple.render(screen)
    snake.renderEnemies(screen)
    snake.render(screen)
    snake.moveDirection()
    pygame.display.update()

