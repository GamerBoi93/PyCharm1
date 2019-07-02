import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.Info()

size = (width, height) = (int(screen.current_w), int(screen.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255, 0, 0)


sprite_image = pygame.image.load("porpoise.png")
sprite_image = pygame.transform.smoothscale(sprite_image, (280, 280))
sprite_rect = sprite_image.get_rect()

sprite_rect.center = (width // 2, height // 2)

speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
sprite_image = pygame.transform.rotate(sprite_image, 180 - rotation)


def move_sprite():
    sprite_rect.move.ip(speed)


def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(sprite_image, sprite_rect)
        pygame.display.flip()



if __name__ == '__main__':
    main()

