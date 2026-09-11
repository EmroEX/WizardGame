from pytmx.util_pygame import load_pygame
import pytmx  # pip install pytmx
import pygame  # pip install pygame
# import sys
# sys.path.append(r'./Entities/Player'), sys.path.append(r'./Entities')           #Včasuh tole ne dela, pa ne vem zakaj in je treba dodat ročno to pot. Meni je kazal neko lučko, ker je line bil podčrtan pa pisal je da dodam to pot
from Entities.Player.player import Player
from Engine.Game.camera import naredi_zaslon, camera  #Ta sys path pa from import sta mal confusing ker včasih niti ne vem zakaj ne dela pa ugotavljam
from Entities import entities
from Engine.Game import keyboard
from GUI.Main_Menu.main_menu import main_menu
from Entities.entities import entities



class GameMap():

    def __init__(self, ime_fajla, velikost_zaslona):
        
        self.__zaslon = naredi_zaslon(*velikost_zaslona, 'WizardGame')
        self.zaslon.fill('black')
        # To bo convertalo vsako tile sliko
        self.tmx_data = load_pygame(ime_fajla)

        #print(dir(self.tmx_data))  #Helpful stuff za pogledat kaj je vse v tmx_data, kere metode pa to
        # print(self.tmx_data.layers)  #Dobiš nazaj vse layerje in njihova imena

        self.__tile_w = self.tmx_data.tilewidth
        # Dobimo dolžino in višino tile-a, čeprav že vemo koliko je 64x32 ampak za vsak slučaj, če bi spremenili mapo, da nam kode ni treba spremeniti
        self.__tile_h = self.tmx_data.tileheight
        self.__map_w = self.tmx_data.width
        self.__map_h = self.tmx_data.height

        self.spawn_point=(3302, 2496)
        self.player = Player(*self.spawn_point, r"Entities\Slike\New Piskel-1.png", 100, 2)


        self.zoom = 3
        self.scaled_tiles = {}

        self.tile_map_collision_layer = self.tmx_data.get_layer_by_name('Collision')
        self.scalaing() #Enkrat scalamo
        self.player.začetek()

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


    def can_move(self, rect):

        tile_size = self.tile_w * self.zoom

        koti = [
            rect.topleft,                           #Tale del sem si pomagal z AI, saj te rect mi je bilo bolj težko, da si zamislim
            (rect.right - 1, rect.top),
            (rect.left, rect.bottom - 1),
            (rect.right - 1, rect.bottom - 1)
        ]

        for x, y in koti:

            tile_x = int(x // tile_size)
            tile_y = int(y // tile_size)

            if tile_x < 0 or tile_y < 0:
                return False

            if tile_x >= self.map_w or tile_y >= self.map_h:        #Ta del pa bolj razumem ker gre po collision layerju
                return False

            gid = self.tile_map_collision_layer.data[tile_y][tile_x]
            
            if gid != 0:
                return False

        return True


    def scalaing(self):  # tole poveča tile - so prvotno narisani 32x32, ampak tko bo vse zgledalo večje za pač večkratnik zoom
        for gid in range(1, self.tmx_data.maxgid):  # maxgid dobi število vseh ID-ov
            tile = self.tmx_data.get_tile_image_by_gid(gid)
            if tile:
                scaled_tile = pygame.transform.scale(
                    tile, (self.tile_w * self.zoom, self.tile_h * self.zoom))
                self.scaled_tiles[gid] = scaled_tile

    def draw_game(self):
        
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
        
        #Nisem o tem prej razmišljal pa se ne izrišejo layarji najbolj pravilno zato v igrici pride do tega da se player izriše npr na strehi
        #to pa, ker layarji niso ločeni npr da se drevo ali pa hiša izriše v dveh različnih layarjih, npr spodnji v enem zgornji v drugem. Pri layaru 2 pa 3 se veliko izriše kar celo
        #Mogu bi v tiled-u to spremeniti sam nisem imel dovolj časa ampak, ko pa spremenim se pa doda samo pomožna metoda in se tej draw_game doda parameter layer
        #ta dodatna fukncija pa sam shrani vsak layer posebi v svojo spremenljivko in nato se v določenem vrstem redu vsaka pošlje v draw in se izriše v željenem vrsten redu
        #vmes pa se na določeno npr med layerjem 2 pa 3 vrine player in potem bo pa zgledalo tko kot je treba. Collision pa se itak ne preverja tukaj tko da o tem ni treba razmišljat
def game():

    entities.clear()

    clock = pygame.time.Clock()

    informacije_zaslona = pygame.display.Info()

    width, height = informacije_zaslona.current_w, informacije_zaslona.current_h

    neki = GameMap(r'World\mapa.tmx',(width,height))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 'quit'
            
            elif keyboard.is_key_pressed(pygame.K_ESCAPE):
                return 'menu'
            
            elif event.type == pygame.KEYDOWN:
                keyboard.keys.add(event.key)
                #print((int(neki.player.x), int(neki.player.y)))    #Tako sem prišel do spawn pointa


            elif event.type == pygame.KEYUP:
                if event.key in keyboard.keys:
                    keyboard.keys.remove(event.key)

        #fps = int(clock.get_fps()) #blit 
        #print(int(fps))
                    
        neki.player.update(neki)

        neki.zaslon.fill((30, 30, 30))

        neki.draw_game()
        for e in entities:
            e.draw_sprite(neki.zaslon)

        pygame.display.flip()
        clock.tick(60)