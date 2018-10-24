import pygame
from tiles import Tiles

class Map:
    def __init__(self,screen,fileMap,platforms,walls):
        file = open(fileMap, 'r')
        lines = file.readlines()

        c = -16
        r = 265

        for line in lines:
            for x in line:
                if x == '_':
                    tile = Tiles(screen,c,r)
                    platforms.add(tile)
                if x == '|':
                    tile = Tiles(screen,c,r)
                    walls.add(tile)
                if x == '\n':
                    r += 16
                c += 16
            c = 16
        file.close()