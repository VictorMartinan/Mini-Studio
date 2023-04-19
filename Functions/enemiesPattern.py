import sys
import pygame
sys.path.append("/Mini-studio/Class")
#from Class.enemy import Enemy

def firstPattern(Enemy):
    
    if Enemy.x <= 0:
        Enemy.facing = "right"
        Enemy.patternStep = 0
    elif Enemy.x >= 1920 - Enemy.size:
        Enemy.facing = "left"
        Enemy.patternStep = 0

    if Enemy.facing == "right" and Enemy.x == 0:
        Enemy.move(Enemy.speed, 1)
    elif Enemy.facing == "right" and Enemy.patternStep%6 == 0 and Enemy.patternStep < (1920 - Enemy.size)//2//Enemy.speed:
        Enemy.move(Enemy.speed, 0)
    elif Enemy.facing == "right" and Enemy.patternStep <= (1920 - Enemy.size)//2//Enemy.speed:
        Enemy.move(Enemy.speed, 1)
    
    if Enemy.facing == "right" and Enemy.patternStep > (1920 - Enemy.size)//2//Enemy.speed and (((Enemy.patternStep-(1920-Enemy.size))//2)//Enemy.speed)%6  == 0:
        Enemy.move(Enemy.speed, 0)
    elif Enemy.facing == "right" and Enemy.patternStep > (1920 - Enemy.size)//2//Enemy.speed:
        Enemy.move(Enemy.speed, -1)

    if Enemy.facing == "left" and Enemy.patternStep == (1920 - Enemy.size)//Enemy.speed:
        Enemy.move(-Enemy.speed, 1)
    elif Enemy.facing == "left" and Enemy.patternStep%6 == 0 and Enemy.patternStep < (1920 - Enemy.size)//2//Enemy.speed:
        Enemy.move(-Enemy.speed, 0)
    elif Enemy.facing == "left" and Enemy.patternStep <= (1920 - Enemy.size)//2//Enemy.speed:
        Enemy.move(-Enemy.speed, 1)
    
    if Enemy.facing == "left" and Enemy.patternStep > (1920 - Enemy.size)//2//Enemy.speed and (((Enemy.patternStep-(1920-Enemy.size))//2)//Enemy.speed)%6 == 0:
        Enemy.move(-Enemy.speed, 0)
    elif Enemy.facing == "left" and Enemy.patternStep > (1920 - Enemy.size)//2//Enemy.speed:
        Enemy.move(-Enemy.speed, -1)

    Enemy.patternStep += 1
    Enemy.bulletHandler.move(Enemy.x, Enemy.y)