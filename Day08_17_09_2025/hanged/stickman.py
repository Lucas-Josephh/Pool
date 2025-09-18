import pygame


class Stickman:

    def __init__(self, surface):
        self.surface = surface

    def head(self):
        pygame.draw.circle(self.surface, (255, 255, 255), (300, 300), 50)

    def body(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 300), (300, 450), 5)

    def right_harm(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 395), (380, 395), 5)

    def left_harm(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 395), (220, 395), 5)

    def left_leg(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 450), (250, 530), 5)

    def right_leg(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 450), (350, 530), 5)

    def rope(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 300), (300, 150), 5)

    def top_sidebar(self):
        pygame.draw.line(self.surface, (255, 255, 255), (300, 150), (100, 150), 5)

    def diagonal_bar(self):
        pygame.draw.line(self.surface, (255, 255, 255), (150, 150), (100, 200), 5)

    def vertical_bar(self):
        pygame.draw.line(self.surface, (255, 255, 255), (100, 150), (100, 650), 5)

    def bottom_bar(self):
        pygame.draw.line(self.surface, (255, 255, 255), (100, 650), (0, 650), 5)
        pygame.draw.line(self.surface, (255, 255, 255), (100, 650), (200, 650), 5)
