import pygame
from pygame.sprite import Sprite


class Fireflower(Sprite):

    def __init__(self, screen):
        super(Fireflower, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('resources/Images/flower1.gif')
        self.rect = self.image.get_rect()

        self.rect.center = (400, 500)

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
