import pygame

pygame.init()

keep_open = True

background = pygame.image.load(
    "C:\\epitech\Pool\\Day08_17_09_2025\\Tasks_3.4\\src\\background.png"
)
background = pygame.transform.scale(background, (600, 600))

screen = pygame.display.set_mode((600, 600))
rect = pygame.Rect(10, 20, 200, 100)


while keep_open:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keep_open = False
    screen.blit(background, (0, 0))
    pygame.display.update()
    pygame.display.flip()
