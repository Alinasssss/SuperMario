import pygame
from pygame.sprite import Sprite
import pygame.font
from physics import *
vector = pygame.math.Vector2


class Mario(Sprite):
    def __init__(self, screen, entity_gamemaster):
        super(Mario, self).__init__()

        self.entity_gamemaster = entity_gamemaster

        # helper info for which side a collision has occured
        self.collision_side = 'top'
        
        # get the screen dims
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # load image of mario
        self.image = pygame.image.load('resources/Images/smallMarioStandRight.gif')
        self.rect = self.image.get_rect()

        # viewport left and right boundaries
        self.view_left = 0

        # control vertical and horizontal velocity
        self.pos = vector(self.screen_rect.width / 2, self.screen_rect.height)

        self.vel = vector(0,0)
        self.acc = vector(0,0)
        self.airborne = False

    def jump(self, platforms_top):
        # slightly move mario down to see if there is a collision below him
        # if true, he is on the floor platform and allow him to jump
        self.rect.y += 1.1
        hits = pygame.sprite.spritecollide(self, platforms_top, False)
        self.rect.y -= 1.1
        if hits:
            self.vel.y = -1.7
            self.airborne = True
            
            # play jump sound effect
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sounds/jump.wav'))

    def jump_height_adjust(self):
        # adjust the jump height to how long the jump key is pressed
        # if the key is released, mario will begin moving down
        if self.vel.y < 0:
            self.vel.y = 0
    
    def viewport(self, viewport):
        changed = False

        # Scroll right
        right_boundary = self.view_left + self.screen_rect.width - VIEWPORT_MARGIN
        if self.rect.right > right_boundary:
            self.view_left += self.rect.right - right_boundary
            changed = True

        if changed:
            self.pos.x -= abs(self.vel.x + 0.8)
            for groups in viewport:
                groups.rect.x -= abs(self.vel.x)
                if groups.rect.x == 0:                    
                    groups.kill()
            
            self.view_left = 0
        
        # prevent mario from falling if less than screen left
        if self.rect.left < 16:
            self.vel.x = 0
            self.pos.x += 1.2

    def check_mushroom_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.mushrooms, True)
        if collisions:
            print("I-ya got eet-uh")

    def check_fireflower_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.fireflowers, True)
        if collisions:
            print("Atsa spicy")

    def check_one_up_mushroom_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.one_up_mushrooms, True)
        if collisions:
            print("One man")

    def check_starman_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.starmen, True)
        if collisions:
            print("Du du du dudu du dudududu")

    def update(self, viewport):
        # set initial acceleration to 0 on x direction and gravity on the downward direction
        self.acc = vector(0, GRAVITY)
    
        keys = pygame.key.get_pressed()

        # update acceleration depending on when mario is running on walking
        if keys[pygame.K_RIGHT] and keys[pygame.K_s]:
            # running right
            self.acc.x = PLAYER_RUN_ACCELERATION

        elif keys[pygame.K_RIGHT]:
            # walking right
            self.acc.x = PLAYER_WALK_ACCELERATION
            
        if keys[pygame.K_LEFT] and keys[pygame.K_s]:
            # running left
            self.acc.x = -PLAYER_RUN_ACCELERATION
           
        elif keys[pygame.K_LEFT]:
            # walking left
            self.acc.x = -PLAYER_WALK_ACCELERATION
    
        # friction only applies in the x direction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.viewport(viewport)

        if self.pos.y > self.screen_rect.height:
            self.pos.y = self.screen_rect.height - 100
            self.pos.x = self.pos.x - 100
        
        self.blitme()

        self.check_mushroom_collisions()
        self.check_fireflower_collisions()
        self.check_one_up_mushroom_collisions()
        self.check_starman_collisions()

    def blitme(self):
        # print self.rect.centerx
        self.screen.blit(self.image, self.rect)
