import pygame
import random
import pprint
import time
    

class Minesweeper:
    class Square:
        def __init__(self, size, screen, pos_x, pos_y, left, top):
            self.value = 0
            self.size = size
            self.screen = screen
            self.pos_x = pos_y
            self.pos_y = pos_x
            self.rect = pygame.Rect(
                left + pos_x * size,
                top + pos_y * size,
                size,
                size
            )
            self.hide = True
            self.flag = False

        def draw(self, pos_x, pos_y, left, top):
            x = left + pos_x * self.size
            y = top + pos_y * self.size
            pygame.draw.rect(self.screen, 'white', (x, y, self.size, self.size), 0)

            if self.hide:
                pygame.draw.rect(self.screen, (20, 20, 20), (x + 1, y + 1, self.size - 2, self.size - 2), 0)
            else:
                color = 'blue' if self.value == 9 else (20, 20, 20)
                pygame.draw.rect(self.screen, color, (x + 1, y + 1, self.size - 2, self.size - 2), 0)

                if self.value != 9:
                    text = font.render(str(self.value), True, 'white')
                    self.screen.blit(text, (x + 10, y + 10))
                    
            if self.flag:
                pygame.draw.circle(screen, 'purple', (x + self.size // 2, y + self.size // 2), self.size // 2 - 5, 4)
                    
        def open_cell(self, board):
            if not self.hide:
                return
            self.hide = False
            if self.value == 0:
                board.try_to_open(self.pos_x + 1, self.pos_y)
                board.try_to_open(self.pos_x - 1, self.pos_y)
                board.try_to_open(self.pos_x, self.pos_y + 1)
                board.try_to_open(self.pos_x, self.pos_y - 1)
                board.try_to_open(self.pos_x + 1, self.pos_y + 1)
                board.try_to_open(self.pos_x + 1, self.pos_y - 1)
                board.try_to_open(self.pos_x - 1, self.pos_y + 1)
                board.try_to_open(self.pos_x - 1, self.pos_y - 1)
                
            
    def __init__(self, screen):
        self.left = 20
        self.top = 20
        self.width = 10
        self.height = 15
        self.sq_size = 40
        self.screen = screen
        self.board = [[self.Square(self.sq_size, self.screen, y, x, self.left, self.top) for y in range(self.width)] for x in range(self.height)]
        self.cnt_mines = 10
        self.game = 0
    
    def render(self):
        for x in range(self.height):
            for y in range(self.width):
                self.board[x][y].draw(y, x, self.left, self.top)
                
    def generate_mines(self):
        bomb_positions = random.sample([(i, j) for i in range(self.height) for j in range(self.width)], k=self.cnt_mines)
        for row, col in bomb_positions:
            self.board[row][col].value = 9
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < self.height and 0 <= j < self.width and self.board[i][j].value != 9:
                        self.board[i][j].value += 1

    def print(self):
        array = list()
        for i in range(len(self.board)):
            m_array = list()
            for j in range(len(self.board[i])):
                m_array.append(self.board[i][j].value)
            array.append(m_array)
        pprint.pprint(array)
        
    def get_square(self, mouse_pos):
        for x in range(self.height):
            for y in range(self.width):
                if self.board[x][y].rect.collidepoint(mouse_pos):
                    return self.board[x][y]
        return None

    def open_all(self):
        for x in range(self.height):
            for y in range(self.width):
                self.board[x][y].open_cell(board=self)
    
    def click(self, event):
        square = self.get_square(event.pos)
        if square:
            if event.button == 1:
                if square.value == 9:
                    self.game = -1
                    self.open_all()
                    return
                square.open_cell(board=self)
            if event.button == 3:
                if square.flag:
                    square.flag = False
                else:
                    square.flag = True
                
            
    def try_to_open(self, pos_x, pos_y):
        if 0 <= pos_x < self.height and 0 <= pos_y < self.width:
            self.board[pos_x][pos_y].open_cell(board=self)
            
    def check_win(self):
        i_think_its_win = True
        for x in range(self.height):
            for y in range(self.width):
                if self.board[x][y].value != 9 and self.board[x][y].hide is True:
                    i_think_its_win = False
                if self.board[x][y].value == 9 and self.board[x][y].flag is False:
                    i_think_its_win = False
                    
        if i_think_its_win:
            self.game = 1
    
        
pygame.init()
font = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode((440, 640))
screen.fill((20, 20, 20))
board = Minesweeper(screen)
board.generate_mines()
running = True
board.print()

while running and board.game == 0:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event)
    
    board.render()
    board.check_win()
    pygame.display.flip()
    
overlay = pygame.Surface((440, 640), pygame.SRCALPHA)
overlay.fill((0, 0, 0, 220))
font = pygame.font.SysFont(None, 80)
screen.blit(overlay, (0, 0))
if board.game == 1:
    text = font.render('YOU WIN', True, 'green')
if board.game == -1:
    text = font.render('YOU LOSE', True, 'red')
screen.blit(text, (220 - text.get_width() // 2, 320 - text.get_height() // 2))
pygame.display.flip()
time.sleep(3)
pygame.quit()