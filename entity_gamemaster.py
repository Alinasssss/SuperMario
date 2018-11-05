from pygame.sprite import Group


class EntityGameMaster:
    def __init__(self):
        self.mushrooms = Group()
        self.fireflowers = Group()
        self.one_up_mushrooms = Group()
        self.starmen = Group()

    def update(self):
        self.mushrooms.update()
        self.fireflowers.update()
        self.one_up_mushrooms.update()
        self.starmen.update()
