import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite
import pygame.font
from physics import *
vector = pygame.math.Vector2

class Mario(Sprite):
    def __init__(self,screen):
        super(Mario,self).__init__()

        self.jumpLimit = 200
        self.slowDown = 100
        
        #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
        #load image of mario
        self.image = pygame.image.load('resources/player.gif')
        self.rect = self.image.get_rect()

        #control vertical and horizontal velocity
        self.pos = vector(screen.get_rect().width / 2, screen.get_rect().height / 2)
        self.vel = vector(0,0)
        self.acc = vector(0,0)
        
        #initially start mario here
        self.rect.centerx = self.screenRect.left + 100
        self.rect.centery = self.screenRect.bottom - 200
    
    def jump(self,platforms):
        #slightly move mario down to see if there is a collision below him
        #if true, he is on the floor platform and allow him to jump
        self.rect.y += 1.2
        hits = pygame.sprite.spritecollide(self,platforms,False)
        self.rect.y -= 1.2
        if hits:
            self.vel.y = -5


    def update(self,platforms,walls):
        #set initial accelation to 0, GRACITY SPEED DOWN
        self.acc = vector(0,GRAVITY)
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        
        #friction only applies in the x direction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.blitme()

    def blitme(self):
        #print self.rect.centerx
        self.screen.blit(self.image,self.rect)