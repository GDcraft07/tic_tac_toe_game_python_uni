import pygame
from config import *


def draw_grid(screen):
    '''
    Рисует разделяющие линии
    '''
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i * (WIDTH // 3)), (WIDTH, i * (WIDTH // 3)), LINE_WIDTH)


def draw_figures(screen, game):
    '''
    Рисует фигуры
    '''
    for i in range(3):
        for j in range(3):
            x = j * (WIDTH // 3)
            y = i * (WIDTH // 3)
            if game[i][j] == 1:
                size = (WIDTH // 3) - 2 * PADDING
                pygame.draw.rect(screen, BLACK, (x + PADDING, y + PADDING, size, size))
            elif game[i][j] == 2:
                pygame.draw.circle(screen, BLACK, (x + (WIDTH // 3) // 2, y + (WIDTH // 3) // 2), (WIDTH // 3) // 2 - PADDING)


def get_cell(pos):
    '''
    Возвращвет по координатам на какую клетку нажал игрок
    '''
    x, y = pos
    return (y // (WIDTH // 3)), (x // (WIDTH // 3))


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = get_cell(event.pos)
                if game[x][y] == 0:
                    game[x][y] = current_player + 1
                    current_player = 1 if current_player == 0 else 0

        screen.fill(WHITE)
        draw_grid(screen)
        draw_figures(screen, game)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()