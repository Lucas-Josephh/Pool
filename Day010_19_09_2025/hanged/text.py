class Text:
    def __init__(self, font, msg="", color=(255, 255, 255), pos=(0, 0)):
        self.font = font
        self.msg = msg
        self.color = color
        self.pos = pos
        self.visible = False
        self.surface = None
        self.rect = None

    def creer(self):
        self.surface = self.font.render(self.msg, True, self.color)
        self.rect = self.surface.get_rect(topleft=self.pos)
        self.visible = True

    def modifier(self, msg=None, color=None, pos=None):
        if msg is not None:
            self.msg = msg
        if color is not None:
            self.color = color
        if pos is not None:
            self.pos = pos
        self.surface = self.font.render(self.msg, True, self.color)
        self.rect = self.surface.get_rect(topleft=self.pos)

    def supprimer(self):
        self.visible = False

    def draw(self, surface):
        if self.visible and self.surface:
            surface.blit(self.surface, self.rect)
