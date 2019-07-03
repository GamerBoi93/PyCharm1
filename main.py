import sys, pygame
import random
from pygame.locals import*

pygame.init()
screen = pygame.display.Info()

size = (width, height) = (int(screen.current_w), int(screen.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255, 0, 0)

Asteroids = pygame.sprite.Group()
NumLevels = 4
Level = 1
AsteoidCount = 3
Player = (Ship(20,200))


def main():
    print("hewow uwu")

if __name__ == "__main__":
    main()