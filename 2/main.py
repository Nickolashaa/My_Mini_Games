import pygame
import random


class Ball:
    def __init__(self):
        self.x = 240
        self.y = 240
        self.speed = None
        self.pos = None
        self.vector = list()
        
    def coordinate(self):
        x, y = self.pos
        self.vector = list()
        if self.y > y:
            self.vector.append('UP')
        if self.y < y:
            self.vector.append('DOWN')
        if self.x > x:
            self.vector.append('LEFT')
        if self.x < x:
            self.vector.append('RIGHT')
                
    def go(self):
        for mini_vector in self.vector:
            if mini_vector == 'UP':
                self.y -= self.speed
            if mini_vector == 'DOWN':
                self.y += self.speed
            if mini_vector == 'LEFT':
                self.x -= self.speed
            if mini_vector == 'RIGHT':
                self.x += self.speed
                
        if (self.x, self.y) == self.pos:
            self.pos = None
    
    def draw(self):
        pygame.draw.circle(screen, 'red', (self.x, self.y), 20, 0)
            

class Mouse:
    def __init__(self):
        self.x = 240
        self.y = 240
        
    def draw(self):
        pygame.draw.polygon(screen, 'green', [
            (self.x - 1, self.y - 1),
            (self.x - 1, self.y - 4),
            (self.x + 1, self.y - 4),
            (self.x + 1, self.y - 1),
            (self.x + 4, self.y - 1),
            (self.x + 4, self.y + 1),
            (self.x + 1, self.y + 1),
            (self.x + 1, self.y + 4),
            (self.x - 1, self.y + 4),
            (self.x - 1, self.y + 1),
            (self.x - 4, self.y + 1),
            (self.x - 4, self.y - 1),
            ], 1)
 

pygame.init()
screen = pygame.display.set_mode((501, 501))
screen.fill('black')
ball = Ball()
pygame.draw.circle(screen, 'red', (ball.x, ball.y), 20, 0)
mouse = Mouse()
pygame.mouse.set_visible(False)
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.pos = event.pos
            ball.speed = random.randint(5, 10) / 100
            
        if event.type == pygame.MOUSEMOTION:
            mouse.x = event.pos[0]
            mouse.y = event.pos[1]
            
    if ball.pos is not None:
        ball.coordinate()
        ball.go()
    
    screen.fill('black')
    ball.draw()
    mouse.draw()
    pygame.display.flip()
    