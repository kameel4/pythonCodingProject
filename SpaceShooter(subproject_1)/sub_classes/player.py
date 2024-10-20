import pygame as pg
from .laser import Laser
from .const import *

class Player(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load("SpaceShooter(subproject_1)/graphics\starship.png").convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT*0.8))
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 450
        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

        #mask
        self.mask = pg.mask.from_surface(self.image)


        #laser
        self.laser_surf = pg.image.load("SpaceShooter(subproject_1)/graphics/purplLaser.png").convert_alpha()
        self.laser_group = pg.sprite.Group()


    def move(self, deltat, keys):
        self.direction.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.direction.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        self.direction = self.direction.normalize() if self.direction.magnitude() != 0 else self.direction
        self.rect.center += self.direction * self.speed * deltat


    
    def shoot(self):
        if self.can_shoot:
            Laser(self.laser_surf, self.rect.midtop, self.laser_group)
            self.laser_shoot_time = pg.time.get_ticks()
            self.can_shoot = False
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pg.time.get_ticks()
            if current_time - self.laser_shoot_time > self.cooldown_duration:
                self.can_shoot = True

    
    def update(self, delta_time, *args, **kwargs):
        self.laser_timer()
        keys = pg.key.get_pressed()
        self.move(delta_time, keys, *args, **kwargs)

        recent_keys = pg.key.get_just_pressed()
        if recent_keys[pg.K_SPACE]:
            self.shoot()
        return super().update(*args, **kwargs)


        