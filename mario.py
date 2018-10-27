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
        
        #helper info for which side a collision has occured
        self.collisionSide = 'top'
        
        #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        #load image of mario
        self.image = pygame.image.load('resources/smallMario.gif')
        self.rect = self.image.get_rect()

        #viewport left and right boundaries
        self.viewLeft = 0
        

        #control vertical and horizontal velocity
        self.pos = vector(self.screenRect.width / 2, self.screenRect.height)
        self.vel = vector(0,0)
        self.acc = vector(0,0)
        
        #initially start mario here
        #self.rect.centerx = self.screenRect.left + 100
        #self.rect.centery = self.screenRect.bottom - 50
    
    def jump(self,platformsTop):
        #slightly move mario down to see if there is a collision below him
        #if true, he is on the floor platform and allow him to jump
        self.rect.y += 1.1
        hits = pygame.sprite.spritecollide(self,platformsTop,False)
        self.rect.y -= 1.1
        if hits:
            self.vel.y = -1.7
            
            #play jump sound effect
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sounds/jump.wav'))
            
    
    def jumpHeightAdjust(self):
        
        #adjust the jump height to how long the jump key is pressed
        #if the key is released, mario will begin moving down
        if self.vel.y < 0:
            self.vel.y = 0
    
    def viewport(self,viewport):

        changed = False

        # Scroll right
        rightBndry = self.viewLeft + self.screenRect.width - VIEWPORT_MARGIN
        if self.rect.right > rightBndry:
            self.viewLeft += self.rect.right - rightBndry
            changed = True
            
        keys = pygame.key.get_pressed()

        if changed:
            self.pos.x -= abs(self.vel.x + 0.4)
            for groups in viewport:
                groups.rect.x -= abs(self.vel.x)
                if groups.rect.x == 0:
                    groups.kill()
            
            self.viewLeft = 0
        
        #prevent mario from falling if less than screen left
        if self.rect.left < 16:
            self.vel.x = 0
            self.pos.x += 1.2



    def update(self,viewport):
        #set initial accelation to 0 on x direction and gravity on the downward direction
        self.acc = vector(0,GRAVITY)
    
        keys = pygame.key.get_pressed()


        #update accelaration depending on when mario is running on walking
        if keys[pygame.K_RIGHT] and keys[pygame.K_s]:
            #running right
            self.acc.x = PLAYER_RUN_ACCELERATION

        elif keys[pygame.K_RIGHT]:
            #walking right
            self.acc.x = PLAYER_WALK_ACCELERATION
            
        if keys[pygame.K_LEFT] and keys[pygame.K_s]:
            #running left
            self.acc.x = -PLAYER_RUN_ACCELERATION
        elif keys[pygame.K_LEFT]:
            #walking left
            self.acc.x = -PLAYER_WALK_ACCELERATION
    
        #friction only applies in the x direction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.viewport(viewport)
                   
        
        self.blitme()

        
        
    def blitme(self):
        #print self.rect.centerx
        self.screen.blit(self.image,self.rect)