import pygame.font
from settings import *


class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = WHITE
        self.text_background_color = LIGHTBLUE
        self.font = pygame.font.Font("resources/fonts/emulogic.ttf", 20)

        self.name = "MARIO"
        self.name_image = None
        self.name_rect = None

        self.score = 0
        self.score_image = None
        self.score_rect = None

        self.coin_counter = 0
        self.coin_counter_image = None
        self.coin_counter_rect = None

        self.world_text = "WORLD"
        self.world_text_image = None
        self.world_text_rect = None

        self.world_number = 1
        self.level_number = 1
        self.level_name_image = None
        self.level_name_rect = None

        self.timer_name = "TIMER"
        self.timer_name_image = None
        self.timer_name_rect = None

        self.timer = 400
        self.timer_image = None
        self.timer_rect = None

        self.update_name_text()
        self.update_score_text()
        self.update_coin_counter_text()
        self.update_world_text()
        self.update_level_name_text()
        self.update_timer_name_text()
        self.update_timer_text()

    def update_name_text(self):
        self.name_image = self.font.render(self.name, True, self.text_color, self.text_background_color)
        self.name_rect = self.name_image.get_rect()
        self.name_rect.left = self.name_rect.left + 35
        self.name_rect.top = 20

    def update_score_text(self):
        score_str = "{:,}".format(self.score).zfill(6)
        self.score_image = self.font.render(score_str, True, self.text_color, self.text_background_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.name_rect.left
        self.score_rect.top = 50

    def update_coin_counter_text(self):
        coin_counter_str = "{:,}".format(self.coin_counter).zfill(2)
        self.coin_counter_image = self.font.render(coin_counter_str, True, self.text_color, self.text_background_color)
        self.coin_counter_rect = self.coin_counter_image.get_rect()
        self.coin_counter_rect.left = self.screen_rect.right * 0.36
        self.coin_counter_rect.top = 50

    def update_world_text(self):
        self.world_text_image = self.font.render(self.world_text, True, self.text_color, self.text_background_color)
        self.world_text_rect = self.world_text_image.get_rect()
        self.world_text_rect.left = self.screen_rect.right * 0.58
        self.world_text_rect.top = 20

    def update_level_name_text(self):
        level_name_str = str(self.world_number) + "-" + str(self.level_number)
        self.level_name_image = self.font.render(level_name_str, True, self.text_color, self.text_background_color)
        self.level_name_rect = self.level_name_image.get_rect()
        self.level_name_rect.centerx = self.world_text_rect.centerx
        self.level_name_rect.top = 50

    def update_timer_name_text(self):
        self.timer_name_image = self.font.render(self.timer_name, True, self.text_color, self.text_background_color)
        self.timer_name_rect = self.timer_name_image.get_rect()
        self.timer_name_rect.right = self.screen_rect.right - 35
        self.timer_name_rect.top = 20

    def update_timer_text(self):
        timer_str = "{:,}".format(self.timer).zfill(3)
        self.timer_image = self.font.render(timer_str, True, self.text_color, self.text_background_color)
        self.timer_rect = self.timer_image.get_rect()
        self.timer_rect.right = self.timer_name_rect.right
        self.timer_rect.top = 50

    def show_score(self):
        self.screen.blit(self.name_image, self.name_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.coin_counter_image, self.coin_counter_rect)
        self.screen.blit(self.world_text_image, self.world_text_rect)
        self.screen.blit(self.level_name_image, self.level_name_rect)
        self.screen.blit(self.timer_name_image, self.timer_name_rect)
        self.screen.blit(self.timer_image, self.timer_rect)
