import pygame
import sys
from  mario import Mario
from pygame.sprite import Group
from map import Map
import events as e 
from settings import BLACK, WIDTH, HEIGHT

def App():

    #initialie sound mixer
    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen_rect = screen.get_rect()

    mario = Mario(screen)
    
    #to hold all tiles from the map, these can be used to mask any game object
    platformsTop = Group()
    platformsBottom = Group()
    leftWalls = Group()
    rightWalls = Group()

    #actual game objects
    floorTiles = Group()
    
    #create a viewport and pass all objects into it for
    #easier management
    viewport = Group()

    #create our map level and all objects within it
    map = Map(screen,'resources/map.txt',platformsTop,platformsBottom,leftWalls,rightWalls,floorTiles)

    #pass all objects groups into viewport so that
    #they get updated with mario x movement
    #creating a scrolling effect
    viewport.add(platformsTop)
    viewport.add(platformsBottom)
    viewport.add(leftWalls)
    viewport.add(rightWalls)
    viewport.add(floorTiles)
        
    while True:
        screen.fill(BLACK)
        e.checkEvents(mario,platformsTop)
        e.checkCollisions(mario,platformsTop,platformsBottom,leftWalls,rightWalls)

        #each collision part is independently handled------------------
        platformsTop.update()
        platformsBottom.update()
        leftWalls.update()
        rightWalls.update()
        #--------------------------------------------------------------
        
        #actual game objects, images, sprites, etc....................
        floorTiles.update()
        #-------------------------------------------------------------

        mario.update(viewport)
        pygame.display.flip()

App()                 