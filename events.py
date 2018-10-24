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
        
def checkKeyDown(event,mario,platforms):
    
    #mario can only run if he is on the floor
    if event.key == pygame.K_f:
        if mario.onFloor:
            mario.running = True

    #character jumps only when he is on the floor
    #this prevents him from doing multiple jumps
    #while on the air
    if event.key == pygame.K_SPACE:
        mario.jump(platforms)
            
    if event.key == pygame.K_DOWN:
        if mario.onFloor:
            mario.crouching = True
        
    if event.key == pygame.K_q:
        sys.exit()

def checkCollisions(mario,platforms,walls):

    #check floor collision and set velocity in the y direction to 0, so that
    #mario does not sink into floor,
    #when there is a collision, set marios y position to the floor tile top coordinate

    if mario.vel.y > 0:
        floorCollision = pygame.sprite.spritecollide(mario,platforms,False)
        if floorCollision:
            mario.vel.y = 0
            mario.pos.y = floorCollision[0].rect.top + 1.2
    



    if not mario.vel.x == 0:
        wallCollision = pygame.sprite.spritecollide(mario,walls,False)
        if wallCollision:
            mario.vel.x = 0
            mario.pos.x = wallCollision[0].rect.left - 15
            