import pygame
from config import *


def draw_grid(screen):
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i * (WIDTH // 3)), (WIDTH, i * (WIDTH // 3)), LINE_WIDTH)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()