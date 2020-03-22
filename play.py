import sys
from lib.config import *
from lib.snake import Snake
from lib.apple import Apple
from lib.borders import Borders
import lib.gui.pygame_textinput as Input
from lib.gui.render_text import renderText

# This code is important to init pygame and set the screen size
# Don't touch this content, your game will can crash
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREN_SIZE, SCREN_SIZE))
pygame.display.set_caption('Snake multi-player sockets')
clock = pygame.time.Clock()


def initScreenLog():
    image = pygame.image.load(r'images/logo.png')
    text_input = Input.TextInput("Enter nickname")

    while True:
        screen.fill((76, 116, 4))
        events = pygame.event.get()
        for e in events:
            if e.type == KEYDOWN:
                if e.key == ENTER:
                    return text_input.get_text()

            if e.type == pygame.QUIT:
                exit()

        text_input.update(events)
        screen.blit(image, (0, 0))
        screen.blit(text_input.get_surface(), (220, SCREN_SIZE - 50))
        pygame.display.update()
        clock.tick(30)


def confirmButton():
    button = pygame.Rect(210, 470, 200, 30)  # creates a rect object
    image = pygame.image.load(r'images/end.png')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = e.pos  # gets mouse position

                # checks if mouse position is over the button
                if button.collidepoint(mouse_pos):
                    return True

        screen.blit(image, (0, 0))
        pygame.display.update()
        clock.tick(30)


def run_game(player, server):
    snake = Snake(server)
    apple = Apple(snake.client)
    borders = Borders()

    while True:
        clock.tick(TIMER)
        direction = snake.getProp('player_direction')
        snake.setProp('name', player)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == UP and direction != DOWN) or (event.key == DOWN and direction != UP):
                    snake.setProp('player_direction', event.key)
                if (event.key == LEFT and direction != RIGHT) or (event.key == RIGHT and direction != LEFT):
                    snake.setProp('player_direction', event.key)

            if event.type == QUIT:
                pygame.quit()

        if snake.collisionBorders() or snake.collisionBody():
            snake.setProp('body', [])
            if confirmButton():
                snake.initState()

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


def main():
    player = initScreenLog()
    server = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    run_game(player, server)


if __name__ == '__main__':
    main()



