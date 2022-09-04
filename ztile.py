import pygame
from zsettings import *


###ENVIRONMENT OBJECTS####
class Tree1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\Environment_tree.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)

class Tree2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\Environment_tree2.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)

class Tree3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\Environment_tree3.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)

class Tree4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\Environment_tree4.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)

class Rock1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\environment_rock1.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -8)

class Rock2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\environment_rock2.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -8)

class Rock3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\environment_rock3.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -8)

class Ore1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\environment_ore1.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -8)


###EQUIPMENT/ITEM OBJECTS####

class Screw1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(r'E:\Python Scripts\LoCS2\LoCS\Assets\item_screw.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -8)
