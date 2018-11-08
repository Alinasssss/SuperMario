import pygame
import sys
import settings as s
from fireball import Fireball


def check_events(mario, platforms_top,screen,fireballs,viewport):
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, mario, platforms_top,screen,fireballs,viewport)
        elif event.type == pygame.KEYUP:
            check_key_up(event, mario)


def check_key_down(event, mario, platforms_top,screen,fireballs,viewport):
    # character jumps only when he is on the floor. this prevents him from doing multiple jumps while in the air
    if event.key == pygame.K_d:
        if not mario.finish:
            mario.jump(platforms_top)

    if event.key == pygame.K_f:
        if not mario.finish:
            if mario.status == 'fire':
                if len(fireballs) <2:
                
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound('resources/sounds/fireball.wav'))
            
                    if mario.direction == "right":
                        mario.change_image(15)
                        fireball = Fireball(screen,mario)
                    elif mario.direction == 'left':
                        mario.change_image(16)
                        fireball = Fireball(screen,mario)
                
                    fireballs.add(fireball)
                    viewport.add(fireballs)
                    
        
    if event.key == pygame.K_q:
        sys.exit()


def check_key_up(event, mario):
    if not mario.finish:
        
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
            

def check_collisions(mario, platforms_top, platforms_bottom, left_walls, right_walls,fireballs,mystery_tiles,brick_tiles,coins,entity_gamemaster):
    # mario is coming down after having jumped, collide with top platform
    if mario.vel.y > 0:
        feet_collisions = pygame.sprite.spritecollide(mario, platforms_top, False)
        if feet_collisions:
            mario.vel.y = 0
            mario.pos.y = feet_collisions[0].rect.top+1
            mario.airborne = False
        if feet_collisions and mario.finish:
            pygame.mixer.Channel(5).play(pygame.mixer.Sound('resources/sounds/stage_clear.wav'))
            mario.finish = False
            mario.pos.x += 42
    
            
    # mario collides with his head
    if mario.vel.y < 0:
        head_collision = pygame.sprite.spritecollide(mario, platforms_bottom, False)
        if head_collision:
            mario.vel.y = 1

            head_collision[0].rect.y -= 23

            #check what other components this bottom platforms collides with and move them up by the same amount
            mystery_collision = pygame.sprite.spritecollide(head_collision[0],mystery_tiles,False)
            if mystery_collision:
                if mystery_collision[0].status == 'new':
                    mystery_collision[0].rect.y -= 23

                    top_collision = pygame.sprite.spritecollide(mystery_collision[0],platforms_top,False)
                    if top_collision:
                        top_collision[0].rect.y -= 23
                
                    left_collision = pygame.sprite.spritecollide(mystery_collision[0],left_walls,False)
                    if left_collision:
                        left_collision[0].rect.y -= 23
                    
                    right_collision = pygame.sprite.spritecollide(mystery_collision[0],right_walls,False)
                    if right_collision:
                        right_collision[0].rect.y -= 23
                    
                    coin_collision = pygame.sprite.spritecollide(mystery_collision[0],coins,False)
                    if coin_collision:
                        pygame.mixer.Channel(6).play(pygame.mixer.Sound('resources/sounds/coin.wav'))
                        coin_collision[0].rect.y -= 95
                    

                    if mario.status == 'small':
                        mushroom_collision = pygame.sprite.spritecollide(mystery_collision[0],entity_gamemaster.mushrooms,False)
                        if mushroom_collision:
                            pygame.mixer.Channel(7).play(pygame.mixer.Sound('resources/sounds/powerup_appears.wav'))
                            mushroom_collision[0].rect.y -= 29
                            mushroom_collision[0].start_movement = True
                    
                    if not mario.status == 'small':
                        flower_collision = pygame.sprite.spritecollide(mystery_collision[0],entity_gamemaster.fireflowers,False)
                        if flower_collision:
                            pygame.mixer.Channel(7).play(pygame.mixer.Sound('resources/sounds/powerup_appears.wav'))
                            flower_collision[0].rect.y -= 29
                    
                    star_collision = pygame.sprite.spritecollide(mystery_collision[0],entity_gamemaster.starmen,False)
                    if star_collision:
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('resources/sounds/powerup_appears.wav'))
                        
                        star_collision[0].rect.y -= 29
                        star_collision[0].start_movement = True


                    mystery_collision[0].status = 'used'
                
            #check what other components this bottom platforms collides with and move them up by the same amount
            brick_collision = pygame.sprite.spritecollide(head_collision[0],brick_tiles,False)
            if brick_collision:
                brick_collision[0].rect.y -= 23
                

                top_collision = pygame.sprite.spritecollide(brick_collision[0],platforms_top,False)
                if top_collision:
                    if mario.status == 'big' or mario.status == 'fire':
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('resources/sounds/break.wav'))
                        top_collision[0].rect.y -= 23
                        top_collision[0].kill()
                
                    else:
                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('resources/sounds/bump.wav'))
                        top_collision[0].rect.y -= 23
                
                left_collision = pygame.sprite.spritecollide(brick_collision[0],left_walls,False)
                if left_collision:
                    if mario.status == 'big' or mario.status == 'fire':
                        left_collision[0].rect.y -= 23
                        left_collision[0].kill()
                    else:
                        left_collision[0].rect.y -= 23
                    
                right_collision = pygame.sprite.spritecollide(brick_collision[0],right_walls,False)
                if right_collision:
                    if mario.status == 'big' or mario.status == 'fire':
                        for r in right_collision:
                            r.kill()
                            
                    else:
                        for r in right_collision:
                            r.rect.y -= 23
                        
                if mario.status == 'big' or mario.status == 'fire':
                    brick_collision[0].kill()

                if mario.status == 'big' or mario.status =='fire':
                    head_collision[0].kill()
            
            

            
            
            

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