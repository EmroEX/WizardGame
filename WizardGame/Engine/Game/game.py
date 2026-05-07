import pytmx #pip install pytmx
import pygame #pip install pygame
import pyautogui #pip install pyautogui



class GameMap():


    def __init__(self, ime_fajla):
        self.__width, self.__height = pyautogui.size()  #Dobimo velikost monitorja oz. zaslona, in z priv. spremenljivko onemogočimo slučajno spreminjanje
        self.__zaslon= pygame.display.set_mode((self.__width,self.__height), pygame.FULLSCREEN)
        self.__title = pygame.display.set_caption('WizardGame')
        self.tmx_data = pytmx.load_pygame(ime_fajla)   #To bo convertalo vsako tile sliko
        self.__tile_w=self.tmx_data.tilewidth           
        self.__tile_h=self.tmx_data.tileheight          #Dobimo dolžino in višino tile-a, čeprav že vemo koliko je 64x32 ampak za vsak slučaj, če bi spremenili mapo, da nam kode ni treba spremeniti
        self.__map_w=self.tmx_data.width                
        self.__map_h=self.tmx_data.height
        
        self.offset_x, self.offset_y = self.zamik_središča()
 
        # --- PLAYER ---          TESTNA KODA
        
        self.player_sprite = pygame.image.load(r"Entities\Player\Sprite\New Piskel-1.png").convert_alpha()
        print(self.player_sprite.get_size())
        self.player_sprite = pygame.transform.scale(self.player_sprite,(24, 32))
        

        # tile pozicija (start na sredini)
        self.player_x = self.map_w // 2
        self.player_y = self.map_h // 2
    @property
    def title(self):
        return self.__title
    
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
    
    def iso_preracun(self,x,y):  #Isometrični preračun koordinat
        zaslon_x = (x - y) * (self.tile_w //2)
        zaslon_y = (x+ y) * (self.tile_h // 2)
        return zaslon_x, zaslon_y
    
    def zamik_središča(self):
        center_zaslona_x, center_zaslona_y = self.iso_preracun(self.map_w//2, self.map_h//2)
        zamik_x = self.width // 2 - center_zaslona_x
        zamik_y = self.height // 2 - center_zaslona_y
        return zamik_x, zamik_y
    



    def draw(self):
        for layer in self.tmx_data.visible_layers:   #Vrne X, Y in GID (Id od tile-a), k je type TiledTileLayer v obliki iterable(tuple(int,int,...)) - loh gre v for loop
            if isinstance(layer, pytmx.TiledTileLayer):

                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        iso_x, iso_y = self.iso_preracun(x, y)
                        narisi_x= iso_x + self.offset_x - self.tile_w //2
                        narisi_y = iso_y + self.offset_y

                        self.zaslon.blit(tile,(narisi_x,narisi_y))

        # --- DRAW PLAYER ---      TESTNA KODA
        iso_x, iso_y = self.iso_preracun(self.player_x, self.player_y)

        draw_x = iso_x + self.offset_x - self.player_sprite.get_width() // 2
        draw_y = iso_y + self.offset_y - self.player_sprite.get_height() + 10

        self.zaslon.blit(self.player_sprite, (draw_x, draw_y))