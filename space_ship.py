import pygame
from pygame.locals import *
import math,random

WIDTH = 640
HEIGHT = 480
ground = [(0,479),(150,300),(300,430),(420,430),(500,350),(639,479)]
goal = (330,430,60,10)
star = []
for i in range(30):
    star.append((random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1),2,2))
    
pygame.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.joystick.init()
if pygame.joystick.get_count == 0:
    print('Joystick not found')
joystick = pygame.joystick.Joystick(0)
joystick.init()
img = pygame.image.load('/home/pi/Downloads/ship3.jpg')
img.set_colorkey((0,0,0),RLEACCEL)
x = 160
y = 16
x1 = 0
y1 = 0
scale = 2
angle = 0
message = ''
myfont = pygame.font.Font(None,70)
myclock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    surface.fill((0,0,0))
    for i in range(30):
        pygame.draw.rect(surface,(0,0,255),star[i])
        
    pygame.draw.polygon(surface,(0,255,0),ground)
    pygame.draw.rect(surface,(255,0,0),goal)
    if message == '':
        col = surface.get_at((int(x),int(y+16)))
        if col.g >= 255:
            message = 'failed'
        if col.r >= 255:
            if y1 >= 0.5:
                message = 'failed'
            else:
                message = 'succeeded'
                
    ax = joystick.get_axis(0)
    ay = joystick.get_axis(1)
    if math.fabs(ax) >= 0.2:
        angle = angle - ax
    boost = -ay
    if boost < 0.2:
        boost = 0
    rd = math.radians(-angle-90)
    x1 += (math.cos(rd)*boost/100)
    y1 += (math.sin(rd)*boost/100)
    xb = int(x - math.cos(rd)*16)
    yb = int(y - math.sin(rd)*16)
    r = int(16*boost)
    pygame.draw.circle(surface,(255,255,255),(xb,yb),r)
    y1 += 0.005
    x += x1
    y += y1
    if x < 0:
        x = 0
    if x > WIDTH-1:
        x = WIDTH-1
    if y < 0:
        y = 0
    if y > HEIGHT-1:
        y=HEIGHT-1
        
    img2 = pygame.transform.rotozoom(img,angle,scale)
    chrw = img2.get_width()
    chrh = img2.get_height()
    surface.blit(img2,(x-(chrw/2),y - (chrh/2)))
    bitmaptext = myfont.render(message,True,(255,255,255))
    surface.blit(bitmaptext,(200,240))
    pygame.display.update()
    myclock.tick(60)

pygame.quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
