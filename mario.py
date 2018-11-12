import pygame
from pygame.sprite import Sprite
import pygame.font
from physics import *

vector = pygame.math.Vector2


class Mario(Sprite):
    def __init__(self, screen, entity_gamemaster, gui):
        super(Mario, self).__init__()

        # get the screen dims
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.entity_gamemaster = entity_gamemaster
        self.gui = gui

        # load all mario images
        self.frames = 0
        self.star_frames = 0
        self.small_mario = []
        self.big_mario = []
        self.fire_mario = []

        self.status = 'small'
        self.direction = 'right'
        self.starman = False
        self.starman_timer = 0
        self.speed = 'walking'
        self.finish = False

        # load all small mario sprites
        self.small_mario.append('resources/Images/smallMarioStandRight.gif')
        self.small_mario.append('resources/Images/smallMarioWalkRight1.gif')
        self.small_mario.append('resources/Images/smallMarioWalkRight2.gif')
        self.small_mario.append('resources/Images/smallMarioWalkRight3.gif')
        self.small_mario.append('resources/Images/smallMarioRightReverse.gif')
        self.small_mario.append('resources/Images/smallMarioJumpRight.gif')
        self.small_mario.append('resources/Images/smallMarioStandLeft.gif')
        self.small_mario.append('resources/Images/smallMarioWalkLeft1.gif')
        self.small_mario.append('resources/Images/smallMarioWalkLeft2.gif')
        self.small_mario.append('resources/Images/smallMarioWalkLeft3.gif')
        self.small_mario.append('resources/Images/smallMarioJumpLeft.gif')
        self.small_mario.append('resources/Images/smallMarioLeftReverse.gif')
        self.small_mario.append('resources/Images/deadMario.gif')
        self.small_mario.append('resources/Images/marioPole.gif')
        self.small_mario.append('resources/Images/marioPole.gif')

        # load all big mario sprites
        self.big_mario.append('resources/Images/bigMarioStandRight.gif')
        self.big_mario.append('resources/Images/bigMarioWalkRight1.gif')
        self.big_mario.append('resources/Images/bigMarioWalkRight2.gif')
        self.big_mario.append('resources/Images/bigMarioWalkRight3.gif')
        self.big_mario.append('resources/Images/bigMarioRightReverse.gif')
        self.big_mario.append('resources/Images/bigMarioJumpRight.gif')
        self.big_mario.append('resources/Images/bigMarioStandLeft.gif')
        self.big_mario.append('resources/Images/bigMarioWalkLeft1.gif')
        self.big_mario.append('resources/Images/bigMarioWalkLeft2.gif')
        self.big_mario.append('resources/Images/bigMarioWalkLeft3.gif')
        self.big_mario.append('resources/Images/bigMarioJumpLeft.gif')
        self.big_mario.append('resources/Images/bigMarioLeftReverse.gif')
        self.big_mario.append('resources/Images/bigMarioSquadRight.gif')
        self.big_mario.append('resources/Images/bigMarioSquadLeft.gif')
        self.big_mario.append('resources/Images/bigMarioPole.gif')

        # load all fire mario sprites
        self.fire_mario.append('resources/Images/fireMarioStandRight.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkRight1.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkRight2.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkRight3.gif')
        self.fire_mario.append('resources/Images/fireMarioRightReverse.gif')
        self.fire_mario.append('resources/Images/fireMarioJumpRight.gif')
        self.fire_mario.append('resources/Images/fireMarioStandLeft.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkLeft1.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkLeft2.gif')
        self.fire_mario.append('resources/Images/fireMarioWalkLeft3.gif')
        self.fire_mario.append('resources/Images/fireMarioJumpLeft.gif')
        self.fire_mario.append('resources/Images/fireMarioLeftReverse.gif')
        self.fire_mario.append('resources/Images/fireMarioSquadRight.gif')
        self.fire_mario.append('resources/Images/fireMarioSquadLeft.gif')
        self.fire_mario.append('resources/Images/fireMarioPole.gif')

        self.fire_mario.append('resources/Images/fireMarioShootRight.gif')
        self.fire_mario.append('resources/Images/fireMarioShootLeft.gif')

        # load image of mario
        self.image = pygame.image.load(self.small_mario[0]).convert_alpha()

        self.pix_map = pygame.PixelArray(self.image)

        self.image = self.pix_map.make_surface()

        # self.change_image(0)
        self.rect = self.image.get_rect()

        # collision mask
        self.mask = pygame.mask.from_surface(self.image)

        # viewport left and right boundaries
        self.view_left = 0

        # control vertical and horizontal velocity
        self.pos = vector(self.screen_rect.width / 2, self.screen_rect.height - 50)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.airborne = False

        # timer variables
        self.previous_game_ticks = pygame.time.get_ticks()
        self.delta_time = 0
        self.one_second_timer = 1000

    def jump(self, platforms_top):
        # slightly move mario down to see if there is a collision below him
        # if true, he is on the floor platform and allow him to jump
        self.rect.y += 1.1
        hits = pygame.sprite.spritecollide(self, platforms_top, False)
        self.rect.y -= 1.1
        if hits:
            self.vel.y = -13
            self.airborne = True

            # play jump sound effect
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sounds/jump.wav'))
            if self.direction == 'right':
                self.change_image(5)
            elif self.direction == 'left':
                self.change_image(10)

    def jump_height_adjust(self):
        # adjust the jump height to how long the jump key is pressed
        # if the key is released, mario will begin moving down
        if self.vel.y < 0:
            self.vel.y = 0

    def viewport(self, viewport):
        changed = False
        
        # Scroll right
        right_boundary = self.view_left + self.screen_rect.width - VIEWPORT_MARGIN
        if self.rect.right > right_boundary:
            self.view_left += self.rect.right - right_boundary
            changed = True

        if changed:
            if self.speed == 'walking':
                if not self.finish:
                    self.pos.x -= abs(self.vel.x + (PLAYER_WALK_ACCELERATION - FRICTION))
            elif self.speed == 'running':
                if not self.finish:
                    self.pos.x -= abs(self.vel.x + (PLAYER_RUN_ACCELERATION - FRICTION))
            for groups in viewport:
                groups.rect.x -= abs(self.vel.x)
                groups.pos.x -= abs(self.vel.x)
                groups.centerx -= abs(self.vel.x)
                
                if groups.rect.x <= 0:
                    groups.rect.x -= 1
                    groups.pos.x -= 1
                    groups.centerx -= 1
                    if groups.rect.x <= -150:
                        groups.kill()

            self.view_left = 0

        # prevent mario from falling if less than screen left
        if self.rect.left < 16:
            self.vel.x = 0
            self.pos.x += 1.2

    def check_mushroom_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.mushrooms, True)
        if collisions:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('resources/sounds/powerup.wav'))
            self.gui.score += 1000
            self.gui.update_score_text()

            if self.status == 'small':
                self.status = 'big'
                if self.vel.x > 0:
                    self.change_image(0)
                elif self.vel.x < 0:
                    self.change_image(6)

    def check_fireflower_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.fireflowers, True)
        if collisions:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('resources/sounds/powerup.wav'))
            self.gui.score += 1000
            self.gui.update_score_text()

            if self.status == 'small':
                self.status = 'big'
                if self.vel.x > 0:
                    self.change_image(0)
                elif self.vel.x < 0:
                    self.change_image(6)
            elif self.status == 'big':
                self.status = 'fire'
                if self.vel.x > 0:
                    self.change_image(0)
                elif self.vel.x < 0:
                    self.change_image(6)

    def check_one_up_mushroom_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.one_up_mushrooms, True)
        if collisions:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('resources/sounds/powerup.wav'))

    def check_starman_collisions(self):
        collisions = pygame.sprite.spritecollide(self, self.entity_gamemaster.starmen, True)
        if collisions:
            self.starman = True
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('resources/sounds/powerup.wav'))
            pygame.mixer.Channel(5).play(pygame.mixer.Sound('resources/sounds/starman.wav'))

    def check_pole_collisions(self, pole):
        if not self.finish:
            collision = pygame.sprite.spritecollide(self, pole, False, pygame.sprite.collide_mask)
            if collision:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('resources/sounds/flagpole.wav'))
                self.pos.x = collision[0].rect.left
                self.finish = True
                if self.status == 'small':
                    self.change_image(13)
                elif not self.status == 'small':
                    self.change_image(14)

                self.vel.x = 0
                self.vel.y = 0

    def update(self, viewport, pole):
        # set initial acceleration to 0 on x direction and gravity on the downward direction
        self.acc = vector(0, GRAVITY)

        if self.starman:
            self.starman_timer += 1
        
        if self.starman_timer == 800:
            self.starman = False
            self.starman_timer = 0
            pygame.mixer.Channel(5).play(pygame.mixer.Sound('resources/sounds/themesong.wav'))

        keys = pygame.key.get_pressed()

        if not self.finish:
            # update acceleration depending on when mario is running on walking
            if keys[pygame.K_RIGHT] and keys[pygame.K_s] and not keys[pygame.K_DOWN]:
                # running right
                self.speed = 'running'
                self.acc.x = PLAYER_RUN_ACCELERATION
                self.direction = 'right'
                if not self.airborne:
                    self.frames += 1
                    if self.status == 'small':
                        if self.frames == 3:
                            self.change_image(1)
                        elif self.frames == 6:
                            self.change_image(2)
                        elif self.frames == 9:
                            self.change_image(3)
                        elif self.frames >= 12:
                            self.frames = 0
                    elif not self.status == 'small':
                        if self.frames == 2:
                            self.change_image(1)
                        elif self.frames == 4:
                            self.change_image(2)
                        elif self.frames == 6:
                            self.change_image(3)
                        elif self.frames >= 8:
                            self.frames = 0

                elif self.airborne:
                    self.change_image(5)
                if self.vel.x < 0 and not self.airborne:
                    self.change_image(11)

            elif keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
                # walking right
                self.speed = 'walking'

                self.acc.x = PLAYER_WALK_ACCELERATION
                self.direction = 'right'
                if not self.airborne:
                    self.frames += 1
                    if self.status == 'small':
                        if self.frames == 4:
                            self.change_image(1)
                        elif self.frames == 8:
                            self.change_image(2)
                        elif self.frames == 12:
                            self.change_image(3)
                        elif self.frames >= 16:
                            self.frames = 0
                    elif not self.status == 'small':
                        if self.frames == 3:
                            self.change_image(1)
                        elif self.frames == 6:
                            self.change_image(2)
                        elif self.frames == 9:
                            self.change_image(3)
                        elif self.frames >= 12:
                            self.frames = 0

                elif self.airborne:
                    self.change_image(5)
                if self.vel.x < 0 and not self.airborne:
                    self.change_image(11)

            if keys[pygame.K_LEFT] and keys[pygame.K_s] and not keys[pygame.K_DOWN]:
                # running left
                # running left
                self.speed = 'running'

                self.acc.x = -PLAYER_RUN_ACCELERATION
                self.direction = 'left'
                if not self.airborne:
                    self.frames += 1
                    if self.status == 'small':
                        if self.frames == 3:
                            self.change_image(7)
                        elif self.frames == 6:
                            self.change_image(8)
                        elif self.frames == 9:
                            self.change_image(9)
                        elif self.frames >= 12:
                            self.frames = 0
                    elif not self.status == 'small':
                        if self.frames == 2:
                            self.change_image(7)
                        elif self.frames == 4:
                            self.change_image(8)
                        elif self.frames == 6:
                            self.change_image(9)
                        elif self.frames >= 8:
                            self.frames = 0
                elif self.airborne:
                    self.change_image(10)
                if self.vel.x > 0 and not self.airborne:
                    self.change_image(4)

            elif keys[pygame.K_LEFT] and not keys[pygame.K_DOWN]:
                # walking left
                self.speed = 'walking'

                self.acc.x = -PLAYER_WALK_ACCELERATION
                self.direction = 'left'
                if not self.airborne:
                    self.frames += 1
                    if self.status == 'small':
                        if self.frames == 4:
                            self.change_image(7)
                        elif self.frames == 8:
                            self.change_image(8)
                        elif self.frames == 12:
                            self.change_image(9)
                        elif self.frames >= 16:
                            self.frames = 0
                        elif self.airborne:
                            self.change_image(10)
                    elif not self.status == 'small':
                        if self.frames == 3:
                            self.change_image(7)
                        elif self.frames == 6:
                            self.change_image(8)
                        elif self.frames == 9:
                            self.change_image(9)
                        elif self.frames >= 12:
                            self.frames = 0
                elif self.airborne:
                    self.change_image(10)
                if self.vel.x > 0 and not self.airborne:
                    self.change_image(4)

            if not self.airborne and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
                self.frames = 0
                if self.vel.x > 0:
                    self.change_image(0)
                elif self.vel.x < 0:
                    self.change_image(6)
                if self.direction == 'right':
                    self.change_image(0)
                elif self.direction == 'left':
                    self.change_image(6)

            if keys[pygame.K_DOWN]:
                if not self.airborne:
                    if not self.status == 'small':
                        if self.direction == 'right':
                            self.change_image(12)
                        elif self.direction == 'left':
                            self.change_image(13)

            # make mario lose momentum if he is already in the air
            # and trying to move in the opposite direciton
            if keys[pygame.K_LEFT] and self.airborne and self.vel.x > 0:
                self.acc.x = DECELLERATION_ON_AIR

            if keys[pygame.K_RIGHT] and self.airborne and self.vel.x < 0:
                self.acc.x = -DECELLERATION_ON_AIR

            # mario falls off pit, change to dead mario animation
            if self.pos.y >= self.screen_rect.height + 10:
                self.status = 'dead'

                pygame.mixer.Channel(4).play(pygame.mixer.Sound('resources/sounds/mariodies.wav'))

                self.vel.x = 0
                self.vel.y = -2
                self.pos.y = self.screen_rect.height - 100

            # friction only applies in the x direction

        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        self.check_mushroom_collisions()
        self.check_fireflower_collisions()
        self.check_one_up_mushroom_collisions()
        self.check_starman_collisions()

        self.viewport(viewport)

        self.blitme()
        self.mask = pygame.mask.from_surface(self.image)

        self.check_pole_collisions(pole)

        # timer stuff
        self.delta_time = pygame.time.get_ticks() - self.previous_game_ticks
        self.previous_game_ticks = pygame.time.get_ticks()
        self.one_second_timer -= self.delta_time
        if self.one_second_timer < 0:
            self.one_second_timer += 1000
            self.gui.timer -= 1
            self.gui.update_timer_text()

    def change_image(self, index):

        if self.status == 'small':
            self.image = pygame.image.load(self.small_mario[index]).convert_alpha()
        elif self.status == 'big':
            self.image = pygame.image.load(self.big_mario[index]).convert_alpha()
        elif self.status == 'fire':
            self.image = pygame.image.load(self.fire_mario[index]).convert_alpha()
        elif self.status == 'dead':
            self.image = pygame.image.load(self.small_mario[index]).convert_alpha()

        if self.starman:
            # create a pixel_map of our image to manipulate
            # and animate starman flashing powerup
            self.pix_map = pygame.PixelArray(self.image)

            # get size of x columsn and rows to iterate through
            size_x, size_y = self.pix_map.shape

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                self.star_frames += 11
            if self.airborne:
                self.star_frames -= 10
            if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                self.star_frames += 1

            if 1 <= self.star_frames <= 20:
                for i in range(size_x):
                    for j in range(size_y):
                        rgb = self.get_rgb_from_integer(self.pix_map[i, j])
                        if rgb == (181, 49, 32) or rgb == (255, 255, 255):
                            self.pix_map[i, j] = (12, 147, 0)
                        if rgb == (107, 109, 0) or rgb == (211, 32, 32):
                            self.pix_map[i, j] = (234, 158, 34)
                        if rgb == (234, 158, 34):
                            self.pix_map[i, j] = (255, 254, 255)

            if 21 <= self.star_frames <= 40:
                for i in range(size_x):
                    for j in range(size_y):
                        rgb = self.get_rgb_from_integer(self.pix_map[i, j])
                        if rgb == (181, 49, 32) or rgb == (255, 255, 255):
                            self.pix_map[i, j] = (181, 49, 32)
                        if rgb == (107, 109, 0) or rgb == (211, 32, 32):
                            self.pix_map[i, j] = (234, 158, 34)
                        if rgb == (234, 158, 34):
                            self.pix_map[i, j] = (255, 254, 255)

            if 41 <= self.star_frames <= 60:
                for i in range(size_x):
                    for j in range(size_y):
                        rgb = self.get_rgb_from_integer(self.pix_map[i, j])
                        if rgb == (181, 49, 32) or rgb == (255, 255, 255):
                            self.pix_map[i, j] = (0, 0, 0)
                        if rgb == (107, 109, 0) or rgb == (211, 32, 32):
                            self.pix_map[i, j] = (153, 78, 0)
                        if rgb == (234, 158, 34):
                            self.pix_map[i, j] = (254, 204, 197)

            if self.star_frames >= 61:
                self.star_frames = 0

            # after pixel manipulation assign the image
            # back to pygame surface image
            self.image = self.pix_map.make_surface()

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # for detecting the colors in rgb format

    def get_rgb_from_integer(self, rgb_int):
        blue = rgb_int & 255
        green = (rgb_int >> 8) & 255
        red = (rgb_int >> 16) & 255
        return red, green, blue

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)
