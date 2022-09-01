from pickle import FALSE
from tkinter import CURRENT, TRUE
import pygame
import os
from random import randint

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1440, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Legend of Coq Shaddeaux")

####ITEMS AND VARIABLES#####

###COLORS####
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 140, 0)
BROWN = (160, 82, 45)
SILVER = (169, 169, 169)

###WEAPON HITBOXES####
SWORD = (35, 40) 
BOMB = (50, 50) 
ARROW = (10, 65)
SHIELD = (55, 20)

###CLASSES FOR SPRITES####
class Tree(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load(os.path.join(r"Environment_tree.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load(os.path.join(r"char_idle_down.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.direct = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys [pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed

class CameraGroup(pygame.sprite.Group):
    def __init__(self): #Gives the camera group the same properties as the player group
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
        #camera offset##
        self.offset = pygame.math.Vector2(WIDTH/2, HEIGHT/2)

        #ground##
        self.ground_surf = grass_background.convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0, 0))

    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self(WIDTH/2)
        self.offset.y = target.rect.centery - self(HEIGHT/2)


    def custom_draw(self, player):
        
        self.center_target_camera(player)
        
        #ground##
        ground_offset = self.ground_rect.topleft + self.offset
        self.display_surface.blit(self.ground_surf. ground_offset)

        #active elements##
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
           offset_pos = sprite.rect.topleft + self.offset 
           self.WIN.blit(sprite.image, offset_pos)


##CURRENT WEAPON###------**START WITH SWORD**---------
global CURRENT_WEAPON
global WEAPON_COLOR
global WEAPON_TEXT

CURRENT_WEAPON = SWORD
WEAPON_TEXT = "Sword Equipped"
WEAPON_COLOR = SILVER

###INFRASTRUCTURE VARIABLES####
FPS = 60
VELO = 10
HITBOXMAX = 1
TEXT_FONT = pygame.font.SysFont('helvetica', 50)
TEXT_COLOR = RED
VECTOR = (0,0)
PROJECTILEVECTOR = (0,0)

###IMAGE FILES####

#ENVIRONMENT IMAGES##
grass_background = pygame.transform.scale(pygame.image.load(os.path.join(r"background_grass.png")), (WIDTH, HEIGHT))
desert_background = pygame.transform.scale(pygame.image.load(os.path.join(r"background_sand.png")), (WIDTH/4, HEIGHT/4))
env_tree = pygame.transform.scale(pygame.image.load(os.path.join(r"Environment_tree.png")), (125, 100))
env_rock = pygame.transform.scale(pygame.image.load(os.path.join(r"environment_rock1.png")), (55, 55))

#CHAR IMAGES##
char_model_standby = pygame.transform.scale(pygame.image.load(os.path.join(r"char_idle_down.png")), (100,75))
char_shieldup_image = pygame.transform.scale(pygame.image.load(os.path.join(r"character_shieldup_down.png")), (100,75))
char_sword_attack_image = pygame.transform.scale(pygame.image.load(os.path.join(r"character_attack1_down.png")), (100,75))
char_sword_powera_image = pygame.transform.scale(pygame.image.load(os.path.join(r"character_attack2_powerup_down.png")), (100,75))
char_sword_powera_image2 = pygame.transform.scale(pygame.image.load(os.path.join(r"character_attack2_swing_down.png")), (100,75))

#WEAPON IMAGES##
sword_image = pygame.transform.scale(pygame.image.load(os.path.join(r"bitsword.png")), (50,37))
bomb_image_1 = pygame.transform.scale(pygame.image.load(os.path.join(r"weapon_energyball1.png")), (50,50)) 
bomb_image_2 = pygame.transform.scale(pygame.image.load(os.path.join(r"weapon_energyball2.png")), (50,50))
bomb_image_3 = pygame.transform.scale(pygame.image.load(os.path.join(r"weapon_energyball3.png")), (50,50))
arrow_image = pygame.transform.scale(pygame.image.load(os.path.join(r"weapon_arrow1.png")), (50, 50))

##GROUPS###
camera_group = CameraGroup()
player = Player((640,360),camera_group)

###PYGAME EVENTS####
CHAR_ATTACK = pygame.USEREVENT +1
CHAR_SWTICH_WEAPON = pygame.USEREVENT +2

###FUNCTIONS####----------------------------------------------------------

def draw_window(CHAR_RECT, HITBOXCOUNTER, WEAPON_TEXT, WEAPON_COLOR):
    WIN.blit(grass_background, (0, 0))
    WIN.blit(desert_background, (WIDTH, HEIGHT))
    
    for t in range(4):
        random_x = randint(0, WIDTH)
        random_y = randint(0, HEIGHT)
        Tree((random_x, random_y), camera_group)

    if CURRENT_WEAPON == SHIELD:
        if VECTOR == DOWN: 
            WIN.blit(char_shieldup_image, (CHAR_RECT.x, CHAR_RECT.y))
        if VECTOR == UP: 
            WIN.blit((pygame.transform.rotate(char_shieldup_image, 180)), (CHAR_RECT.x, CHAR_RECT.y))
        if VECTOR == LEFT: 
            WIN.blit((pygame.transform.rotate(char_shieldup_image, 270)), (CHAR_RECT.x, CHAR_RECT.y))
        if VECTOR == RIGHT: 
            WIN.blit((pygame.transform.rotate(char_shieldup_image, 90)), (CHAR_RECT.x, CHAR_RECT.y))
    else:
        if VECTOR == DOWN: 
            WIN.blit(char_model_standby, (CHAR_RECT.x, CHAR_RECT.y))
        if VECTOR == UP: 
            WIN.blit((pygame.transform.rotate(char_model_standby, 180)), (CHAR_RECT.x, CHAR_RECT.y))
        if VECTOR == LEFT: 
            WIN.blit((pygame.transform.rotate(char_model_standby, 270)), (CHAR_RECT.x, CHAR_RECT.y))
        if VECTOR == RIGHT: 
            WIN.blit((pygame.transform.rotate(char_model_standby, 90)), (CHAR_RECT.x, CHAR_RECT.y))

    #Show currently equipped weapon##
    draw_weapon_switch = TEXT_FONT.render(WEAPON_TEXT, 1, WEAPON_COLOR)
    WIN.blit(draw_weapon_switch, (
        WIDTH//10+25 - draw_weapon_switch.get_width()//2,
        HEIGHT//10-35 - draw_weapon_switch.get_height()//2))
     
    pygame.display.update()

#-------^^^WINDOW FUNCTION ABOVE^^^------##

def CHAR_MOVEMENT(keys_pressed, CHAR_RECT):
    
    ###GLOBAL VARIABLES####
    global VECTOR
    global PROJECTILEVECTOR
    global UP
    global DOWN
    global LEFT
    global RIGHT

    ##VECTOR TUPLES###
    UP = (CHAR_RECT.width//2 - 13,-50)
    DOWN = (CHAR_RECT.width//2 - 13, CHAR_RECT.height + 30)
    LEFT = (-30, -CHAR_RECT.height//-2 - 20)
    RIGHT = (CHAR_RECT.width + 8, -CHAR_RECT.height//-2 - 20)

    ##MOVEMENT CONTROLS AND VECTOR DETERMINATION####
    if keys_pressed[pygame.K_a] :#left
        CHAR_RECT.x -= VELO
        VECTOR = LEFT
    if keys_pressed[pygame.K_d] :#right
        CHAR_RECT.x += VELO
        VECTOR = RIGHT
    if keys_pressed[pygame.K_w] :#up
        CHAR_RECT.y -= VELO
        VECTOR = UP
    if keys_pressed[pygame.K_s] :#down
        CHAR_RECT.y += VELO
        VECTOR = DOWN

    ##HANDLE PROJECTILE WEAPON RANGE AND DIRECTION RELATIVE TO PLAYER DIRECTION###
    if CURRENT_WEAPON == BOMB:
        PROJECTILERANGE = 100
    elif CURRENT_WEAPON == ARROW:
        PROJECTILERANGE = 200    
    elif CURRENT_WEAPON == SWORD or CURRENT_WEAPON == SHIELD:
        PROJECTILERANGE = 0

    if VECTOR == UP:
        PROJECTILEVECTOR = (0, -PROJECTILERANGE)
    elif VECTOR == DOWN:
        PROJECTILEVECTOR = (0, PROJECTILERANGE)
    elif VECTOR == RIGHT:
        PROJECTILEVECTOR = (PROJECTILERANGE, 0)
    elif VECTOR == LEFT:
        PROJECTILEVECTOR = (-PROJECTILERANGE, 0) 

#-------^^^CHARACTER MOVEMENT FUNCTION ABOVE^^^------##

def switch_weapons(keys_pressed):  
    global CURRENT_WEAPON
    global WEAPON_COLOR
    global WEAPON_TEXT

    ##SWITCH WEAPONS USING NUMBER KEYS###
    if keys_pressed[pygame.K_1]:
        CURRENT_WEAPON = SWORD
        WEAPON_TEXT = "Sword Equipped"
        WEAPON_COLOR = SILVER
        
    if keys_pressed[pygame.K_2]:
        CURRENT_WEAPON = SHIELD
        WEAPON_TEXT = "Shield Equipped"
        WEAPON_COLOR = BLUE
                            
    if keys_pressed[pygame.K_3]:
        CURRENT_WEAPON = ARROW
        WEAPON_TEXT = "Arrow Equipped"
        WEAPON_COLOR = BROWN
        
    if keys_pressed[pygame.K_4]:
        CURRENT_WEAPON = BOMB
        WEAPON_TEXT = "Bomb Equipped"
        WEAPON_COLOR = ORANGE

#-------^^^SWITCH WEAPONS FUNCTION ABOVE^^^------##        

def quit(keys_pressed):
    if keys_pressed[pygame.K_PAGEDOWN]:
        pygame.quit()

#-------^^^QUIT FUNCTION ABOVE^^^------##

def main():
    CHAR_RECT = pygame.Rect(300, 400, 100, 75)
    
    HITBOXCOUNTER = []
    
    global CURRENT_WEAPON
    global WEAPON_COLOR
    global UP
    global DOWN
    global LEFT
    global RIGHT


    clock = pygame.time.Clock()
    run = TRUE

    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = FALSE
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                #unpack tuple variable for hitbox adjustment based on character vector
                (xadj , yadj) = VECTOR
                #unpack tuple variable for weapon hitbox
                (currentweaponwidth, currentweaponheight) = CURRENT_WEAPON
                #unpack tuple variable for projectile hitbox adjustment
                (xprojadj, yprojadj) = PROJECTILEVECTOR                
                
                
                
                if (event.key == pygame.K_RCTRL) and (len(HITBOXCOUNTER) < HITBOXMAX):

                    if CURRENT_WEAPON == SWORD:
                        HIT_BOX = pygame.Rect(CHAR_RECT.x + xadj + xprojadj, CHAR_RECT.y + yadj + yprojadj, currentweaponwidth, currentweaponheight)
                        HITBOXCOUNTER.append(HIT_BOX)
                        
                    elif CURRENT_WEAPON == SHIELD:
                        HIT_BOX = pygame.Rect(CHAR_RECT.x + xadj + xprojadj, CHAR_RECT.y + yadj + yprojadj, currentweaponwidth, currentweaponheight)
                        HITBOXCOUNTER.append(HIT_BOX)
                    
                    elif CURRENT_WEAPON == BOMB:
                        HIT_BOX = pygame.Rect(CHAR_RECT.x + xadj + xprojadj - 10, CHAR_RECT.y + yadj + yprojadj, currentweaponwidth, currentweaponheight)
                        HITBOXCOUNTER.append(HIT_BOX)
                    
                    elif CURRENT_WEAPON == ARROW:
                        HIT_BOX = pygame.Rect(CHAR_RECT.x + xadj + xprojadj, CHAR_RECT.y + yadj + yprojadj, currentweaponwidth, currentweaponheight)
                        HITBOXCOUNTER.append(HIT_BOX)
                                       
        for HIT_BOX in HITBOXCOUNTER:
        
            if CURRENT_WEAPON == SWORD:
                if VECTOR == LEFT:
                    WIN.blit((pygame.transform.rotate(char_sword_attack_image ,270)), (CHAR_RECT.x, CHAR_RECT.y))#this adds a new image to the screen rather than changing the onscreen image for CHAR_RECT
                elif VECTOR == RIGHT:
                    WIN.blit((pygame.transform.rotate(char_sword_attack_image ,90)), (CHAR_RECT.x, CHAR_RECT.y))    
                elif VECTOR == UP:
                    WIN.blit((pygame.transform.rotate(char_sword_attack_image ,180)), (CHAR_RECT.x, CHAR_RECT.y))
                elif VECTOR == DOWN:
                    WIN.blit((pygame.transform.rotate(char_sword_attack_image ,0)), (CHAR_RECT.x, CHAR_RECT.y))
                
                pygame.display.update()
                pygame.time.delay(200)
                HITBOXCOUNTER.remove(HIT_BOX)
                
            
            elif CURRENT_WEAPON == SHIELD:
                if VECTOR == LEFT:
                    WIN.blit((pygame.transform.rotate(char_shieldup_image ,270)), (CHAR_RECT.x, CHAR_RECT.y))
                elif VECTOR == RIGHT:
                    WIN.blit((pygame.transform.rotate(char_shieldup_image ,90)), (CHAR_RECT.x, CHAR_RECT.y))
                elif VECTOR == UP:
                    WIN.blit((pygame.transform.rotate(char_shieldup_image, 180)), (CHAR_RECT.x, CHAR_RECT.y))
                elif VECTOR == DOWN:
                    WIN.blit((pygame.transform.rotate(char_shieldup_image, 0)), (CHAR_RECT.x, CHAR_RECT.y))
                                
                pygame.display.update()
                pygame.time.delay(250)
                HITBOXCOUNTER.remove(HIT_BOX)

            elif CURRENT_WEAPON == BOMB:
                WIN.blit(bomb_image_1, (HIT_BOX.x, HIT_BOX.y))
                pygame.display.update()
                pygame.time.delay(80)
                
                WIN.blit(bomb_image_2, (HIT_BOX.x, HIT_BOX.y))
                pygame.display.update()
                pygame.time.delay(80)

                WIN.blit(bomb_image_3, (HIT_BOX.x, HIT_BOX.y))
                pygame.display.update()
                pygame.time.delay(80)

                HITBOXCOUNTER.remove(HIT_BOX)

            elif CURRENT_WEAPON == ARROW:
                if VECTOR == LEFT:
                    WIN.blit((pygame.transform.rotate(arrow_image, 270)),(HIT_BOX.x, HIT_BOX.y))
                elif VECTOR == RIGHT:
                    WIN.blit((pygame.transform.rotate(arrow_image, 90)), (HIT_BOX.x, HIT_BOX.y))
                elif VECTOR == UP:
                    WIN.blit((pygame.transform.rotate(arrow_image, 180)), (HIT_BOX.x, HIT_BOX.y))
                elif VECTOR == DOWN:
                    WIN.blit((pygame.transform.rotate(arrow_image, 0)), (HIT_BOX.x, HIT_BOX.y))
                
                pygame.display.update()
                pygame.time.delay(150)
                HITBOXCOUNTER.remove(HIT_BOX)
                               

        keys_pressed = pygame.key.get_pressed()
        CHAR_MOVEMENT(keys_pressed, CHAR_RECT)
        switch_weapons(keys_pressed)

        draw_window(CHAR_RECT, HITBOXCOUNTER, WEAPON_TEXT, WEAPON_COLOR)

        quit(keys_pressed)

    main()

if __name__ == "__main__":
    main()