import pygame
from pygame.sprite import Sprite
vector = pygame.math.Vector2


class Mushroom(Sprite):

    def __init__(self, screen, platform_tops, left_walls, right_walls,x,y):
        super(Mushroom, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.platform_tops = platform_tops
        self.left_walls = left_walls
        self.right_walls = right_walls

        self.start_movement= False

        #dummy code testing
        self.pos = vector(20,32)
        self.pos.x = 0


        self.image = pygame.image.load('resources/Images/growMushroom1.gif')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        #self.rect.center = (400, 400)
        self.mask = pygame.mask.from_surface(self.image)
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.previous_centery = self.centery

        self.rect.centerx = x
        self.rect.bottom = y

        self.center = float(self.rect.centerx)
        self.original_y = self.rect.bottom

        self.velocity_x = 0
        self.velocity_y = 0.1
        self.gravity = 0.001
        self.horizontal_speed = 0.2

    def update(self):
        #this will triger after mario hits mystery tile
        if self.start_movement:
            
            self.previous_centery = self.centery

            self.centerx += self.velocity_x

            self.centery += self.velocity_y
            self.velocity_y += self.gravity

            colliding_with_floor = pygame.sprite.spritecollideany(self, self.platform_tops)
            if colliding_with_floor:
                self.velocity_x = self.horizontal_speed
                self.velocity_y = 0
                self.centery = self.previous_centery

            colliding_with_right_wall = pygame.sprite.spritecollideany(self, self.right_walls)
            if colliding_with_right_wall:
                self.velocity_x = self.horizontal_speed

            colliding_with_left_wall = pygame.sprite.spritecollideany(self, self.left_walls)
            if colliding_with_left_wall:
                self.velocity_x = -self.horizontal_speed

        self.mask = pygame.mask.from_surface(self.image)
        #self.rect.center = (self.centerx, self.centery)
        
        
        self.blitme()
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen,(255,0,0),self.rect,1)


    def get_mask(self):
        return self.mask
