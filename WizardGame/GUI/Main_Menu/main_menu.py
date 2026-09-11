import pygame
import sys
sys.path.append('.')
from GUI.buttons import Button
from Engine.Game import game
from Engine.Game import keyboard



def get_font(size, oddebeljeno): # Dobiš nazaj željeno velikost fonta
    return pygame.font.SysFont('papyrus', size, bold=oddebeljeno)



def main_menu(x,y):
    
    screen = pygame.display.set_mode((x,y))
    screen.fill('black')
    pygame.display.set_caption('WizardGame')

    
    while True:
        
        screen.fill("black")

        pozicija_miske = pygame.mouse.get_pos()
        menu_besedilo = get_font(100, True).render('MAIN  MENU', True, "#0324AA")
        menu_rect = menu_besedilo.get_rect(center=(x/2, (y/2 - (y/2)/2)))


        play = Button(slika=pygame.image.load(r'GUI\Main_Menu\Play Rect.png'), x= x/2, y= y/2, niz= 'PLAY',
                       font= get_font(80, False), barva="#294BD3", druga_barva="#BCE80C" )
      
        
        options = Button(slika=pygame.image.load(r'GUI\Main_Menu\Options Rect.png'), x= x/2, y= (y/2 + y/6), niz= 'OPTIONS',
                       font= get_font(80, False), barva="#294BD3", druga_barva="#BCE80C" )
        
        quit = Button(slika=pygame.image.load(r'GUI\Main_Menu\Play Rect.png'), x= x/2, y= (y/2 + y/3), niz= 'QUIT',
                       font= get_font(80, False), barva="#294BD3", druga_barva="#BCE80C" )
        
        screen.blit(menu_besedilo,menu_rect)        #Tole gor naredi tipke ki se izričejo v MAIN MENU zaslonu, so pa iz button fila

        for button in [play, options, quit]:
            button.spremeni_barvo(*pozicija_miske)      #to gre čez vse tipke in preveri če je pozicija miške na njim, če je pa barvo sprmeni
            button.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

            elif event.type == pygame.KEYDOWN:
                keyboard.keys.add(event.key)

                if event.key == pygame.K_ESCAPE:
                    return 'play'
                                                                        #To je pa zadolženo da se zasloni prav irišejo oz. pravilno funkcijo/metodo pokliče
            elif event.type == pygame.KEYUP:
                if event.key in keyboard.keys:
                    keyboard.keys.remove(event.key)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.vnosi(*pozicija_miske):
                    return 'play'
                
                if options.vnosi(*pozicija_miske):  #Za zdej nimam še nič dodano za opcije, pač knof je tam
                    pass

                if quit.vnosi(*pozicija_miske):
                    return 'quit'
    
        pygame.display.update()






