import pygame
from mario import Mario
from pygame.sprite import Group
from map import Map
import events as e 
from settings import LIGHTBLUE, WIDTH, HEIGHT
from entity_gamemaster import EntityGameMaster
from enemy_gamemaster import EnemyGameMaster
from gui import GUI


def run_game():
    # initialize fonts
    pygame.init()

    # initialize sound mixer
    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # to hold all tiles from the map
    platforms_top = Group()
    platforms_bottom = Group()
    left_walls = Group()
    right_walls = Group()
    floor_tiles = Group()

    # actual game objects
    floor_tiles = Group()
    brick_tiles = Group()
    mystery_tiles = Group()
    pole = Group()
    fireballs = Group()
    
    # create a viewport and pass all objects into it for
    # easier management
    viewport = Group()

    entity_gamemaster = EntityGameMaster()
    enemy_gamemaster = EnemyGameMaster()

    gui = GUI(screen)

    mario = Mario(screen, entity_gamemaster, gui)

    # create our map level and all objects within it
    map = Map(screen, 'resources/map.txt', platforms_top, platforms_bottom, left_walls, right_walls, floor_tiles,
              brick_tiles, mystery_tiles, pole, enemy_gamemaster, mario)

    # pass all objects groups into viewport so that they get updated with mario x movement creating a scrolling effect
    viewport.add(platforms_top)
    viewport.add(platforms_bottom)
    viewport.add(left_walls)
    viewport.add(right_walls)
    viewport.add(floor_tiles)
    viewport.add(brick_tiles)
    viewport.add(mystery_tiles)
    viewport.add(pole)

    viewport.add(entity_gamemaster.fireflowers)
    viewport.add(entity_gamemaster.mushrooms)
    viewport.add(entity_gamemaster.one_up_mushrooms)
    viewport.add(entity_gamemaster.starmen)

    viewport.add(enemy_gamemaster.goombas)
    viewport.add(enemy_gamemaster.koopas)

    while True:
        screen.fill(LIGHTBLUE)

        entity_gamemaster.update()
        enemy_gamemaster.update()

        e.check_events(mario, platforms_top, screen, fireballs)
        e.check_collisions(mario, platforms_top, platforms_bottom, left_walls, right_walls, fireballs)

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
        pole.update()
        fireballs.update(platforms_top, left_walls, right_walls, enemy_gamemaster)
        # -------------------------------------------------------------

        mario.update(viewport, pole)
        gui.show_score()
        pygame.display.flip()


run_game()
