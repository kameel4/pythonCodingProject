import pygame as pg
from random import uniform, randint
from .const import *

class Meteor(pg.sprite.Sprite):
    def __init__(self, surf, pos, *groups):
        super().__init__(*groups)
        self.original_image = surf

        self.image = self.original_image
        self.rotation = 0
        self.rotation_speed = randint(-100, 100)

        self.rect = self.image.get_frect()
        self.rect.center = pos
        self.speed = randint(200, 400)
        self.direction = pg.math.Vector2(uniform(-0.5, 0.5), 1)
        
    def update(self, delta_time):
        self.image = pg.transform.rotozoom(self.original_image, self.rotation, 1)
        self.rect = self.image.get_frect(center=self.rect.center)
        self.rotation += self.rotation_speed * delta_time
        self.rect.center += self.direction * self.speed * delta_time 
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()