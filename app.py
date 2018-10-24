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
    walls = Group()
    
    #create our map level
    map = Map(screen,'resources/map.txt',platforms,walls)
    
    while True:
        screen.fill((0,0,0))
        e.checkEvents(mario,platforms)
        e.checkCollisions(mario,platforms,walls)
        platforms.update()
        walls.update()
        mario.update(platforms,walls)
        pygame.display.flip()

App()                 