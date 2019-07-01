import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.info()

size = (width, height) = (int(screen.current_w), int(screen.current_h))
screen = pygame.display.set_mod(size)
clock = pygame.time.Clock()
color(255, 0, 0)


def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display.flip()


if __name__ == '__main__':
    main()
