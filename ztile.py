import pygame
from zsettings import *

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\Environment_tree.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)

class Rock1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\environment_rock1.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -8)