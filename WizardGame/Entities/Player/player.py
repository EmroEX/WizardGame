import pygame
from Entities.entities import Entities
from Engine.Game.camera import camera


class Player(Entities):
    def __init__(self, x, y, slika, zdravje, hitrost):
        super().__init__(x, y, slika, zdravje, hitrost)

    def začetek(self):
        camera.x=self.x - camera.width // 2 + self.slika.get_width() // 2
        camera.y = self.y - camera.height // 2 + self.slika.get_height() // 2

    def update():
        pass

    def move(self, x2, y2):
        
        self.x += x2
        self.y += y2
        self.začetek()
