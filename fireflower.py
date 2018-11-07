import pygame
from pygame.sprite import Sprite


class Fireflower(Sprite):

    def __init__(self, screen,x,y):
        super(Fireflower, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('resources/Images/flower_resized.gif')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        #self.rect.center = (500, 550)

        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen,(255,0,0),self.rect,1)
