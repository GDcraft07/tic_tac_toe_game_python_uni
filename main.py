import pygame
from config import *
from random import choice


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


def find_winner(game):
    '''
    Проверка есть ли победитель
    '''
    for i in range(3):
        if game[i][0] != 0 and game[i][0] == game[i][1] == game[i][2]:
            return game[i][0]
        if game[0][i] != 0 and game[0][i] == game[1][i] == game[2][i]:
            return game[0][i]
    if game[1][1] != 0:
        if game[0][0] == game[1][1] == game[2][2]:
            return game[1][1]
        if game[0][2] == game[1][1] == game[2][0]:
            return game[1][1]
    return None


def get_empty_cells(game):
    '''
    Cписок координат всех пустых клеток
    '''
    return [(i, j) for i in range(3) for j in range(3) if game[i][j] == 0]


def find_line_move(game, player):
    '''
    Ищет линию, где у игрока две фигуры и одна пустая клетка, и возвращает эту клетку
    '''
    for line in LINES:
        values = [game[i][j] for i, j in line]
        if values.count(player) == 2 and values.count(0) == 1:
            return line[values.index(0)]
    return None


def get_bot_move(game):
    '''
    Выбирает ход бота по приоритету
    '''
    move = find_line_move(game, 2)
    if move:
        return move

    move = find_line_move(game, 1)
    if move:
        return move

    if game[1][1] == 0:
        return (1, 1)

    free_corners = [(i, j) for i, j in CORNERS if game[i][j] == 0]
    if free_corners:
        return choice(free_corners)

    return choice(get_empty_cells(game))


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = get_cell(event.pos)
                if game[x][y] == 0:
                    game[x][y] = 1
                    if find_winner(game) is None and get_empty_cells(game):
                        row, col = get_bot_move(game)
                        game[row][col] = 2

        screen.fill(WHITE)
        draw_grid(screen)
        draw_figures(screen, game)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()