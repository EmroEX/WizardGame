import pygame

camera = pygame.Rect(0, 0, 0, 0)


def naredi_zaslon(width, height, ime):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(ime)

    camera.width, camera.height = width, height
    return screen
