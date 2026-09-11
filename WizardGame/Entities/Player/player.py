import pygame
from Entities.entities import Entities
from Engine.Game.camera import camera
from Engine.Game.keyboard import is_key_pressed
import math


class Player(Entities):
    def __init__(self, x, y, slika, zdravje, hitrost):      #To iz fila entities podeduje neke osnovne stvari ki so tam definirane
        super().__init__(x, y, slika, zdravje, hitrost)


    def začetek(self):                                          #To je poskrbi da je kamera nacentirana na playera in da se player izriše na sredini zaslona na začetku in vsakič k spremeni koordinate
        camera.x=self.x - camera.width // 2 + self.slika.get_width() // 2
        camera.y = self.y - camera.height // 2 + self.slika.get_height() // 2 




    def update(self, game_map):
        v_x = 0
        v_y = 0

        if is_key_pressed(pygame.K_w):              #Tole tukaj je za izračunavanje vektorja premikanja, da bi se player v vse smeri premikal približno enakomerno
            v_y -= 1
        if is_key_pressed(pygame.K_s):
            v_y += 1
        if is_key_pressed(pygame.K_a):
            v_x -= 1
        if is_key_pressed(pygame.K_d):
            v_x += 1

        dolzina = math.sqrt(v_x**2 + v_y**2)
        if dolzina == 0:
            return

        v_x /= dolzina
        v_y /= dolzina
        v_x *= self.move_speed
        v_y *= self.move_speed
                                                                            #Tole dol sem pa naredil, ker me je precej motilo da se diagonalno premika hitreje kot samo v eno smer
        naslednji_rect = self.rect.copy()                       #---- Od kle dol mi je mal AI pomagal, ker nisem mogel ugotoviti točno kako to narest, sem pa bil precej blizu 
        naslednji_rect.x += v_x                                     # Iskreno samo nisem vedel kako poklicati fukncijo/metodo can move tukaj, brez da bi jo importu
        naslednji_rect.y += v_y                                      

        if game_map.can_move(naslednji_rect):        #Tle se preveri diagonalni premik, če je znotraj mape pa brez trkov
            self.move(self.x + v_x, self.y + v_y)
            return

        naslednji_rect_x = self.rect.copy()             #Kako dela vse skupi:
        naslednji_rect_x.x += v_x                       #Najprej preveri ali se lahko premakne po diagonali, če ne potem če lahko po x osi, če tudi to ne pol pa še po y osi                 
        naslednji_rect_y = self.rect.copy()             #- če še ta ne more pa se verjetno ne bo nikamor premaknu
        naslednji_rect_y.y += v_y

        if game_map.can_move(naslednji_rect_x):  #Tle se preveri samo premik po x osi
            self.move(self.x + v_x, self.y)
        elif game_map.can_move(naslednji_rect_y):       #Kle se pa preveri samo po y osi
            self.move(self.x, self.y + v_y)

                                                        #--------- pa do tukaj

    def move(self,x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)    #To pa premakne plejerja in njegov pravokotnik da loh spet računamo a je kakšen trk al ne
        
        self.začetek()

