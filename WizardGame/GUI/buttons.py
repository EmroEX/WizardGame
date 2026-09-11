import pygame
                                                
pygame.font.init()  

class Button():
    def __init__(self, slika, x, y,niz,font, barva, druga_barva):                    #Kle se incializirajo stvari ki jih rabimo
        self.slika = slika
        self.x = x
        self.y =y
        self.niz = niz
        self.font = font
        self.barva = barva
        self.druga_barva = druga_barva
        self.fontiran_niz = self.font.render(self.niz, True, self.barva)
        if self.slika is None:
            self.slika = self.fontiran_niz
        self.rect = self.slika.get_rect(center=(self.x,self.y))   #Funkcija center sprejme 2 argumenta in pač centrira nek string za določeno dolžino, privzeto za space 
        self.niz_rect = self.fontiran_niz.get_rect(center=(self.x, self.y))

    def update(self, screen):
        if self.slika is not None:                                                  #Tekst se izriše na ekran
            screen.blit(self.slika, self.rect)
        screen.blit(self.fontiran_niz, self.niz_rect)

    def vnosi(self, x,y):                                   #Preverjamo če gor hoveramo z miško 
        if x in range(self.rect.left, self.rect.right) and y in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def spremeni_barvo(self, x,y ):                            #Če goveramo pol se barva zamenja
        if self.vnosi(x,y):
            self.fontiran_niz = self.font.render(self.niz, True, self.druga_barva)
        else:
            self.fontiran_niz = self.font.render(self.niz, True, self.barva)


