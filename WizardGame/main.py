import pygame
import math
from Entities.entities import entities
from Engine.Game import game


def main():

    pygame.init()

    clock = pygame.time.Clock()

    neki = game.GameMap(r'World\mapa.tmx')

    neki.player.začetek()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        #if (keys[pygame.K_a] and keys[pygame.K_s]):
            #neki.player.move(-(neki.player.move_speed//2),neki.player.move_speed//2)          #Ko se premikam v dve smeri hkrati gre player mal hitreje
        temp_x = neki.player.x + neki.player.move_speed
        temp_y = neki.player.y + neki.player.move_speed

        if neki.can_move(temp_x,temp_y):
            if keys[pygame.K_w]:
                neki.player.move(0, -neki.player.move_speed)
            if keys[pygame.K_s]:
                neki.player.move(0, neki.player.move_speed)
            if keys[pygame.K_a]:
                neki.player.move(-neki.player.move_speed, 0)
            if keys[pygame.K_d]:
                neki.player.move(neki.player.move_speed, 0)

        #print((neki.player.x,neki.player.y))             #Tako sem prišel do spawn pointa

        neki.zaslon.fill((30, 30, 30))

        neki.draw()
        for e in entities:
            e.draw_sprite(neki.zaslon)


        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()







if __name__ == "__main__":
    main()
