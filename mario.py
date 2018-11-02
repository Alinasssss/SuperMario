import pygame
from pygame.sprite import Sprite
import pygame.font
from physics import *
vector = pygame.math.Vector2


class Mario(Sprite):
    def __init__(self, screen, entity_gamemaster):
        super(Mario, self).__init__()

        self.entity_gamemaster = entity_gamemaster

        # get the screen dims
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #load all mario images
        self.frames = 0
        self.small_mario = []
        self.big_mario = []
        self.fire_mario = []

        self.status = 'small'
        self.direction = 'right'


        #load all small mario sprites
        self.small_mario.append('resources/Images/smallMarioStandRight.gif')
        self.small_mario.append('resources/Images/smallMarioWalkRight1.gif')
        self.small_mario.append('resources/Images/smallMarioWalkRight2.gif')
        self.small_mario.append('resources/Images/smallMarioWalkRight3.gif')
        self.small_mario.append('resources/Images/smallMarioRightReverse.gif')
        self.small_mario.append('resources/Images/smallMarioJumpRight.gif')
        self.small_mario.append('resources/Images/smallMarioStandLeft.gif')
        self.small_mario.append('resources/Images/smallMarioWalkLeft1.gif')
        self.small_mario.append('resources/Images/smallMarioWalkLeft2.gif')
        self.small_mario.append('resources/Images/smallMarioWalkLeft3.gif')
        self.small_mario.append('resources/Images/smallMarioJumpLeft.gif')
        self.small_mario.append('resources/Images/smallMarioLeftReverse.gif')
        self.small_mario.append('resources/Images/deadMario.gif')

        #load all big mario sprites
        self.big_mario.append('resources/Images/bigMarioStandRight.gif')
        self.big_mario.append('resources/Images/bigMarioWalkRight1.gif')
        self.big_mario.append('resources/Images/bigMarioWalkRight2.gif')
        self.big_mario.append('resources/Images/bigMarioWalkRight3.gif')
        self.big_mario.append('resources/Images/bigMarioRightReverse.gif')
        self.big_mario.append('resources/Images/bigMarioJumpRight.gif')
        self.big_mario.append('resources/Images/bigMarioStandLeft.gif')
        self.big_mario.append('resources/Images/bigMarioWalkLeft1.gif')
        self.big_mario.append('resources/Images/bigMarioWalkLeft2.gif')
        self.big_mario.append('resources/Images/bigMarioWalkLeft3.gif')
        self.big_mario.append('resources/Images/bigMarioJumpLeft.gif')
        self.big_mario.append('resources/Images/bigMarioLeftReverse.gif')
        self.big_mario.append('resources/Images/bigMarioSquadRight.gif')
        self.big_mario.append('resources/Images/bigMarioSquadLeft.gif')
        
        
        #load all fire mario sprites
        self.fire_mario.append('resources/Images/fireMarioStandRight.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkRight1.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkRight2.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkRight3.gif')
        self.fire_mario.append('resources/Images/fireMarioRightReverse.gif')
        self.fire_mario.append('resources/Images/fireMarioJumpRight.gif')
        self.fire_mario.append('resources/Images/fireMarioStandLeft.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkLeft1.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkLeft2.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkLeft3.gif')
        self.fire_mario.append('resources/Images/fireMarioJumpLeft.gif')
        self.fire_mario.append('resources/Images/fireMarioLeftReverse.gif')
        self.fire_mario.append('resources/Images/fireMarioSquadRight.gif')
        self.fire_mario.append('resources/Images/fireMarioSquadLeft.gif')



        # load image of mario
        self.image = pygame.image.load(self.small_mario[0]).convert_alpha()
        self.change_image(0)
        self.rect = self.image.get_rect()

        #collision mask
        self.mask = pygame.mask.from_surface(self.image)
        
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
            self.vel.y = -1.98
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
                #print groups
                groups.rect.x -= abs(self.vel.x)
                if groups.rect.x == 0:                    
                    groups.kill()
            
            self.view_left = 0
        
        # prevent mario from falling if less than screen left
        if self.rect.left < 16:
            self.vel.x = 0
            self.pos.x += 1.2

    def check_mushroom_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.mushrooms, True,pygame.sprite.collide_mask)
        if collisions:
            print("I-ya got eet-uh")
            if self.status == 'small':
                self.status = 'big'
                if self.vel > 0:
                    self.change_image(0)
                elif self.vel < 0:
                    self.change_image(6)

    def check_fireflower_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.fireflowers, True,pygame.sprite.collide_mask)
        if collisions:
            if self.status == 'small':
                self.status = 'big'
                if self.vel > 0:
                    self.change_image(0)
                elif self.vel < 0:
                    self.change_image(6)
            elif self.status == 'big':
                self.status = 'fire'
                if self.vel > 0:
                    self.change_image(0)
                elif self.vel < 0:
                    self.change_image(6)
            
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
            self.direction = 'right'
            if not self.airborne:
                self.frames += 1
                if self.status == 'small':
                    if self.frames == 9:
                        self.change_image(1)
                    elif self.frames == 18:
                        self.change_image(2)
                    elif self.frames == 27:
                        self.change_image(3)
                    elif self.frames >= 34:
                        self.frames = 0
                elif not self.status == 'small':
                    if self.frames == 12:
                        self.change_image(1)
                    elif self.frames == 24:
                        self.change_image(2)
                    elif self.frames == 36:
                        self.change_image(3)
                    elif self.frames >= 48:
                        self.frames = 0

            elif self.airborne:
                self.change_image(5)
            if self.vel.x < 0 and not self.airborne:
                self.change_image(11)


        elif keys[pygame.K_RIGHT]:
            # walking right
            self.acc.x = PLAYER_WALK_ACCELERATION
            self.direction = 'right'
            if not self.airborne:
                self.frames += 1
                if self.status == 'small':
                    if self.frames == 13:
                        self.change_image(1)
                    elif self.frames == 26:
                        self.change_image(2)
                    elif self.frames == 39:
                        self.change_image(3)
                    elif self.frames >= 51:
                        self.frames = 0
                elif not self.status == 'small':
                    if self.frames == 17:
                        self.change_image(1)
                    elif self.frames == 34:
                        self.change_image(2)
                    elif self.frames == 61:
                        self.change_image(3)
                    elif self.frames >= 78:
                        self.frames = 0

            elif self.airborne:
                self.change_image(5)
            if self.vel.x < 0 and not self.airborne:
                self.change_image(11)

        if keys[pygame.K_LEFT] and keys[pygame.K_s]:
            # running left
            #running left
            self.acc.x = -PLAYER_RUN_ACCELERATION
            self.direction = 'left'
            if not self.airborne:
                self.frames += 1
                if self.status == 'small':
                    if self.frames == 9:
                        self.change_image(7)
                    elif self.frames == 18:
                        self.change_image(8)
                    elif self.frames == 27:
                        self.change_image(9)
                    elif self.frames >= 34:
                        self.frames = 0
                elif not self.status == 'small':
                    if self.frames == 12:
                        self.change_image(7)
                    elif self.frames == 24:
                        self.change_image(8)
                    elif self.frames == 36:
                        self.change_image(9)
                    elif self.frames >= 48:
                        self.frames = 0
            elif self.airborne:
                self.change_image(10)
            if self.vel.x > 0 and not self.airborne:
                self.change_image(4)
           
        elif keys[pygame.K_LEFT]:
            # walking left
            self.acc.x = -PLAYER_WALK_ACCELERATION
            self.direction = 'left'
            if not self.airborne:
                self.frames += 1
                if self.status == 'small':
                    if self.frames == 13:
                        self.change_image(7)
                    elif self.frames == 26:
                        self.change_image(8)
                    elif self.frames == 39:
                        self.change_image(9)
                    elif self.frames >= 51:
                        self.frames = 0
                    elif self.airborne:
                        self.change_image(10)
                elif not self.status == 'small':
                    if self.frames == 17:
                        self.change_image(7)
                    elif self.frames == 34:
                        self.change_image(8)
                    elif self.frames == 61:
                        self.change_image(9)
                    elif self.frames >= 78:
                        self.frames = 0
            elif self.airborne:
                self.change_image(10)
            if self.vel.x > 0 and not self.airborne:
                self.change_image(4)
            
        if not self.airborne and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_s]:
            self.frames = 0
            if self.vel.x > 0:
                self.change_image(0)
            elif self.vel.x < 0:
                self.change_image(6)

        
                #make mario lose momentum if he is already in the air
        #and trying to move in the opposite direciton
        if keys[pygame.K_LEFT] and self.airborne and self.vel.x > 0:
            self.acc.x = DECELLERATION_ON_AIR

        if keys[pygame.K_RIGHT] and self.airborne and self.vel.x < 0:
            self.acc.x = -DECELLERATION_ON_AIR
        

        #mario falls off pit, change to dead mario animation
        if self.pos.y >= self.screen_rect.height + 10:
            self.status = 'dead'
            print self.screen_rect.height
            print self.pos.y
            self.vel.x = 0
            self.vel.y = -2
            self.pos.y = self.screen_rect.height - 100
            #self.change_image(12)
            
        # friction only applies in the x direction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.check_mushroom_collisions()
        self.check_fireflower_collisions()
        self.check_one_up_mushroom_collisions()
        self.check_starman_collisions()

        self.viewport(viewport)
        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)
        

    def change_image(self,index):
        if self.status == 'small':
            self.image = pygame.image.load(self.small_mario[index]).convert_alpha()
        elif self.status == 'big':
            self.image = pygame.image.load(self.big_mario[index]).convert_alpha()
        elif self.status == 'fire':
            self.image = pygame.image.load(self.fire_mario[index]).convert_alpha()
        elif self.status == 'dead':
            print self.status
            self.image = pygame.image.load(self.small_mario[index]).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        
    def blitme(self):
        # print self.rect.centerx
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen,(255,0,0),self.rect,1)
        