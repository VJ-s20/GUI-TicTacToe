import pygame
from pygame.constants import KEYDOWN, KEYUP, K_SPACE
import random
pygame.init()
pygame.font.init()
fnt = pygame.font.SysFont("comiscans", 280)
WIDTH = 500
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))


RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.width = width
        self.color = WHITE
        self.total_rows = total_rows
        self.plyer = None

    def is_valid(self):
        return self.color == WHITE

    def player_color(self):
        self.color = RED

    def comp_color(self):
        self.color = GREEN

    def Reset(self):
        self.color = WHITE

    def player_move(self, chance):
        self.plyer = chance

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width), 5)

    def player(self, win):
        text = fnt.render(self.plyer, 1, (0, 0, 0))
        win.blit(text, (self.x+15, self.y))


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos
    row = x // gap
    col = y // gap
    return row, col


def make_grid(rows, width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap), 3)
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width), 3)


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
            spot.player(win)
    draw_grid(win, rows,  width)
    pygame.display.update()


def main(win, width):
    Rows = 3
    grid = make_grid(Rows, width)
    run = True
    player = 'X'
    other_player = "O"
    Board = [[i, j] for i in range(3) for j in range(3)]
    while run:
        draw(win, grid, Rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, Rows, width)
                    spot = grid[row][col]
                    valid_move = True
                    if spot.is_valid():
                        spot.player_color()
                        spot.player_move(player)
                    try:
                        Board.pop(Board.index([row, col]))
                    except:
                        valid_move = False
                if event.key == pygame.K_c:
                    grid = make_grid(Rows, width)
                    Board = [[i, j] for i in range(3) for j in range(3)]
            if event.type == KEYUP and valid_move:
                if event.key == K_SPACE:
                    if Board:
                        x, y = random.choice(Board)
                        spot = grid[x][y]
                        spot.comp_color()
                        spot.player_move(other_player)
                        Board.pop(Board.index([x, y]))

    pygame.quit()


main(SCREEN, WIDTH)
