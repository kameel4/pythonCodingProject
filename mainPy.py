from const import *
import pygame
from random import randint


pygame.init()
pygame.display.set_caption("Space shooter")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
#plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100


player_surface = pygame.image.load("graphics\starship.png").convert_alpha()
star_surface = pygame.image.load("graphics\star.png").convert_alpha()
coordinates = []
for ix in range(1, 15, 2):
    for iy in range(1, 9):
        coordinates.append((randint((ix-1) * 100, ix*100), randint((iy-1) * 100, iy*100)))
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #drawing the game
    display_surface.fill('darkgrey')
    x+=0.1
    for coords in coordinates:
        display_surface.blit(star_surface, coords)
    display_surface.blit(player_surface, (x, 150))
    pygame.display.update()


pygame.quit()