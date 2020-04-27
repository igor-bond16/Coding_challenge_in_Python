import pygame
import math
import numpy as np

win = pygame.display.set_mode((600,400))

class Ship:
    def __init__(self,win):
        self.x = 300
        self.y = 350
        self.width = 20
        self.height = 40
        self.vel = 1
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win,(255,255,255),(self.x,self.y,self.width,self.height),0)

    def move(self,keys):
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        elif keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel

class Flower:
    def __init__(self,win,x):
        self.x = x
        self.y = 100
        self.radius = 30
        self.win = win
        self.hitcircle = (self.x,self.y)
        self.xdir = 1
        self.ydir = 0
        self.edge = False
        self.moveloop = 0

    def draw(self):
        pygame.draw.circle(self.win,(255,0,200), (self.x,self.y), self.radius)
        self.hitcircle = (self.x,self.y)

    def grow(self,flower):
        self.radius += 2

    def move(self):
        self.x += self.xdir

    def shiftDown(self):
        self.xdir *= -1
        self.y += self.radius
        self.edge = False


class Drop:
    def __init__(self,win,x):
        self.win = win
        self.y =  350
        self.vel = 10
        self.x = x
        self.r = 8

    def draw(self):
        pygame.draw.rect(self.win,(150,0,255),(self.x,self.y,self.r*2,self.r*2),0)

    def collide(self,drop,flower):
        dist = math.sqrt(np.abs(flower.hitcircle[0]-drop.x)**2+np.abs(flower.hitcircle[1]-drop.y)**2)
        if dist < 38:
            return True
        return False 

def drawWindow(ship,drops):
    ship.draw()

    for i in drops:
        i.draw()

    for b in flowers:
        b.draw()
        b.move()  

    pygame.display.update()

drops = []
flowers = []
shootloop = 0
for i in range(6):
    x = i*80 + 80
    flowers.append(Flower(win,x))
ship = Ship(win)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
    
    keys = pygame.key.get_pressed()

    if shootloop > 0:
        shootloop += 1
    if shootloop > 20:
        shootloop = 0

    if keys[pygame.K_SPACE] and shootloop == 0:
        if len(drops) <= 10:
            drops.append(Drop(win,ship.x))
        
        shootloop = 1

    for drop in drops:
        if drop.y > 0:
            drop.y -= 1
        else:
            drops.pop(drops.index(drop))    
        
        for flower in flowers:
            if drop.collide(drop,flower):
                flower.grow(flower)
                drops.pop(drops.index(drop))

    for flower in flowers:
        if flower.x > 600 or flower.x < 0:
            flower.edge = True

        if flower.edge:
            flower.shiftDown()

    ship.move(keys)
    win.fill((51,51,51))
    drawWindow(ship,drops)

pygame.quit()
