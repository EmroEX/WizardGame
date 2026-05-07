import pytmx  #pip install pytmx
import pygame #pip install pygame

from pytmx.util_pygame import load_pygame

pygame.init()

WIDTH = 1280
HEIGHT = 780

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Isometric TMX Test")

clock = pygame.time.Clock()

tmx_data = load_pygame("test.tmx")

tile_w = tmx_data.tilewidth
tile_h = tmx_data.tileheight

map_w = tmx_data.width
map_h = tmx_data.height

# center map
offset_x = WIDTH // 2
offset_y = HEIGHT //2


def iso_to_screen(x, y):
    screen_x = (x - y) * (tile_w // 2)
    screen_y = (x + y) * (tile_h // 2)
    return screen_x + offset_x, screen_y + offset_y


def draw_map(surface):

    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):

            for x, y, gid in layer:

                tile = tmx_data.get_tile_image_by_gid(gid)

                if tile:

                    screen_x, screen_y = iso_to_screen(x, y)

                    surface.blit(tile, (screen_x, screen_y))


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 15, 40))

    draw_map(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()