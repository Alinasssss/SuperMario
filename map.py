import pygame
from tiles import Tiles

class Map:
    def __init__(self,screen,fileMap,platforms,leftWalls,rightWalls):
        file = open(fileMap, 'r')
        lines = file.readlines()

        x = -16
        y = 0

        for line in lines:
            for p in line:
                if p == 'f':

                    #create a w sided rectangle, with top and bottom collidible with head and feet
                    # and left and right wall collidible with mario right or left
                    platformTop = Tiles(screen,x,y,'platform')
                    platformBottom = Tiles(screen,x,y+32,'platform')
                    wallLeft = Tiles(screen,x-19,y+28,'wall')
                    wallRight = Tiles(screen,x+18,y+28,'wall')

                    platforms.add(platformTop)
                    platforms.add(platformBottom)
                    leftWalls.add(wallLeft)
                    rightWalls.add(wallRight)
                if p == 'w':
                    ''''''
                                    
                if p == '\n':
                    y += 32
                x += 32
            x = 32
        file.close()