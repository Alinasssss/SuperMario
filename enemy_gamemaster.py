from pygame.sprite import Group


class EnemyGameMaster:
    def __init__(self):
        self.goombas = Group()
        self.koopas = Group()

    def update(self):
        self.goombas.update()
        self.koopas.update()
