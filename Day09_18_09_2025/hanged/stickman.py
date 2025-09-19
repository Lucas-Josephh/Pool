import pygame


class Stickman:

    def __init__(
        self,
        surface,
        width,
        heigh,
        pos_x=0,
        pos_y=0,
        width_bottom=0,
        vertical_pos_x=0,
        vertical_pos_y=0,
        vertical_width=0,
        top_sidebar_height=0,
        top_sidebar_width=0,
    ):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.heigh = heigh
        self.width_bottom = width_bottom
        self.vertical_pos_x = vertical_pos_x
        self.vertical_pos_y = vertical_pos_y
        self.vertical_width = vertical_width
        self.top_sidebar_height = top_sidebar_height
        self.top_sidebar_width = top_sidebar_width

    def head(self):
        pygame.draw.circle(self.surface, (0, 0, 0), (300, 300), 50)

    def body(self):
        pygame.draw.line(self.surface, (0, 0, 0), (300, 300), (300, 450), 5)

    def right_harm(self):
        pygame.draw.line(self.surface, (0, 0, 0), (300, 395), (380, 395), 5)

    def left_harm(self):
        pygame.draw.line(self.surface, (0, 0, 0), (300, 395), (220, 395), 5)

    def left_leg(self):
        pygame.draw.line(self.surface, (0, 0, 0), (300, 450), (250, 530), 5)

    def right_leg(self):
        pygame.draw.line(self.surface, (0, 0, 0), (300, 450), (350, 530), 5)

    def bottom_bar(self):
        img = pygame.image.load("Day09_18_09_2025\\hanged\\src\\bottom_bar.png")
        img = pygame.transform.scale(img, (200, 35))
        img.convert()
        self.set_width_bottom_bar(img.get_width())
        self.surface.blit(img, (self.pos_x, self.pos_y))

    def set_width_bottom_bar(self, width):
        self.width_bottom = width

    def get_width_bottom_bar(self):
        return self.width_bottom

    def vertical_bar(self):
        img = pygame.image.load("Day09_18_09_2025\\hanged\\src\\vertical_bar.png")
        img = pygame.transform.scale(img, (40, 220))
        img.convert()
        pos_x = self.pos_x + (self.get_width_bottom_bar() // 2) - (img.get_width() // 2)
        pos_y = self.pos_y - img.get_height()
        self.set_pos_vertical_bar(pos_x, pos_y, img.get_width())
        self.surface.blit(img, (pos_x, pos_y))

    def set_pos_vertical_bar(self, pos_x, pos_y, width):
        self.vertical_pos_x = pos_x
        self.vertical_pos_y = pos_y
        self.vertical_width = width

    def get_pos_vertical_bar(self):
        return [self.vertical_pos_x, self.vertical_pos_y, self.vertical_width]

    def top_sidebar(self):
        img = pygame.image.load("Day09_18_09_2025\\hanged\\src\\top_bar.png")
        img = pygame.transform.scale(img, (250, 33))
        img.convert()
        self.set_top_sidebar_size(img.get_height(), img.get_width())
        self.surface.blit(
            img, (self.get_pos_vertical_bar()[0], self.get_pos_vertical_bar()[1])
        )

    def set_top_sidebar_size(self, height, width):
        self.top_sidebar_height = height
        self.top_sidebar_width = width

    def get_top_sidebar_size(self):
        return [self.top_sidebar_width, self.top_sidebar_height]

    def diagonal_bar(self):
        img = pygame.image.load("Day09_18_09_2025\\hanged\\src\\diagonal_bar.png")
        img = pygame.transform.scale(img, (55, 50))
        img.convert()
        self.surface.blit(
            img,
            (
                (self.get_pos_vertical_bar()[0] + self.get_pos_vertical_bar()[2]),
                self.get_pos_vertical_bar()[1] + self.get_top_sidebar_size()[1],
            ),
        )

    def rope(self):
        img = pygame.image.load("Day09_18_09_2025\\hanged\\src\\rope.png")
        img = pygame.transform.scale(img, (25, 90))
        img.convert()
        self.surface.blit(
            img,
            (
                self.get_pos_vertical_bar()[0] + self.get_top_sidebar_size()[0] / 1.5,
                self.get_pos_vertical_bar()[1] + self.get_top_sidebar_size()[1],
            ),
        )

    def pos(self, _pos_x, _pos_y):
        self.pos_x = _pos_x
        self.pos_y = _pos_y
