import pygame
from pygame.sprite import Sprite


class OneUpMushroom(Sprite):

    def __init__(self, screen, platform_tops, left_walls, right_walls):
        super(OneUpMushroom, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        self.image = pygame.image.load('resources/Images/1UpMushroom.gif')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.center = (400, 0)
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        self.velocity_x = 1
        self.velocity_y = 0.1
        self.gravity = 0.15
        self.horizontal_speed = 2

    def update(self):
        self.centerx += self.velocity_x
        self.centery += self.velocity_y
        self.velocity_y += self.gravity

        colliding_with_floor = pygame.sprite.spritecollideany(self, self.platform_tops)
        if colliding_with_floor:
            self.velocity_y = 0

        colliding_with_right_wall = pygame.sprite.spritecollideany(self, self.right_walls)
        if colliding_with_right_wall:
            self.velocity_x = self.horizontal_speed

        colliding_with_left_wall = pygame.sprite.spritecollideany(self, self.left_walls)
        if colliding_with_left_wall:
            self.velocity_x = -self.horizontal_speed

        self.rect.center = (self.centerx, self.centery)
        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen,(255,0,0),self.rect,1)
