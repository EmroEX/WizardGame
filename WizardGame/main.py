import pygame
from sys import exit
from Entities.entities import entities
from Engine.Game import game
from Engine.Game import keyboard
from GUI.Main_Menu import main_menu


def main():
    
    pygame.init()


    informacije_zaslona = pygame.display.Info()
    # Dobimo velikost monitorja oz. zaslona, in z priv. spremenljivko onemogočimo slučajno spreminjanje
    width, height = informacije_zaslona.current_w, informacije_zaslona.current_h
    zaslon = pygame.display.set_mode((width,height))
    #zaslon= pygame.display.set_mode((width,height), pygame.FULLSCREEN)  - na ta način loh FULLSCREEN nastavimo, loh pa pač samo od podanega kuk je zaslon velik
    
    zaslon.fill('black')

    while True:
        keyboard.keys.clear()      #Tole se mora sproti čistiti ker drugač se bo npr ESC v nedolged ponavlju ko gremo iz enega fila v drugi
        result = main_menu.main_menu(width, height)         #Pa to sem si mogu pomagati z AI ker nisem mogel ugotoviti kje je napaka pač sem mislu da je problem v klicih ampak je blo, da se ni keys spraznu

        
        if result == 'play':
            
            keyboard.keys.clear()
            print("Starting game")
            result = game.game()


        elif result == 'menu':
            continue

        elif result == 'quit':
            break
            
    pygame.quit()
    exit()
        
    
if __name__ == "__main__":
    main()
