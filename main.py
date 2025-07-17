import pygame
import sys

from settings import *
from player import Player
from map import Map, load_tile_kinds
from camera import create_screen
from quest_manager import QuestManager

pygame.init()

#Setup
window = create_screen(WINDOW_WIDTH, WINDOW_HEIGHT, "rpg-quest-game")
tile_kinds = load_tile_kinds(TILE_DATA)
map = Map("maps/start.map", 'maps/object_layer.map', tile_kinds, TILE_SIZE, OBJECT_LIST)

def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(PLAYER_IMAGE, PLAYER_SPEED)
    player.x_cord = WINDOW_WIDTH//2
    player.y_cord = WINDOW_HEIGHT//2

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        #-----DRAW-----
        window.fill((0,0,0))
        map.draw(window, player)
        player.handle_movement(keys, map, map.objects_on_map)
        player.draw_hud(window)
        player.handle_interaction(map.objects_on_map, keys)
        player.inventory.draw(window)

        pygame.display.update()

if __name__ == "__main__":
    main()