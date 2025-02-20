import pygame


def my_rect(screen, color, coords, pic):
    pygame.draw.rect(screen, 'white', coords, 0)
    coords[0] += 1
    coords[1] += 1
    coords[2] -= 2
    coords[3] -= 2
    pygame.draw.rect(screen, color, coords, 0)
    coords[0] += 1
    coords[1] += 1
    coords[2] -= 2
    coords[3] -= 2
    if pic == 0:
        pygame.draw.circle(screen,
                           'red',
                           (coords[0] + coords[2] // 2, coords[1] + coords[3] // 2),
                           coords[2] // 2,
                           1)
    if pic == 1:
        pygame.draw.line(screen,
                          'blue',
                          (coords[0], coords[1]),
                          (coords[0] + coords[2], coords[1] + coords[3])
                          )
        pygame.draw.line(screen,
                          'blue',
                          (coords[0] + coords[2], coords[1]),
                          (coords[0], coords[1] + coords[2])
                          ) 
    

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.step = 1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                my_rect(screen,
                        'black',
                        [self.left + self.cell_size * j,
                        self.top + self.cell_size * i,
                        self.cell_size,
                        self.cell_size,
                        ],
                        self.board[i][j]
                        )
                            
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        
    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if x > self.width - 1 or y > self.height - 1 or x < 0 or y < 0:
            return None
        return y, x
        
    def on_click(self, cell_coords):
        if cell_coords is not None:
            x, y = cell_coords
            if self.board[x][y] == -1:
                self.board[x][y] = self.step % 2
                self.step += 1
     

pygame.init()
screen = pygame.display.set_mode((500, 350))
screen.fill('black')
board = Board(10, 7)
board.set_view(27, 20, 45)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
    