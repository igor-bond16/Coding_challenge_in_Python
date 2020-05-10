import pygame
import math
import sys


width = 400

win = pygame.display.set_mode((width,width))
win.fill((51,51,51))
sys.setrecursionlimit(5000)
length = 100
sita = math.pi/4
pos_list = []
x = 200
y = 300

pygame.draw.line(win,(255,255,255),(200,400),(200,300))

def branch(length,current_x,current_y):
    if length < 4:
        return 0
    new_x = current_x+math.cos(13*math.pi/36)*length
    new_y = current_y-math.sin(13*math.pi/36)*length
   # pos_list.append((new_x,new_y))
    pygame.draw.line(win,(255,255,255),(current_x,current_y),(new_x,new_y))
    length *= 0.67
    current_x = new_x
    current_y = new_y
    pos_list.append((current_x,current_y))
    pos_list.append((new_x,new_y))
    branch (length,current_x,current_y)
    
    

def drawWindow():
    branch(100,x,y)
    pygame.display.update()

drawWindow()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        #drawWindow()
    
pygame.quit()
