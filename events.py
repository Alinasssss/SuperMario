import pygame
import sys
from tiles import Tiles
from map import Map
import random


def checkEvents(mario,platformsTop):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDown(event,mario,platformsTop)
        elif event.type == pygame.KEYUP:
            checkKeyUp(event,mario)
        
def checkKeyDown(event,mario,platformsTop):
        
    #character jumps only when he is on the floor
    #this prevents him from doing multiple jumps
    #while on the air
    if event.key == pygame.K_d:
        mario.jump(platformsTop)
            
    if event.key == pygame.K_DOWN:
        if mario.onFloor:
            mario.crouching = True
        
    if event.key == pygame.K_q:
        sys.exit()

def checkKeyUp(event,mario):
    if event.key == pygame.K_d:
        mario.jumpHeightAdjust()

def checkCollisions(mario,platformsTop,platformsBottom,leftWalls,rightWalls):

    #mario is coming down after having jumped, colide with top platform
    if mario.vel.y > 0:
        feetCollision = pygame.sprite.spritecollide(mario,platformsTop,False)
        if feetCollision:
            #print 'floor collides'
            mario.vel.y = 0
            mario.pos.y = feetCollision[0].rect.top+1
            mario.airborne = False
            
    #mario is jumping check if colllision with his head
    if mario.vel.y < 0:
        headCollision = pygame.sprite.spritecollide(mario,platformsBottom,False)
        if headCollision:
            print 'head collides'
            mario.vel.y = mario.vel.y * -1
            mario.pos.y = headCollision[0].rect.bottom + 36

    
    #when mario is moving in the right direction, his velocity is greater than 0, 
    #check for collisions with wall
    #move mario back to position of collision, subtract 16 since pos.x is midbottom center of mario
    if mario.vel.x > 0:
        wallCollision = pygame.sprite.spritecollide(mario,leftWalls,False)
        if wallCollision:
            print 'left wall collision'
            mario.vel.x = 0
            mario.pos.x = wallCollision[0].rect.left - 12
    
    #when mario is moving in the left direction, his velocity is less than 0, 
    #when for collisions with wall
    #move mario forward to position of collision, add 16 since pos.x is midbottom center of mario
    if mario.vel.x < 0:
        wallCollision = pygame.sprite.spritecollide(mario,rightWalls,False)
        if wallCollision:
            print 'right wall collision'
            mario.vel.x = 0
            mario.pos.x = wallCollision[0].rect.right + 12
    
    
            