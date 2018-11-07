import pygame
from pygame.sprite import Sprite


class Goomba(Sprite):

    def __init__(self, screen, mario, platform_tops, left_walls, right_walls):
        super(Goomba, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.mario = mario
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        # Animation timer stuff
        self.animation_timer_length = 250
        self.animation_timer = self.animation_timer_length
        self.current_animation_frame = 0

        self.death_animation_timer_length = 1000
        self.dying = False

        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_time = 0

        self.image_frames = [
            pygame.image.load('resources/Images/goomba1.gif'),
            pygame.image.load('resources/Images/goomba2.gif')
        ]
        self.death_image = pygame.image.load('resources/Images/goombaDead.gif')
        self.current_image = self.image_frames[self.current_animation_frame]
        self.rect = self.current_image.get_rect()   # Used for drawing the sprite in the correct location

        self.environment_rect = self.current_image.get_rect()   # Used for detecting floor and wall collisions
        self.environment_rect.width = self.environment_rect.width * 0.5

        self.top_rect = self.current_image.get_rect()   # Used for mario collisions
        self.top_rect.height = self.top_rect.height/4

        self.left_rect = self.current_image.get_rect()  # Used for mario collisions
        self.left_rect.width = self.left_rect.width/4
        self.left_rect.height = self.left_rect.height/2

        self.right_rect = self.current_image.get_rect() # Used for mario collisions
        self.right_rect.width = self.right_rect.width/4
        self.right_rect.height = self.right_rect.height/2

        self.centerx = self.current_image.get_rect().centerx
        self.centery = self.current_image.get_rect().centery

        self.velocity_x = 0.25
        self.velocity_y = 0.1
        self.gravity = 0.01
        self.horizontal_speed = 0.25

    def update(self):
        if self.dying:
            self.delta_time = pygame.time.get_ticks() - self.last_frame_ticks
            self.last_frame_ticks = pygame.time.get_ticks()

            self.animation_timer -= self.delta_time
            if self.animation_timer <= 0:
                self.kill()
        else:
            self.update_animation()

            self.centerx += self.velocity_x
            self.centery += self.velocity_y
            self.velocity_y += self.gravity

            self.rect.center = (self.centerx, self.centery)
            self.environment_rect.center = (self.centerx, self.centery)
            self.top_rect.center = (self.centerx, self.centery - 18)
            self.left_rect.center = (self.centerx - 12, self.centery + 6)
            self.right_rect.center = (self.centerx + 12, self.centery + 6)

            for platform_top in self.platform_tops:
                if self.environment_rect.colliderect(platform_top):
                    self.velocity_y = 0

            for left_wall in self.left_walls:
                if self.environment_rect.colliderect(left_wall):
                    self.velocity_x = -self.horizontal_speed

            for right_wall in self.right_walls:
                if self.environment_rect.colliderect(right_wall):
                    self.velocity_x = self.horizontal_speed

            self.check_mario_collision()

        self.blitme()

    def update_animation(self):
        self.delta_time = pygame.time.get_ticks() - self.last_frame_ticks
        self.last_frame_ticks = pygame.time.get_ticks()

        self.animation_timer -= self.delta_time
        if self.animation_timer <= 0:
            self.animation_timer += self.animation_timer_length

            self.current_animation_frame += 1
            if self.current_animation_frame > len(self.image_frames) - 1:
                self.current_animation_frame = 0

            self.current_image = self.image_frames[self.current_animation_frame]

    def check_mario_collision(self):
        if self.mario.rect.colliderect(self.top_rect):
            self.mario.gui.score += 100
            self.mario.gui.update_score_text()
            self.mario.vel.y = -1
            self.perform_death()
        if self.mario.rect.colliderect(self.left_rect) or self.mario.rect.colliderect(self.right_rect):
            print("haha")

    def perform_death(self):
        self.dying = True
        self.velocity_x = 0
        self.velocity_y = 0
        self.horizontal_speed = 0

        self.centery += 15                  # It's easier to just offset the death image for the old rect rather than
        self.rect.centery = self.centery    # create a new rect solely for the death image

        self.current_image = self.death_image
        self.animation_timer = self.death_animation_timer_length

    def blitme(self):
        self.screen.blit(self.current_image, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 255), self.rect, 1)
        pygame.draw.rect(self.screen, (0, 255, 255), self.environment_rect, 1)
        pygame.draw.rect(self.screen, (0, 255, 0), self.top_rect, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.left_rect, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.right_rect, 1)
