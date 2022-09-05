import pygame, sys
import os
from zclonelevel import Level
from zsettings import *

# pygame.font.init()
# pygame.mixer.init()


###BASIC SETUP THAT RUNS GAME####
class Game:
    def __init__(self):
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Legend of Coq Shaddeaux")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(grass_background, ORIGIN)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
##^^^^-------GAME RUNNING FUNCTION ABOVE------^^^^###


####ITEMS AND VARIABLES#####

###COLORS####
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 140, 0)
BROWN = (160, 82, 45)
SILVER = (169, 169, 169)

###WEAPON HITBOXES####
# SWORD = (35, 40) 
# BOMB = (50, 50) 
# ARROW = (10, 65)
# SHIELD = (55, 20)

##CURRENT WEAPON###------**START WITH SWORD**---------
global CURRENT_WEAPON
global WEAPON_COLOR
global WEAPON_TEXT

# CURRENT_WEAPON = SWORD
# WEAPON_TEXT = "Sword Equipped"
WEAPON_COLOR = SILVER

###INFRASTRUCTURE VARIABLES####

# TEXT_FONT = pygame.font.SysFont('helvetica', 50)

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

###FUNCTIONS####----------------------------------------------------------


#-------^^^WINDOW FUNCTION ABOVE^^^------##


#-------^^^CHARACTER MOVEMENT FUNCTION ABOVE^^^------##

# def switch_weapons(keys_pressed):  
#     global CURRENT_WEAPON
#     global WEAPON_COLOR
#     global WEAPON_TEXT

#     ##SWITCH WEAPONS USING NUMBER KEYS###
#     if keys_pressed[pygame.K_1]:
#         CURRENT_WEAPON = SWORD
#         WEAPON_TEXT = "Sword Equipped"
#         WEAPON_COLOR = SILVER
        
#     if keys_pressed[pygame.K_2]:
#         CURRENT_WEAPON = SHIELD
#         WEAPON_TEXT = "Shield Equipped"
#         WEAPON_COLOR = BLUE
                            
#     if keys_pressed[pygame.K_3]:
#         CURRENT_WEAPON = ARROW
#         WEAPON_TEXT = "Arrow Equipped"
#         WEAPON_COLOR = BROWN
        
#     if keys_pressed[pygame.K_4]:
#         CURRENT_WEAPON = BOMB
#         WEAPON_TEXT = "Bomb Equipped"
#         WEAPON_COLOR = ORANGE

#-------^^^SWITCH WEAPONS FUNCTION ABOVE^^^------##        


# #-------^^^QUIT FUNCTION ABOVE^^^------##

