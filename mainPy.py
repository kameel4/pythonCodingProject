from const import *
from player import Player
import pygame as pg
from random import randint


pg.init()
pg.display.set_caption("Space shooter")
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pg.time.Clock()



player = Player(pg.key.get_pressed())
star_surface = pg.image.load("graphics\star.png").convert_alpha()
meteor_surface = pg.image.load("./graphics/meteor.png").convert_alpha()
meteor_rect = meteor_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
laser_surface = pg.image.load("./graphics/laser.png").convert_alpha()
laser_rect = laser_surface.get_rect(bottomleft=(20, WINDOW_HEIGHT-40))
coordinates = []
for ix in range(1, 15, 2):
    for iy in range(1, 9):
        coordinates.append((randint((ix-1) * 100, ix*100), randint((iy-1) * 100, iy*100)))
while running:
    delta_time = clock.tick(165)/1000
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    # player movement
    player.move(delta_time, pg.key.get_pressed())


    # drawing the game
    display_surface.fill('darkgrey')
    for coords in coordinates:
        display_surface.blit(star_surface, coords)
    display_surface.blit(player.surface, player.frect)
    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)
    pg.display.update()


pg.quit()