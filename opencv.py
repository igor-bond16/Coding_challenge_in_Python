import pygame
import math
import random

pygame.init()
win = pygame.display.set_mode((750, 650))

def drawTree(a, b, pos, deepness):
   if deepness:
      branch1 = random.randint(1,10)
      branch2 = random.randint(1,10)
      c = a + int(math.cos(math.radians(pos)) * deepness * branch1)
      d = b + int(math.sin(math.radians(pos)) * deepness * branch2)
      pygame.draw.line(win, (255,255,255), (a, b), (c, d), 1)
      drawTree(c, d, pos - 20, deepness - 1)
      drawTree(c, d, pos + 20, deepness- 1)
   else:
      pygame.draw.circle(win,(0,255,0),(a,b),2,0)

drawTree(370, 650, -90,10)
pygame.display.flip()
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()