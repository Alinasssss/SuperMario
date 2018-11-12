import pygame
from pygame.sprite import Sprite
vector = pygame.math.Vector2


class Starman(Sprite):
    def __init__(self, screen, platform_tops, left_walls, right_walls, mystery):
        super(Starman, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        self.start_movement = False

        # dummy code testing
        self.pos = vector(20, 32)
        self.pos.x = 0

        self.image = pygame.image.load('resources/Images/star1.gif')
        self.rect = self.image.get_rect()

        # self.rect.center = (400, 400)
        # self.centerx = self.rect.centerx
        self.centerx = mystery.rect.x + 10

        # self.centery = self.rect.centery
        self.centery = mystery.rect.y

        self.velocity_x = 1
        self.velocity_y = 0.1
        self.gravity = 0.15
        self.horizontal_speed = 1

    def update(self):
        # when brick is hit, spawn starman
        self.centerx += self.velocity_x
        self.centery += self.velocity_y
        self.velocity_y += self.gravity

        colliding_with_floor = pygame.sprite.spritecollideany(self, self.platform_tops)
        if colliding_with_floor:
            self.velocity_y = -4

        colliding_with_right_wall = pygame.sprite.spritecollideany(self, self.right_walls)
        if colliding_with_right_wall:
            self.velocity_x = self.horizontal_speed

        colliding_with_left_wall = pygame.sprite.spritecollideany(self, self.left_walls)
        if colliding_with_left_wall:
            self.velocity_x = -self.horizontal_speed

        self.rect.center = (self.centerx, self.centery)
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
