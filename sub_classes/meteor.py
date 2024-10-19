import pygame as pg
from const import *

class Meteor(pg.sprite.Sprite):
    def __init__(self, surf, pos, *groups):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_frect()
        self.rect.center = pos
    
    def update(self, delta_time):
        self.rect.y += 200 * delta_time
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()