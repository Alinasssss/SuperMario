import pygame
from pygame.sprite import Sprite
from physics import *
vector = pygame.math.Vector2


class Coin(Sprite):

    def __init__(self, screen, mystery):
        super(Coin, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.origin_x = mystery.rect.x
        self.origin_y = mystery.rect.y

        self.value = 10
        self.start = True
        
        # load image of mario
        self.image = pygame.image.load('resources/Images/coin.gif').convert_alpha()
        self.rect = self.image.get_rect()

        # collision mask
        self.mask = pygame.mask.from_surface(self.image)
        
        self.vel = vector(0,0)
        self.acc = vector(0,0)

        self.centerx = 0
        

        self.pos = vector(mystery.rect.x + 16,mystery.rect.y - 32)
            
    def update(self):
        # set initial acceleration to 0 on x direction and gravity on the downward direction
        if self.start:
            self.acc = vector(0,GRAVITY)
            self.acc.y += 0.06
            self.vel.y = -1
            self.start = False

        if self.pos.y >= self.origin_y:
            self.kill()      
        
        # friction only applies in the x direction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)

        
    def blitme(self):
        # print self.rect.centerx
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)