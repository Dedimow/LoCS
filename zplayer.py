import pygame
from zsettings import *

class Player(pygame.sprite.Sprite):
    
    #initialize list for player inventory
    player_inventory = []

    def __init__(self, pos, groups, obstacle_sprites, equipment_sprites):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load('E:\Python Scripts\LoCS2\LoCS\Assets\char_idle_down.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -20)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.equipment_sprites = equipment_sprites

    def input(self,):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self,speed):
        #normalize diagonal move speed
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        #set up horizontal collision
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')

        #set up vertical collision
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')

        self.rect.center = self.hitbox.center
        

    def item_pickup(self, player_inventory, equipment_sprites, visible_sprites):
        for sprite in self.equipment_sprites:
            if self.hitbox.x == sprite.hitbox.x or self.hitbox.y == sprite.hitbox.y:
                player_inventory.append[sprite]
                pygame.sprite.spritecollide(self.player, equipment_sprites,True)
                pygame.sprite.spritecollide(self.player, visible_sprites,True)
                self.visible_sprites.update()


                

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right
            
            
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):              
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
            
           


    def update(self):
        self.input()
        
        self.move(self.speed)