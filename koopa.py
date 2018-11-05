import pygame
from pygame.sprite import Sprite


class Koopa(Sprite):

    def __init__(self, screen, mario, platform_tops, left_walls, right_walls):
        super(Koopa, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.mario = mario
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        self.image = pygame.image.load('resources/Images/koopa2left.gif')
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width/2
        self.mask = pygame.mask.from_surface(self.image)

        self.mask = pygame.mask.from_surface(self.image)
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.previous_centery = self.centery

        self.velocity_x = 0.25
        self.velocity_y = 0.1
        self.gravity = 0.004
        self.horizontal_speed = 0.25

    def update(self):
        self.previous_centery = self.centery

        self.centerx += self.velocity_x

        self.centery += self.velocity_y
        self.velocity_y += self.gravity

        colliding_with_floor = pygame.sprite.spritecollideany(self, self.platform_tops)
        if colliding_with_floor:
            self.velocity_y = 0
            self.centery = self.previous_centery

        colliding_with_right_wall = pygame.sprite.spritecollideany(self, self.right_walls)
        if colliding_with_right_wall:
            self.velocity_x = self.horizontal_speed

        colliding_with_left_wall = pygame.sprite.spritecollideany(self, self.left_walls)
        if colliding_with_left_wall:
            self.velocity_x = -self.horizontal_speed

        self.check_mario_collision()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (self.centerx, self.centery)

        self.mask = pygame.mask.from_surface(self.image)

        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)

    def check_mario_collision(self):
        collisions = pygame.sprite.collide_rect(self, self.mario)
        if collisions:
            print("Koopa got me")

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

    def get_mask(self):
        return self.mask
