import pygame
from zsettings import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status

        #graphic
        full_path = weapon_data[player.weapon]['graphic']
        
        #placement
        if direction == 'right':
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(full_path), (SCALEX, SCALEY)).convert_alpha(), 270)
            self.rect =  self.image.get_rect(midleft = player.rect.midright)
        elif direction == 'left':
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(full_path), (SCALEX, SCALEY)).convert_alpha(), 90)
            self.rect =  self.image.get_rect(midright = player.rect.midleft)
        elif direction == 'up':
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(full_path), (SCALEX, SCALEY)).convert_alpha(), 0)
            self.rect =  self.image.get_rect(midbottom = player.rect.midtop)
        elif direction == 'down':
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(full_path), (SCALEX, SCALEY)).convert_alpha(), 180)
            self.rect =  self.image.get_rect(midtop = player.rect.midbottom)    