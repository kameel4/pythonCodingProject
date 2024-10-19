import pygame as pg
from const import *

class Player(pg.sprite.Sprite):
    def __init__(self, keys, *groups):
        super().__init__(*groups)
        self.surface = pg.image.load("graphics\starship.png").convert_alpha()
        self.frect = self.surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT*0.8))
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 300
    
    def move(self, deltat, keys):
        self.direction.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.direction.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        self.direction = self.direction.normalize() if self.direction.magnitude() != 0 else self.direction
        self.frect.center += self.direction * self.speed * deltat
        