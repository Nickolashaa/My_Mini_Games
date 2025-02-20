import pygame
from sys import stdin


try:
    n = int(stdin.read())
    step = 300 / (n * 2)
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    screen.fill('black')

    for i in range(n):
        first = step * i
        second = 300 - step * i
        pygame.draw.ellipse(screen, 'white', (first, 0, second - first, 300), 1)
        pygame.draw.ellipse(screen, 'white', (0, first, 300, second - first), 1)
        
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
        
except Exception:
    print('Неправильный формат ввода')
