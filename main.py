import pygame
import sys

from settings import *
from player import Player
from map import Map, load_tile_kinds
from camera import create_screen
from npc import load_npcs

#Setup
window = create_screen(WINDOW_WIDTH, WINDOW_HEIGHT, "rpg-quest-game")
tile_kinds = load_tile_kinds(TILE_DATA)
map = Map("maps/start.map", tile_kinds, TILE_SIZE)
npcs = load_npcs(NPC_DATA)

def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(PLAYER_IMAGE, PLAYER_SPEED)
    player.x_cord = WINDOW_WIDTH//2
    player.y_cord = WINDOW_HEIGHT//2
    interactables = []

    for npc in npcs:
        interactables.append(npc)
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        #-----DRAW-----
        window.fill((0,0,0))
        map.draw(window)
        player.handle_movement(keys, map)
        player.draw(window)
        player.draw_hud(window)
        for npc in interactables:
            npc.draw(window)
        player.handle_interaction(interactables, keys)

        pygame.display.update()

if __name__ == "__main__":
    main()