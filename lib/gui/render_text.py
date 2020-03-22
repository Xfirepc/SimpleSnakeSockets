from lib.config import *


def renderText(text, tcolor=apple_color):
    my_font = pygame.font.Font('lib/gui/modern_space.ttf', 18)
    surface = my_font.render(text, True, tcolor)
    return surface
