import pygame as pg


class AnimatedExplsion(pg.sprite.Sprite):
    
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = frames[0]
        self.rect = self.image.get_frect(center=pos)
    
    def update(self, delta_time):
        self.frame_index += 20 * delta_time
        if int(self.frame_index) > 12:
            self.kill()
            return 0
        self.image = self.frames[int(self.frame_index)]