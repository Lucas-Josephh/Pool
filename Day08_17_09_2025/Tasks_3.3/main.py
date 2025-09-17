import pygame

pygame.init()
pygame.display.set_mode((600, 600))

keep_open = True

while keep_open:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keep_open = False
