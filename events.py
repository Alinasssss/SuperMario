import pygame
import sys
from tiles import Tiles
from map import Map
import random


def checkEvents(mario,platforms):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDown(event,mario,platforms)
        elif event.type == pygame.KEYUP:
            checkKeyUp(event,mario)
        
def checkKeyDown(event,mario,platforms):
        
    #character jumps only when he is on the floor
    #this prevents him from doing multiple jumps
    #while on the air
    if event.key == pygame.K_d:
        mario.jump(platforms)
            
    if event.key == pygame.K_DOWN:
        if mario.onFloor:
            mario.crouching = True
        
    if event.key == pygame.K_q:
        sys.exit()

def checkKeyUp(event,mario):
    if event.key == pygame.K_d:
        mario.jumpHeightAdjust()

def checkCollisions(mario,platforms,leftWalls,rightWalls):


    #check head collision and set velocity in the y direction to 0, so that
    #mario stops going up
    #when there is a collision, set marios y position to the block botttom y coordinate

    if mario.vel.y > 0:
        feetCollision = pygame.sprite.spritecollide(mario,platforms,False)
        if feetCollision:
            #print 'floor collides'
            mario.vel.y = 0
            mario.pos.y = feetCollision[0].rect.top+1
    

    if mario.vel.y < 0:
        headCollision = pygame.sprite.spritecollide(mario,platforms,False)
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
            mario.vel.x = 0
            mario.pos.x = wallCollision[0].rect.left - 12
    
    #when mario is moving in the left direction, his velocity is less than 0, 
    #when for collisions with wall
    #move mario forward to position of collision, add 16 since pos.x is midbottom center of mario
    if mario.vel.x < 0:
        wallCollision = pygame.sprite.spritecollide(mario,rightWalls,False)
        if wallCollision:
            mario.vel.x = 0
            mario.pos.x = wallCollision[0].rect.right + 12
    
    
            