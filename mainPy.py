import pygame as pg
from const import *
from sys import exit

pg.init()
screen = pg.display.set_mode((WIDGHT, HEIGHT))
pg.display.set_caption("Runner")
clock = pg.time.Clock()



test_surface = pg.image.load('graphics/small_sky_background.png')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(test_surface, (0, 0)) 
    
    pg.display.update()
    clock.tick(FPS)