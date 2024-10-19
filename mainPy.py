from const import *
from sub_classes.player import Player
from sub_classes.star import Star
from sub_classes.meteor import Meteor
import pygame as pg
from random import randint


pg.init()
pg.display.set_caption("Space shooter")
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pg.time.Clock()


all_sprites = pg.sprite.Group()
stars_group = pg.sprite.Group()
laser_surf = pg.image.load("graphics\laser.png").convert_alpha()
star_surface = pg.image.load("graphics\star.png").convert_alpha()
meteor_surface = pg.image.load("graphics\meteor.png").convert_alpha()
player = Player(all_sprites)

for _ in range(30):
    star = Star(star_surface, stars_group)

#custom event
meteor_event = pg.event.custom_type()
pg.time.set_timer(meteor_event, 1000)


while running:
    delta_time = clock.tick(165)/1000
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(meteor_surface, (randint(0, WINDOW_WIDTH), 0), all_sprites)
    # updating the game
    all_sprites.update(delta_time)

    # drawing the game
    display_surface.fill('darkgrey')
    stars_group.draw(display_surface)
    all_sprites.draw(display_surface)
    pg.display.update()


pg.quit()