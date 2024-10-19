import pygame as pg


class Laser(pg.sprite.Sprite):
    def __init__(self, surf, pos, *groups):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)
    
    def update(self, delta_time):
        self.rect.y -= 400 * delta_time
        if self.rect.bottom < 0:
            self.kill()
