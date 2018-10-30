import pygame
import sys
from pygame.sprite import Sprite

class Tiles(Sprite):
    def __init__(self,screen,x,y,type):
        super(Tiles,self).__init__()

        #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
        #create wall or floor tile depending on type input
        if type == 'platform':
            self.image = pygame.image.load('resources/floor.gif')
        if type == 'wall':
            self.image = pygame.image.load('resources/wall.gif')
        if type == 'floor':
            self.image = pygame.image.load('resources/floorTile.gif')

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.rect.centerx = x
        self.rect.bottom = y
        
        self.center = float(self.rect.centerx)

        self.blitme()
            
    def update(self):            
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image,self.rect) 

        