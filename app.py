import pygame
import sys
from  mario import Mario
from pygame.sprite import Group
from map import Map
import events as e 

def App():
    screen = pygame.display.set_mode((1900,700))
    screen_rect = screen.get_rect()
    mario = Mario(screen)
    
    #to hold all tiles from the map
    platforms = Group()
    leftWalls = Group()
    rightWalls = Group()
    floorTiles = Group()
    
    #create our map level
    map = Map(screen,'resources/map.txt',platforms,leftWalls,rightWalls,floorTiles)
    
    while True:
        screen.fill((0,0,0))
        e.checkEvents(mario,platforms)
        e.checkCollisions(mario,platforms,leftWalls,rightWalls)
        platforms.update()
        leftWalls.update()
        rightWalls.update()
        floorTiles.update()
        mario.update(platforms,leftWalls,rightWalls)
        pygame.display.flip()

App()                 