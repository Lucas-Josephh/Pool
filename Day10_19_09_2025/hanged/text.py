import time
import pygame


class Text:
    def __init__(self, surface, msg="", rects=None):
        self.surface = surface
        self.msg = msg
        self.rects = rects

    def create(self):
        self.rects = pygame.font.Font(None, 36).render(self.msg, True, (255, 255, 255))

    def modifier(self, msg):
        self.msg = msg
        self.rects = pygame.font.Font(None, 36).render(self.msg, True, (255, 255, 255))

    def display(self, surface, size, pos=(0, 0)):
        self.surface = surface
        self.pos = pos
        pygame.draw.rect(self.surface, (255, 255, 255), (self.pos, (500, 50)), 100)
        pygame.display.flip()
        self.rect = pygame.font.Font(None, 36).render(self.msg, True, (0, 0, 0))
        self.surface.blit(self.rect, self.pos)
