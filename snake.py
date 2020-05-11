import pygame

win = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
global scl
scl = 20

class Snake:
    def __init__(self,win):
        self.win = win
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0

    def update(self):
        self.x += self.xspeed*scl
        self.y += self.yspeed*scl

    def show(self):
        pygame.draw.rect(self.win,(255,255,255),(self.x,self.y,scl,scl))

    def dir(self,x,y):
        self.xspeed = x
        self.yspeed = y

    def eat(self,pos):
        pass


def drawWindow(s):
    s.update()
    s.show()
    pygame.display.update()

s = Snake(win)
run = True
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        s.dir(0,-1)
    elif keys[pygame.K_DOWN]:
        s.dir(0,1)
    elif keys[pygame.K_RIGHT]:
        s.dir(1,0)
    elif keys[pygame.K_LEFT]:
        s.dir(-1,0)
    if  s.x < 0:
        s.x = 0
    elif s.x + scl > 600:
        s.x  = 580
    elif s.y < 0:
        s.y = 0
    elif s.y + scl > 600:
        s.y  = 580


    win.fill((51,51,51))
    drawWindow(s)

pygame.quit()