# Importam te dve stvari posebej, ker nič druzga ne rabim
from pytmx.util_pygame import load_pygame
from pytmx import TiledTileLayer  # pip install pytmx
import pygame  # pip install pygame
# import sys
# sys.path.append(r'./Entities/Player'), sys.path.append(r'./Entities')           #Včasuh tole ne dela, pa ne vem zakaj in je treba dodat ročno to pot. Meni je kazal neko lučko, ker je line bil podčrtan pa pisal je da dodam to pot
from Entities.Player.player import Player
from Engine.Game.camera import naredi_zaslon, camera
from Entities.entities import Entities

spawn_point = (3302, 2496)

class GameMap():

    def __init__(self, ime_fajla):
        self.informacije_zaslona = pygame.display.Info()
        # Dobimo velikost monitorja oz. zaslona, in z priv. spremenljivko onemogočimo slučajno spreminjanje
        self.__width, self.__height = self.informacije_zaslona.current_w, self.informacije_zaslona.current_h
        # self.__zaslon= pygame.display.set_mode((self.__width,self.__height), pygame.FULLSCREEN)
        self.__zaslon = naredi_zaslon(self.width, self.height, 'WizardGame')
        # To bo convertalo vsako tile sliko
        self.tmx_data = load_pygame(ime_fajla)

        print(dir(self.tmx_data))  #Helpful stuff za pogledat kaj je vse v tmx_data, kere metode pa to
        # print(self.tmx_data.layers)  #Dobiš nazaj vse layerje in njihova imena

        self.__tile_w = self.tmx_data.tilewidth
        # Dobimo dolžino in višino tile-a, čeprav že vemo koliko je 64x32 ampak za vsak slučaj, če bi spremenili mapo, da nam kode ni treba spremeniti
        self.__tile_h = self.tmx_data.tileheight
        self.__map_w = self.tmx_data.width
        self.__map_h = self.tmx_data.height

        self.player = Player(*spawn_point, r"Entities\Slike\New Piskel-1.png", 100, 2)

        self.zoom = 3
        self.scaled_tiles = {}

    @property
    def zaslon(self):
        return self.__zaslon

    @property
    def tile_w(self):
        return self.__tile_w

    @property
    def tile_h(self):
        return self.__tile_h

    @property
    def map_w(self):
        return self.__map_w

    @property
    def map_h(self):
        return self.__map_h

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def world_w(self):
        return self.map_w * self.tile_w * self.zoom
    
    @property
    def world_h(self):
        return self.map_h * self.tile_h * self.zoom
    
    def can_move(self, x, y):
        if 0 <= x <= self.world_w - self.player.slika.get_width():
            return True
        
        if 0 <= x <= self.world_h - self.player.slika.get_height():
            return True 
        

    def scalaing(self):  # tole poveča tile - so prvotno narisani 32x32, ampak tko bo vse zgledalo večje
        for gid in range(1, self.tmx_data.maxgid):  # maxgid dobi število vseh ID-ov
            tile = self.tmx_data.get_tile_image_by_gid(gid)
            if tile:
                scaled_tile = pygame.transform.scale(
                    tile, (self.tile_w * self.zoom, self.tile_h * self.zoom))
                self.scaled_tiles[gid] = scaled_tile

    def draw(self):
        self.scalaing()
        # Vrne X, Y in GID (Id od tile-a), k je type TiledTileLayer v obliki iterable(tuple(int,int,...)) - loh gre v for loop. gid je pa tisti seznam layerjev iz tmx datoteke
        for layer in self.tmx_data.visible_layers:

            for x, y, gid in layer:
                # print(x)
                # print(y)
                # print(gid)
                tile = self.scaled_tiles.get(gid)

                if tile:

                    # tukaj nisem čisto ziher zakaj moramo še enkrat množit z zoom-om, če ne pride mapa zelo čudno izrisana
                    narisi_x = x * self.tile_w * self.zoom - camera.x
                    narisi_y = y * self.tile_h * self.zoom - camera.y

                    self.zaslon.blit(tile, (narisi_x, narisi_y))
