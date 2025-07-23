import pygame
import sys
from settings import *

class CombatSystem:
    def __init__(self, player, enemy):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #Initialize player and enemy
        self.player = player
        self.enemy = enemy

    
    def run_combat(self):
        run = True

        while run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()