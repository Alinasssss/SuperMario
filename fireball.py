import pygame
from pygame.sprite import Sprite
from physics import *
vector = pygame.math.Vector2


class Fireball(Sprite):

    def __init__(self,screen,mario):
        super(Fireball,self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.frames = 0
        self.fire_animation = []
        self.direction = 'right'

        self.shots = 2
        
        self.fire_animation.append('resources/Images/fireball1.gif')
        self.fire_animation.append('resources/Images/fireball2.gif')
        self.fire_animation.append('resources/Images/fireball3.gif')
        self.fire_animation.append('resources/Images/fireball4.gif')
        
        # load image of mario
        self.image = pygame.image.load(self.fire_animation[0]).convert_alpha()
        self.rect = self.image.get_rect()

        self.mario = mario

        #collision mask
        self.mask = pygame.mask.from_surface(self.image)
        
        self.vel = vector(0,0)
        self.acc = vector(0,0)
        
        # control vertical and horizontal velocity
        if self.mario.direction == 'right':
            self.pos = vector(mario.pos.x + 20,mario.pos.y - 32)
            self.direction = 'right'
        elif self.mario.direction == 'left':
            self.pos = vector(mario.pos.x - 20,mario.pos.y - 32)
            self.direction = 'left'

        
    def update(self,platforms_top):
        # set initial acceleration to 0 on x direction and gravity on the downward direction
        if self.direction == 'right':
            self.acc = vector(0,GRAVITY)
            self.acc.x += 0.01
            self.vel.x = 1
        elif self.direction == 'left':
            self.acc = vector(0, GRAVITY)
            self.acc.x -= 0.01
            self.vel.x = -1
        
        #check ground collisions for fireballs
        fireball_collision = pygame.sprite.spritecollide(self,platforms_top,False,pygame.sprite.collide_mask)
        if fireball_collision:
            self.vel.y = -1
        
        # friction only applies in the x direction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)

        if self.pos.y > self.screen_rect.height or self.pos.x > self.screen_rect.width:
            self.kill()
        
    
    def blitme(self):
        # print self.rect.centerx
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen,(255,0,0),self.rect,1)
    
    