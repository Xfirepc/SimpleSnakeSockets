
from lib.config import *
import lib.gui.pygame_textinput as Input
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders

# This code is important to init pygame and set the screen size
# Don't touch this content, your game will can crash
pygame.init()
screen = pygame.display.set_mode((SCREN_SIZE, SCREN_SIZE))
pygame.display.set_caption('Snake multi-player sockets')

def initScreenLog():
    image = pygame.image.load(r'images/logo.png')
    text_input = Input.TextInput("Enter nickname")
    while True:
        screen.fill((76, 116, 4))
        events = pygame.event.get()
        for event in events:
            if event.type == KEYDOWN:
                if event.key == ENTER:
                    return text_input

            if event.type == pygame.QUIT:
                exit()

        text_input.update(events)
        screen.blit(image, (0, 0))
        screen.blit(text_input.get_surface(), (220, SCREN_SIZE - 50))
        pygame.display.update()
        pygame.time.Clock().tick(30)


snake = Snake()
apple = Apple(snake.client)
borders = Borders()
player = None

while True:
    if not player:
        player = initScreenLog()

    pygame.time.Clock().tick(2)
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

