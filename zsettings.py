import pygame, os

#game settings and important data
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
SCALEX = 55
SCALEY = 55
ORIGIN = (0,0)

#ENVIRONMENT IMAGES##
grass_background = pygame.transform.scale(pygame.image.load(os.path.join(r"background_grass.png")), (WIDTH, HEIGHT))
desert_background = pygame.transform.scale(pygame.image.load(os.path.join(r"background_sand.png")), (WIDTH/4, HEIGHT/4))


#WEAPON DATA##
weapon_data = {
    'sword': {'cooldown':100, 'dmg':15, 'graphic':r'E:\Python Scripts\LoCS2\LoCS\Assets\weapon_sword_lowres_walpha.png'}, 
    'bomb': {'cooldown':250, 'dmg' :30, 'graphic': r'E:\Python Scripts\LoCS2\LoCS\Assets\weapon_energyball1.png'},
    'arrow': {'cooldown': 150, 'dmg': 10, 'graphic':r'E:\Python Scripts\LoCS2\LoCS\Assets\weapon_arrow1.png'},
    'shield': {'cooldown':200, 'dmg': 25, 'graphic':r'E:\Python Scripts\LoCS2\LoCS\Assets\character_shieldup_down.png'}
}


WORLD_MAP = [
['tv','tv','tv','tv','tv','tv','tv','ov','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ','p',' ','ov','ov',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ','s1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','rv',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','rv',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','rv',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','rv','rv','rv',' ',' ',' ',' ',' '],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ','rv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','rv',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','tv'],
['tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv','tv'],
]