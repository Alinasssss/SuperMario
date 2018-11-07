import pygame
from pygame.sprite import Sprite


class Starman(Sprite):

    def __init__(self, screen, platform_tops, left_walls, right_walls,x,y):
        super(Starman, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        self.start_movement = False

        self.image = pygame.image.load('resources/Images/star1_resized.gif')
        self.rect = self.image.get_rect()

        #self.rect.center = (400, 400)
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.previous_centery = self.centery

        self.rect.centerx = x
        self.rect.bottom = y


        self.velocity_x = 0
        self.velocity_y = 0.1
        self.gravity = 0.002
        self.horizontal_speed = 0.2

    def update(self):
        # when brick is hit, spawn starman
        if self.start_movement:
            self.centerx += self.velocity_x

            self.centery += self.velocity_y
            self.velocity_y += self.gravity

            colliding_with_floor = pygame.sprite.spritecollideany(self, self.platform_tops)
            if colliding_with_floor:
                self.velocity_x = self.horizontal_speed
                self.velocity_y = -0.6

            colliding_with_right_wall = pygame.sprite.spritecollideany(self, self.right_walls)
            if colliding_with_right_wall:
                self.velocity_x = self.horizontal_speed

            colliding_with_left_wall = pygame.sprite.spritecollideany(self, self.left_walls)
            if colliding_with_left_wall:
                self.velocity_x = -self.horizontal_speed

        #self.rect.center = (self.centerx, self.centery)
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
