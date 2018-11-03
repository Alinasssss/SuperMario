import pygame
import sys
import settings as s
from fireball import Fireball


def check_events(mario, platforms_top,screen,fireballs):
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, mario, platforms_top,screen,fireballs)
        elif event.type == pygame.KEYUP:
            check_key_up(event, mario)


def check_key_down(event, mario, platforms_top,screen,fireballs):
    # character jumps only when he is on the floor. this prevents him from doing multiple jumps while in the air
    if event.key == pygame.K_d:
        mario.jump(platforms_top)

    if event.key == pygame.K_DOWN:
        if mario.onFloor:
            mario.crouching = True
    
    if event.key == pygame.K_f:
        if mario.status == 'fire':
            if len(fireballs) <2:
                if mario.direction == "right":
                    mario.change_image(14)
                    fireball = Fireball(screen,mario)
                elif mario.direction == 'left':
                    mario.change_image(15)
                    fireball = Fireball(screen,mario)
                
                fireballs.add(fireball)
                    
        
    if event.key == pygame.K_q:
        sys.exit()


def check_key_up(event, mario):
    if event.key == pygame.K_d:
            mario.jump_height_adjust()
    if event.key == pygame.K_RIGHT:
        if mario.vel.x >= 0 and not mario.airborne:
            mario.frames = 0
            mario.change_image(0)
            
    if (event.key == pygame.K_LEFT and mario.vel.y > 0 and not mario.airborne) or (mario.vel.y == 0):
        if mario.vel.x <= 0 and not mario.airborne:
            mario.frames = 0
            mario.change_image(6)
            

def check_collisions(mario, platforms_top, platforms_bottom, left_walls, right_walls,fireballs):
    # mario is coming down after having jumped, collide with top platform
    if mario.vel.y > 0:
        feet_collisions = pygame.sprite.spritecollide(mario, platforms_top, False)
        if feet_collisions:
            mario.vel.y = 0
            mario.pos.y = feet_collisions[0].rect.top+1
            mario.airborne = False
            
    # mario collides with his head
    if mario.vel.y < 0:
        head_collision = pygame.sprite.spritecollide(mario, platforms_bottom, False,pygame.sprite.collide_mask)
        if head_collision:
            mario.vel.y = 0
            

    # when mario is moving in the right direction, his velocity is greater than 0,
    # check for collisions with wall
    # move mario back to position of collision, subtract 16 since pos.x is midbottom center of mario
    if mario.vel.x > 0:
        wall_collision = pygame.sprite.spritecollide(mario, left_walls, False)
        if wall_collision:
            mario.vel.x = 0
            mario.pos.x = wall_collision[0].rect.left - 12
    
    # when mario is moving in the left direction, his velocity is less than 0,
    # when for collisions with wall
    # move mario forward to position of collision, add 16 since pos.x is midbottom center of mario
    if mario.vel.x < 0:
        wall_collision = pygame.sprite.spritecollide(mario, right_walls, False)
        if wall_collision:
            mario.vel.x = 0
            mario.pos.x = wall_collision[0].rect.right + 12