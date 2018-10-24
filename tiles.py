import pygame
import sys
from pygame.sprite import Sprite

class Tiles(Sprite):
    def __init__(self,screen,x,y):
        super(Tiles,self).__init__()

        #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
        #create tile
        self.image = pygame.image.load('resources/tile.gif')
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

        