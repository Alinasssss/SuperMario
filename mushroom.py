import pygame
from pygame.sprite import Sprite
vector = pygame.math.Vector2


class Mushroom(Sprite):

    def __init__(self, screen, platform_tops, left_walls, right_walls, mystery):
        super(Mushroom, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        self.start_movement = False

        # dummy code testing
        self.pos = vector(20,32)
        self.pos.x = 0

        self.image = pygame.image.load('resources/Images/growMushroom.gif')
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.rect.center = (400, 400)
        self.mask = pygame.mask.from_surface(self.image)
        
        self.centerx = mystery.rect.centerx
        self.centery = mystery.rect.centery - 10

        self.center = float(self.rect.centerx)
        self.original_y = self.rect.bottom

        self.velocity_x = 1
        self.velocity_y = 0.1
        self.gravity = 0.15
        self.horizontal_speed = 1.6

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
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def get_mask(self):
        return self.mask
