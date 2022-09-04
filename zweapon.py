import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status

        #graphic
        full_path = r'E:\Python Scripts\LoCS2\LoCS\Assets\bitsword.png'
        
        

        #placement
        if direction == 'right':
            self.image = pygame.transform.rotate(pygame.image.load(full_path).convert_alpha(), 270)
            self.rect =  self.image.get_rect(midleft = player.rect.midright)
            
        elif direction == 'left':
            self.image = pygame.transform.rotate(pygame.image.load(full_path).convert_alpha(), 90)
            self.rect =  self.image.get_rect(midright = player.rect.midleft)
        elif direction == 'up':
            self.image = pygame.transform.rotate(pygame.image.load(full_path).convert_alpha(), 0)
            self.rect =  self.image.get_rect(midbottom = player.rect.midtop)
        elif direction == 'down':
            self.image = pygame.transform.rotate(pygame.image.load(full_path).convert_alpha(), 180)
            self.rect =  self.image.get_rect(midtop = player.rect.midbottom)    