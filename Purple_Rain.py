
import pygame
import random

WIDTH = 640
HEIGHT = 360

win = pygame.display.set_mode((WIDTH,HEIGHT))

class Drop:
    def __init__(self,win):
        self.x = random.uniform(0,WIDTH)
        self.y = -1
        self.yspeed = random.uniform(1,3)
        self.win = win
        self.length = random.uniform(10,20)

    def fall(self):
        self.y += self.yspeed

    def show(self):
        pygame.draw.rect(self.win,(138,43,226),(self.x,self.y,2,self.length))

def drawWindow(rain):
    for water in rain:
        water.show()
        if water.y <= 360:
            water.fall()
        else:
            rain.pop(rain.index(water))

    pygame.display.update()

rain = []
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((230,230,250))
    
    if len(rain) < 500:
        rain.append(Drop(win))

    drawWindow(rain)
pygame.quit()