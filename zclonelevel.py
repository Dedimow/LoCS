import pygame
from ztile import *
from zplayer import Player
from zsettings import *
from random import randint
from zweapon import Weapon

class Level:
    def __init__(self):

       #get the display surface
       self.display_surface = pygame.display.get_surface()
       
       # sprite group setup
       self.visible_sprites = YSortCameraGroup()
       self.obstacle_sprites = pygame.sprite.Group()
       self.equipment_sprites = pygame.sprite.Group()

       #attack sprites
       self.current_attack = None

       #sprite setup
       self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                #display environment objects
                if col == 'tv':
                    treemodel = randint(1 , 4)
                    if treemodel == 1:
                        Tree1((x,y),[self.visible_sprites, self.obstacle_sprites])
                    if treemodel == 2:
                        Tree2((x,y),[self.visible_sprites, self.obstacle_sprites])
                    if treemodel == 3:
                        Tree3((x,y),[self.visible_sprites, self.obstacle_sprites])
                    if treemodel == 4:
                        Tree4((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == 'ov':
                    Ore1((x,y),[self.visible_sprites])
                if col == 'rv':
                    rockmodel = randint(1 , 3)
                    if rockmodel == 1:
                        Rock1((x,y),[self.visible_sprites, self.obstacle_sprites])
                    if rockmodel == 2:
                        Rock2((x,y),[self.visible_sprites, self.obstacle_sprites])
                    if rockmodel == 3:
                        Rock3((x,y),[self.visible_sprites, self.obstacle_sprites])
                
                #display player model
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites, self.equipment_sprites, self.create_attack, self.destroy_weapon)

                #display equipment/item objects
                if col == 's1':
                    Screw1((x,y), [self.visible_sprites, self.equipment_sprites])

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_weapon(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        #getting the offset 
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)