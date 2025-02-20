import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.width = 50
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('gray')
        self.rect = self.image.get_rect(topleft=(x, y))
        

class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.width = 10
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=(x, y))
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.width = 20
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def update(self, vector, platforms, stairs):
        if vector == 'GRAVITY DOWN':
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    return
                
            for stair in stairs:
                if self.rect.colliderect(stair.rect):
                    return
                
            self.rect.y += 5
            
        if vector == 'UP':
            for stair in stairs:
                if self.rect.colliderect(stair.rect):
                    self.rect.y -= 10
                    return
                    
        if vector == 'DOWN':
            for stair in stairs:
                if self.rect.colliderect(stair.rect):
                    self.rect.y += 10
                    return
            
        if vector == 'RIGHT':
            self.rect.x += 10
            
        if vector == 'LEFT':
            self.rect.x -= 10


def main():
    pygame.init()
    WIDTH = HEIGHT = 500
    FPS = 60
    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT, 100)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    platforms = pygame.sprite.Group()
    stairs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    player = None
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                ctrl_pressed = pygame.key.get_pressed()[pygame.K_LCTRL]
                if event.button == 1 and not ctrl_pressed:
                    Platform(event.pos[0], event.pos[1], platforms, all_sprites)
                    
                if event.button == 1 and ctrl_pressed:
                    Stair(event.pos[0], event.pos[1], stairs, all_sprites)
                
                if event.button == 3:
                    if player is None:
                        player = Player(event.pos[0], event.pos[1], all_sprites)
                    else:
                        player.move(event.pos[0], event.pos[1])
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.update('LEFT', platforms, stairs)
                if event.key == pygame.K_RIGHT:
                    player.update('RIGHT', platforms, stairs)
                if event.key == pygame.K_UP:
                    player.update('UP', platforms, stairs)
                if event.key == pygame.K_DOWN:
                    player.update('DOWN', platforms, stairs)
                        
            if event.type == TIMER_EVENT and player is not None:
                player.update('GRAVITY DOWN', platforms, stairs)

        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
