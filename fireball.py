import pygame
from pygame.sprite import Sprite
from physics import *
vector = pygame.math.Vector2


class Fireball(Sprite):

    def __init__(self, screen, mario):
        super(Fireball, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.frames = 0
        self.fire_animation = []
        self.direction = 'right'

        self.shots = 2
        
        self.fire_animation.append('resources/Images/fireball_right1.gif')
        self.fire_animation.append('resources/Images/fireball_right2.gif')
        self.fire_animation.append('resources/Images/fireball_right3.gif')
        self.fire_animation.append('resources/Images/fireball_right4.gif')
        self.fire_animation.append('resources/Images/fireball_left1.gif')
        self.fire_animation.append('resources/Images/fireball_left2.gif')
        self.fire_animation.append('resources/Images/fireball_left3.gif')
        self.fire_animation.append('resources/Images/fireball_left4.gif')
        
        # load image of mario
        self.image = pygame.image.load(self.fire_animation[0]).convert_alpha()
        self.rect = self.image.get_rect()

        self.mario = mario

        # collision mask
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

    def update(self, platforms_top, left_walls, right_walls, enemy_gamemaster):
        # set initial acceleration to 0 on x direction and gravity on the downward direction
        if self.direction == 'right':
            self.acc = vector(0,GRAVITY)
            self.acc.x += 0.06
            self.vel.x = 4
        elif self.direction == 'left':
            self.acc = vector(0, GRAVITY)
            self.acc.x -= 0.06
            self.vel.x = -4
        
        self.frames += 1

        if self.frames == 20:
            self.change_image(0)
        elif self.frames == 40:
            self.change_image(1)
        elif self.frames == 60:
            self.change_image(2)
        elif self.frames == 80:
            self.change_image(3)
        elif self.frames == 100:
            self.frames = 0

        if self.pos.y > self.screen_rect.bottom or self.pos.x > self.screen_rect.right or self.pos.x < self.screen_rect.left:
            self.kill()

        # check ground collisions for fireballs
        floor_collision = pygame.sprite.spritecollide(self, platforms_top, False, pygame.sprite.collide_mask)
        if floor_collision:
            self.vel.y = -4
        
        left_wall_collision = pygame.sprite.spritecollide(self, left_walls, False, pygame.sprite.collide_mask)
        if left_wall_collision:
            self.kill()

        right_wall_collision = pygame.sprite.spritecollide(self, left_walls, False, pygame.sprite.collide_mask)
        if right_wall_collision:
            self.kill()

        goomba_collision = pygame.sprite.spritecollide(self, enemy_gamemaster.goombas, True)
        if goomba_collision:
            self.kill()
            self.mario.gui.score += 100
            self.mario.gui.update_score_text()

        koopa_collision = pygame.sprite.spritecollide(self, enemy_gamemaster.koopas, True)
        if koopa_collision:
            self.kill()
            self.mario.gui.score += 250
            self.mario.gui.update_score_text()

        # friction only applies in the x direction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)

    def blitme(self):
        # print self.rect.centerx
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

    def change_image(self, index):
        if self.direction == 'right':
            self.image = pygame.image.load(self.fire_animation[index]).convert_alpha()
        elif self.direction == 'left':
            self.image = pygame.image.load(self.fire_animation[index+4]).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
