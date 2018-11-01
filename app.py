import pygame
from mario import Mario
from pygame.sprite import Group
from map import Map
import events as e 
from settings import LIGHTBLUE, WIDTH, HEIGHT
from entity_gamemaster import EntityGameMaster
from mushroom import Mushroom
from fireflower import Fireflower
from one_up_mushroom import OneUpMushroom
from starman import Starman


def run_game():
    # initialize sound mixer
    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    
    # to hold all tiles from the map
    platforms_top = Group()
    platforms_bottom = Group()
    left_walls = Group()
    right_walls = Group()
    floor_tiles = Group()

    
    #actual game objects
    floor_tiles = Group()
    brick_tiles = Group()
    mystery_tiles = Group()
    
    # create a viewport and pass all objects into it for
    # easier management
    viewport = Group()

    # create our map level and all objects within it
    map = Map(screen, 'resources/map.txt', platforms_top, platforms_bottom, left_walls, right_walls, floor_tiles,brick_tiles,mystery_tiles)

    # pass all objects groups into viewport so that they get updated with mario x movement creating a scrolling effect
    viewport.add(platforms_top)
    viewport.add(platforms_bottom)
    viewport.add(left_walls)
    viewport.add(right_walls)
    viewport.add(floor_tiles)
    viewport.add(brick_tiles)
    viewport.add(mystery_tiles)

    entity_gamemaster = EntityGameMaster()
    mushroom = Mushroom(screen, floor_tiles, left_walls, right_walls)
    fireflower = Fireflower(screen)
    one_up_mushroom = OneUpMushroom(screen, floor_tiles, left_walls, right_walls)
    starman = Starman(screen, floor_tiles, left_walls, right_walls)
    entity_gamemaster.mushrooms.add(mushroom)
    entity_gamemaster.fireflowers.add(fireflower)
    entity_gamemaster.one_up_mushrooms.add(one_up_mushroom)
    entity_gamemaster.starmen.add(starman)

    mario = Mario(screen, entity_gamemaster)
        
    while True:
        screen.fill(LIGHTBLUE)

        entity_gamemaster.update()

        e.check_events(mario, platforms_top)
        e.check_collisions(mario, platforms_top, platforms_bottom, left_walls, right_walls)

        # each collision part is independently handled------------------
        platforms_top.update()
        platforms_bottom.update()
        left_walls.update()
        right_walls.update()
        # --------------------------------------------------------------
        
        # actual game objects, images, sprites, etc....................
        floor_tiles.update()
        brick_tiles.update()
        mystery_tiles.update()
        # -------------------------------------------------------------

        mario.update(viewport)
        pygame.display.flip()


run_game()
