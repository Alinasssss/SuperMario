import pygame
from tiles import Tiles


class Map:
    def __init__(self,screen, file_map, platforms_top, platforms_bottom, left_walls, right_walls, floor_tiles):
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
                    platform_bottom = Tiles(screen, x, y+32, 'platform')
                    wall_left = Tiles(screen, x-17, y+28, 'wall')
                    wall_right = Tiles(screen, x+15, y+28, 'wall')
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

                if p == 'w':
                    ''''''

                if p == '\n':
                    y += 32
                x += 32
            x = 32
        file.close()
