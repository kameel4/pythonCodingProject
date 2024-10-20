from sub_classes.const import *
from sub_classes.player import Player
from sub_classes.star import Star
from sub_classes.meteor import Meteor
from sub_classes.animatedExplsion import AnimatedExplsion
import pygame as pg
from random import randint

def collision():
    global running
    meteor_laser_collision = pg.sprite.groupcollide(meteor_sprites, player.laser_group, True, True)
    if meteor_laser_collision:
        AnimatedExplsion(explsion_frames, list(meteor_laser_collision.keys())[0].rect.center, all_sprites)

    if pg.sprite.spritecollide(player, meteor_sprites, False, pg.sprite.collide_mask):
        running = False

def display_score(d_surface):
    current_time = pg.time.get_ticks()
    text_surf = font.render(f"Score: {int(current_time/100)}", True, (255, 255, 255))
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH/2, WINDOW_HEIGHT-100))
    d_surface.blit(text_surf, text_rect)
    pg.draw.rect(d_surface, (240, 240, 240), text_rect.inflate(10, 10), 3, 10)

def increase_frequency():
    global meteor_spawn_frequency
    meteor_spawn_frequency -= 150
    if meteor_spawn_frequency <= 50:
        meteor_spawn_frequency = 50
    pg.time.set_timer(meteor_event, int(meteor_spawn_frequency/(1 + (pg.time.get_ticks()/1000)*0.1)))

pg.init()
pg.display.set_caption("Space shooter")
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pg.time.Clock()

# sprites
all_sprites = pg.sprite.Group()
meteor_sprites = pg.sprite.Group()

# image loads
meteor_surface = pg.image.load("SpaceShooter(subproject_1)/graphics/meteor.png").convert_alpha()
background_surface = pg.image.load("SpaceShooter(subproject_1)/graphics/background1.png").convert()
explsion_frames = [pg.image.load(f"SpaceShooter(subproject_1)/graphics/explosion_frames/frame{i}.png") for i in range(13)]

font = pg.font.Font(None, 20)
text_surface = font.render("test", True, (255, 255, 255))

player = Player(all_sprites)

# for _ in range(30):
#     star = Star(star_surface, (all_sprites, stars_group))

#custom event
meteor_event = pg.event.custom_type()
meteor_spawn_frequency = 1000
pg.time.set_timer(meteor_event, int(meteor_spawn_frequency/(1 + (pg.time.get_ticks()/1000)*0.1)))




while running:
    delta_time = clock.tick(165)/1000
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(meteor_surface, (randint(0, WINDOW_WIDTH), 0), (all_sprites, meteor_sprites)) 
   
   
    # updating the game
    all_sprites.update(delta_time)
    player.laser_group.update(delta_time)

    if pg.time.get_ticks() % 3000==0:
        increase_frequency()

    # drawing the game
    display_surface.blit(background_surface, (0, 0))
    display_score(display_surface)
    all_sprites.draw(display_surface)
    player.laser_group.draw(display_surface)


    # collision
    collision()


    pg.display.update()


pg.quit()
