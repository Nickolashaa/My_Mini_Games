import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.images = ['data/bomb.png', 'data/boom.png']
        self.image = pygame.image.load(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.image.get_width() - 1)
        self.rect.y = random.randrange(HEIGHT - self.image.get_height() - 1)
    
    def update(self, *args):
        if args and self.rect.collidepoint(args[0]):
            self.image = pygame.image.load(self.images[1])
        
        
pygame.init()
WIDTH = HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill('black')
running = True
all_sprites = pygame.sprite.Group()
for _ in range(20):
    Bomb(all_sprites)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event.pos)
        
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()