import pygame
from pygame.sprite import Sprite


class Tiles(Sprite):
    def __init__(self, screen, x, y, tile_type):
        super(Tiles, self).__init__()

        # get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        # create wall or floor tile depending on type input
        if tile_type == 'platform':
            self.image = pygame.image.load('resources/Images/floor.gif')
        if tile_type == 'wall':
            self.image = pygame.image.load('resources/Images/wall.gif')
        if tile_type == 'floor':
            self.image = pygame.image.load('resources/Images/floorTile.gif')
        if tile_type == 'brick':
            self.image = pygame.image.load('resources/Images/hitTile.gif')
        if tile_type == 'mystery':
            self.image = pygame.image.load('resources/Images/mysteryBox1.gif')
        if tile_type == 'metal':
            self.image = pygame.image.load('resources/Images/metalTile.gif')
        if tile_type == 'pole':
            self.image = pygame.image.load('resources/Images/pole.gif')


        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.rect.centerx = x
        self.rect.bottom = y
        
        self.center = float(self.rect.centerx)

        self.blitme()
            
    def update(self):
        self.mask = pygame.mask.from_surface(self.image)            
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image,self.rect)
