import pygame
from Engine.Game.camera import camera

entities = []
loaded = {}


class Entities():
    def __init__(self, x, y, slika, zdravje, hitrost):

        if slika in loaded:
            self.slika = loaded[slika]

        else:
            self.slika = pygame.image.load(slika).convert_alpha()      #convert alpha je pa zaradi transparancija da se pravi izriše
            # scalam playarja ker sem tudi tile povečal pa da bo približno okej zgledal
            self.slika = pygame.transform.scale(self.slika, (32, 48))
            loaded[slika] = self.slika

        self.x = x
        self.y = y
        self.hp = zdravje
        self.move_speed = hitrost
        entities.append(self)
        self.rect = pygame.Rect(self.x, self.y, self.slika.get_width(), self.slika.get_height())

    def draw_sprite(self, screen):
        screen.blit(self.slika, (self.x - camera.x, self.y - camera.y))
        
