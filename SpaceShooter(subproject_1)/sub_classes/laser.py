import pygame as pg


class Laser(pg.sprite.Sprite):
    def __init__(self, surf, pos, *groups):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)
        self.speed = 700
    
    def update(self, delta_time):
        self.rect.y -= self.speed * delta_time
