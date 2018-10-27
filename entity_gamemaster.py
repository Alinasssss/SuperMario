import pygame
from pygame.sprite import Group


class EntityGameMaster:
    def __init__(self):
        self.mushrooms = Group()

    def update(self):
        self.mushrooms.update()
