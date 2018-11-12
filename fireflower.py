import pygame
from pygame.sprite import Sprite
vector = pygame.math.Vector2


class Fireflower(Sprite):

    def __init__(self, screen,mystery):
        super(Fireflower, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('resources/Images/flower1.gif')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.centerx = 0

        # dummy code testing
        self.pos = vector(20,32)
        self.pos.x = 0

        self.rect.centerx = mystery.rect.x + 15
        self.rect.bottom = mystery.rect.y + 25

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen,(255,0,0),self.rect,1)
