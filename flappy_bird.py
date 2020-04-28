import pygame

win = pygame.display.set_mode((400,600))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))
    pygame.display.update()

pygame.quit()