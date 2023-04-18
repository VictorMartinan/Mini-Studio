import math
import pygame
from Class.bulletHandler import BulletHandler
from Class.particle import Particle

class Player():
    def __init__(self, basicSpeed, slowSpeed, size, displayWidth, displayHeight, dashSpeed,cooldownDash,timeDash, lives, projectileList, imgBullet, imgMissile):
        self.X = 1000
        self.Y = 1000
        self.basicSpeed = basicSpeed
        self.slowSpeed = slowSpeed
        self.speed = basicSpeed
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.dashSpeed = dashSpeed
        self.cooldownDash = cooldownDash
        self.timeDash = timeDash
        self.lives = lives
        self.money = 0
        self.bulletImg = imgBullet
        self.missileImg = imgMissile

        self.projectileList = projectileList
        self.arrayNumber = 3
        self.bulletSpeed = 50
        self.angleBetweenArrays = 10
        #60 = 1sec
        self.timeBetweenShots = 0.3
        self.cooldown = self.timeBetweenShots
        self.timeBetweenMissiles = 0.3
        self.missileCooldown = self.timeBetweenMissiles
        self.timeBetweenUltimates = 60
        self.ultimateCooldown = self.timeBetweenUltimates
        self.ultimateDmg = 50

        self.bulletImg = pygame.image.load("img/bullet.png")
        self.bulletImg = pygame.transform.scale(self.bulletImg, (50, 50))
        self.missileImg = pygame.image.load("img/missile.png")
        self.missileImg = pygame.transform.scale(self.missileImg, (50, 50))

        self.bulletHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.bulletImg, isHoming=False,isPlayer = True)
        self.missileHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.missileImg, isHoming=True,isPlayer = True)

    def move(self, veloX, veloY):
        if veloX != 0 and veloY != 0:
            self.X = self.X + math.sqrt(1/2) * self.speed * veloX
            self.Y = self.Y + math.sqrt(1/2) * self.speed * veloY
        else:
            self.X = self.X + veloX * self.speed
            self.Y = self.Y + veloY * self.speed
        
        #Stop player from going out of the screen
        if self.X > self.displayWidth - self.size:
            self.X = self.displayWidth - self.size
        if self.X < 0:
            self.X = 0
        if self.Y > self.displayHeight - self.size:
            self.Y = self.displayHeight - self.size
        if self.Y < 0:
            self.Y = 0
        self.bulletHandler.move(self.X+self.size/4, self.Y+self.size/4)
        self.missileHandler.move(self.X+self.size/4, self.Y+self.size/4)
    
    def getHit(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            print("You lost")
        

    def shoot(self):
        direction = (0,-1)
        self.bulletHandler.update(direction)

    def shootHoming(self):
        direction = (0,-1)
        self.missileHandler.update(direction)
    
    def shootUltimate(self, particleList):
        ultimateSize = 100
        particleColor = pygame.Color(255,255,255)
        particleCoordinates = pygame.math.Vector2(self.displayWidth/2, self.displayHeight/2)
        particle = Particle(particleCoordinates, ultimateSize, particleColor, particleList)