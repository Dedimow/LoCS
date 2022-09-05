import pygame
from zsettings import *

#initialize list for player inventory
global player_inventory
player_inventory = []

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, groups, obstacle_sprites, equipment_sprites, create_attack, destroy_weapon, switch_weapons):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load('E:\Python Scripts\LoCS2\LoCS\Assets\char_idle_down.png'), (SCALEX, SCALEY)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -20)

        self.status = 'down'

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        

        self.obstacle_sprites = obstacle_sprites
        self.equipment_sprites = equipment_sprites


        #weapon
        self.create_attack = create_attack
        self.destroy_weapon = destroy_weapon
        self.switch_weapons = switch_weapons
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

    def switch_weapons(self):
        if self.weapon_index == 3:
            self.weapon_index = 1
        else:
            self.weapon_index +=1

        self.weapon = list(weapon_data.keys())[self.weapon_index]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

        #attack input
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()

        #switch weapons
        if keys[pygame.K_1]:
            self.switch_weapons()
            print(self.weapon)
            print(self.weapon_index)

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



    def item_pickup(self, item_name):
                print(item_name)
                if item_name not in player_inventory:
                    player_inventory.append(item_name)
                print(player_inventory)

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                        
                    if self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right
                        
            
            for sprite in self.equipment_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        
                        self.item_pickup(sprite)
                    if self.direction.x < 0: #moving left
                        
                        self.item_pickup(sprite)
            
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):              
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                        
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
                        

            for sprite in self.equipment_sprites:
                if sprite.hitbox.colliderect(self.hitbox):              
                    if self.direction.y > 0: #moving down
                        
                        self.item_pickup(sprite)
                    if self.direction.y < 0: #moving up
                        
                        self.item_pickup(sprite)
            
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_weapon()           


    def update(self):
        self.input()
        self.cooldowns()
        
        self.move(self.speed)