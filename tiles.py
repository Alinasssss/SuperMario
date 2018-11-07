import pygame
from pygame.sprite import Sprite


class Tiles(Sprite):
    def __init__(self, screen, x, y, tile_type):
        super(Tiles, self).__init__()

        # get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        self.moving = False
        self.frames = 0
        self.status = 'new'
        self.destroy_self = False

        self.tile_type = tile_type

        # create wall or floor tile depending on type input
        if self.tile_type == 'platform':
            self.image = pygame.image.load('resources/Images/floor.gif')
        if self.tile_type == 'wall':
            self.image = pygame.image.load('resources/Images/wall.gif')
        if self.tile_type == 'floor':
            self.image = pygame.image.load('resources/Images/floorTile.gif')
        if self.tile_type == 'brick':
            self.image = pygame.image.load('resources/Images/hitTile.gif')
        if self.tile_type == 'mystery':
            self.image = pygame.image.load('resources/Images/mysteryBox1.gif')
        if self.tile_type == 'metal':
            self.image = pygame.image.load('resources/Images/metalTile.gif')
        if self.tile_type == 'pole':
            self.image = pygame.image.load('resources/Images/pole.gif')
        if self.tile_type == 'flag':
            self.image = pygame.image.load('resources/Images/flag.gif')
        if self.tile_type == 'bighill':
            self.image = pygame.image.load('resources/Images/hillBig.gif')
        if self.tile_type == 'smallhill':
            self.image = pygame.image.load('resources/Images/hillSmall.gif')
        if self.tile_type == 'cloud1':
            self.image = pygame.image.load('resources/Images/cloud1.gif')
        if self.tile_type == 'cloud2':
            self.image = pygame.image.load('resources/Images/cloud2.gif')
        if self.tile_type == 'cloud3':
            self.image = pygame.image.load('resources/Images/cloud3.gif')
        if self.tile_type == 'pipetop':
            self.image = pygame.image.load('resources/Images/pipeTop.gif')
        if self.tile_type == 'pipebottom':
            self.image = pygame.image.load('resources/Images/pipeExtension.gif')
        if self.tile_type == 'bush1':
            self.image = pygame.image.load('resources/Images/bush1.gif')
        if self.tile_type == 'bush2':
            self.image = pygame.image.load('resources/Images/bush2.gif')
        if self.tile_type == 'bush3':
            self.image = pygame.image.load('resources/Images/bush3.gif')
        if self.tile_type == 'castle':
            self.image = pygame.image.load('resources/Images/castle.gif')
        if self.tile_type == 'coin':
            self.image = pygame.image.load('resources/Images/coin.gif')

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        
        self.rect.centerx = x
        self.rect.bottom = y

        self.original_y = self.rect.bottom
        
        self.center = float(self.rect.centerx)

        self.blitme()
            
    def update(self):
        if self.destroy_self:
            print('kill myself')
            self.kill()

        #if the block has been hit and moved up, make it go back to original position
        if not self.original_y == self.rect.bottom:
            self.rect.bottom += 1
            if self.tile_type == 'coin':
                self.rect.bottom += 2
        
        if self.tile_type == 'coin' and self.rect.y >= self.original_y - 20:
            self.kill()
        
        if self.status == 'new' and self.tile_type == 'mystery':
            self.frames += 1
            
            #animate the mystery box tile
            if self.frames == 1:
                self.image = pygame.image.load('resources/Images/mysteryBox1.gif')
            if self.frames == 40:
                self.image = pygame.image.load('resources/Images/mysteryBox2.gif')
            if self.frames == 60:
                self.image = pygame.image.load('resources/Images/mysteryBox3.gif')
            if self.frames == 80:
                self.frames = 0

        if self.status == 'used':
            self.image = pygame.image.load('resources/Images/mysteryBoxUsed.gif')
                    
        
        self.mask = pygame.mask.from_surface(self.image)            
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
