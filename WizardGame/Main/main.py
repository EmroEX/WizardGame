import pygame
import sys

sys.path.append('Engine/Game')
import game

pygame.init()

clock = pygame.time.Clock()

neki=game.GameMap('test.tmx')



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False


    if keys[pygame.K_w]:
        neki.player_y -= 1
    if keys[pygame.K_s]:
            neki.player_y += 1
    if keys[pygame.K_a]:
        neki.player_x -= 1
    if keys[pygame.K_d]:
        neki.player_x += 1

    neki.zaslon.fill((30, 30, 30))

    neki.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


"""
entities = [player, npc, animal]

for e in entities:
    e.update()
    e.draw(screen)
"""