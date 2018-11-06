import pygame
from tiles import Tiles
from goomba import Goomba
from koopa import Koopa


class Map:
    def __init__(self, screen, file_map, platforms_top, platforms_bottom, left_walls, right_walls, floor_tiles, brick_tiles, mystery_tiles, pole, clouds, hills, bushes, pipes, metal_tiles, castle, enemy_gamemaster, mario):
        file = open(file_map, 'r')
        lines = file.readlines()

        x = 0
        y = 0

        for line in lines:
            for p in line:
                if p == 'f':

                    # create a 4 sided rectangle, with top collidable with mario's feet
                    # bottom collidable with mario head
                    # and left and right wall collidable with mario right or left

                    # 4 sided rectangle with independent collidable parts - - - - -
                    # this will serve as a mask for every game object that needs to be collidable
                    platform_top = Tiles(screen, x, y, 'platform')
                    platform_bottom = Tiles(screen, x, y+34, 'platform')
                    wall_left = Tiles(screen, x-17, y+28, 'wall')
                    wall_right = Tiles(screen, x+18, y+28, 'wall')
                    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                    # game object representation of floor tile
                    floor_tile = Tiles(screen, x+1, y+32, 'floor')

                    platforms_top.add(platform_top)
                    platforms_bottom.add(platform_bottom)
                    left_walls.add(wall_left)
                    right_walls.add(wall_right)
                    floor_tiles.add(floor_tile)

                # continue adding if statement for objects you
                # want to add in the map.txt file

                if p == 'b':
                    platform_top = Tiles(screen,x,y+4,'platform')
                    platform_bottom = Tiles(screen,x,y+34,'platform')
                    wall_left = Tiles(screen,x-17,y+28,'wall')
                    wall_right = Tiles(screen,x+18,y+28,'wall')

                    brick_tile = Tiles(screen,x,y+32,'brick')

                    platforms_top.add(platform_top)
                    platforms_bottom.add(platform_bottom)
                    left_walls.add(wall_left)
                    right_walls.add(wall_right)
                    brick_tiles.add(brick_tile)

                if p == 'm':
                    platform_top = Tiles(screen,x,y+4,'platform')
                    platform_bottom = Tiles(screen,x,y+34,'platform')
                    wall_left = Tiles(screen,x-17,y+28,'wall')
                    wall_right = Tiles(screen,x+18,y+28,'wall')

                    mystery_tile = Tiles(screen,x,y+32,'mystery')

                    platforms_top.add(platform_top)
                    platforms_bottom.add(platform_bottom)
                    left_walls.add(wall_left)
                    right_walls.add(wall_right)
                    mystery_tiles.add(mystery_tile)

                if p == 't':
                    platform_top = Tiles(screen, x, y + 4, 'platform')
                    platform_bottom = Tiles(screen, x, y + 34, 'platform')
                    wall_left = Tiles(screen, x - 17, y + 28, 'wall')
                    wall_right = Tiles(screen, x + 18, y + 28, 'wall')

                    pipeTop = Tiles(screen, x, y + 32, 'pipetop')

                    platforms_top.add(platform_top)
                    platforms_bottom.add(platform_bottom)
                    left_walls.add(wall_left)
                    right_walls.add(wall_right)
                    pipes.add(pipeTop)

                if p == 'x':
                    platform_top = Tiles(screen, x, y + 4, 'platform')
                    platform_bottom = Tiles(screen, x, y + 34, 'platform')
                    wall_left = Tiles(screen, x - 17, y + 28, 'wall')
                    wall_right = Tiles(screen, x + 18, y + 28, 'wall')

                    pipeExtension = Tiles(screen, x, y + 32, 'pipebottom')

                    platforms_top.add(platform_top)
                    platforms_bottom.add(platform_bottom)
                    left_walls.add(wall_left)
                    right_walls.add(wall_right)
                    pipes.add(pipeExtension)

                if p == 'l':
                    platform_top = Tiles(screen, x, y + 4, 'platform')
                    platform_bottom = Tiles(screen, x, y + 34, 'platform')
                    wall_left = Tiles(screen, x - 17, y + 28, 'wall')
                    wall_right = Tiles(screen, x + 18, y + 28, 'wall')

                    metal = Tiles(screen, x, y + 32, 'metal')

                    platforms_top.add(platform_top)
                    platforms_bottom.add(platform_bottom)
                    left_walls.add(wall_left)
                    right_walls.add(wall_right)
                    metal_tiles.add(metal)

                if p == 'p':
                    flag_pole = Tiles(screen, x, y + 32, 'pole')
                    pole.add(flag_pole)

                if p == 'g':
                    flag = Tiles(screen, x - 16, y + 36, 'flag')
                    pole.add(flag)

                if p == 'c':
                    cloud1 = Tiles(screen, x, y + 32, 'cloud1')
                    clouds.add(cloud1)

                if p == 'v':
                    cloud2 = Tiles(screen, x, y + 32, 'cloud2')
                    clouds.add(cloud2)

                if p == 'd':
                    cloud3 = Tiles(screen, x, y + 32, 'cloud3')
                    clouds.add(cloud3)

                if p == 'h':
                    bighill = Tiles(screen, x, y + 32, 'bighill')
                    hills.add(bighill)

                if p == 'j':
                    smallhill = Tiles(screen, x, y + 32, 'smallhill')
                    hills.add(smallhill)

                if p == 'y':
                    bush1 = Tiles(screen, x, y + 32, 'bush1')
                    bushes.add(bush1)

                if p == 'u':
                    bush2 = Tiles(screen, x, y + 32, 'bush2')
                    bushes.add(bush2)

                if p == 'i':
                    bush3 = Tiles(screen, x, y + 32, 'bush3')
                    bushes.add(bush3)

                if p == 's':
                    cast = Tiles(screen, x, y + 32, 'castle')
                    castle.add(cast)

                if p == 'G':
                    goomba = Goomba(screen, mario, platforms_top, left_walls, right_walls)
                    goomba.rect.center = (x, y)
                    goomba.centerx = goomba.rect.centerx
                    goomba.centery = goomba.rect.centery
                    goomba.previous_centery = goomba.centery
                    enemy_gamemaster.goombas.add(goomba)

                if p == 'K':
                    koopa = Koopa(screen, mario, platforms_top, left_walls, right_walls)
                    koopa.rect.center = (x, y)
                    koopa.centerx = koopa.rect.centerx
                    koopa.centery = koopa.rect.centery
                    koopa.previous_centery = koopa.centery
                    enemy_gamemaster.koopas.add(koopa)

                if p == '\n':
                    y += 32
                x += 32
            x = 32
        file.close()
