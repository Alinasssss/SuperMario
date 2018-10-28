import pygame
from tiles import Tiles

class Map:
    def __init__(self,screen,fileMap,platformsTop,platformsBottom,leftWalls,rightWalls,floorTiles,brickTiles, mysteryTiles):
        file = open(fileMap, 'r')
        lines = file.readlines()

        x = 0
        y = 0

        for line in lines:
            for p in line:
                if p == 'f':

                    #create a 4 sided rectangle, with top collidable with marios feet
                    # bottom collidable with mario head
                    # and left and right wall collidable with mario right or left

                    #4 sided rectangle with independent collidable parts----------
                    # this will serve as a mask for every game object that needs to
                    # be collidable
                    platformTop = Tiles(screen,x,y,'platform')
                    platformBottom = Tiles(screen,x,y+32,'platform')
                    wallLeft = Tiles(screen,x-17,y+28,'wall')
                    wallRight = Tiles(screen,x+15,y+28,'wall')
                    #-------------------------------------------------------------


                    #game object representation of floor tile
                    floorTile = Tiles(screen,x+1,y+32,'floor')

                    platformsTop.add(platformTop)
                    platformsBottom.add(platformBottom)
                    leftWalls.add(wallLeft)
                    rightWalls.add(wallRight)
                    floorTiles.add(floorTile)

                #continue adding if statement for objects you
                #want to add in the map.txt file,
                 

                if p == 'b':
                    platformTop = Tiles(screen,x,y,'platform')
                    platformBottom = Tiles(screen,x,y+32,'platform')
                    wallLeft = Tiles(screen,x-17,y+28,'wall')
                    wallRight = Tiles(screen,x+15,y+28,'wall')

                    brickTile = Tiles(screen,x,y+32,'brick')

                    platformsTop.add(platformTop)
                    platformsBottom.add(platformBottom)
                    leftWalls.add(wallLeft)
                    rightWalls.add(wallRight)
                    brickTiles.add(brickTile)

                if p == 'm':
                    platformTop = Tiles(screen,x,y,'platform')
                    platformBottom = Tiles(screen,x,y+32,'platform')
                    wallLeft = Tiles(screen,x-17,y+28,'wall')
                    wallRight = Tiles(screen,x+15,y+28,'wall')

                    mysteryTile = Tiles(screen,x,y+32,'mystery')

                    platformsTop.add(platformTop)
                    platformsBottom.add(platformBottom)
                    leftWalls.add(wallLeft)
                    rightWalls.add(wallRight)
                    mysteryTiles.add(mysteryTile)

                if p == '\n':
                    y += 32
                x += 32
            x = 32
        file.close()