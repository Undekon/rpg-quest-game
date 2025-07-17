import pygame
from settings import *
from camera import world_to_screen

class Interactable:
    def __init__(self, x, y, width, height):
        self.interact_icon = pygame.image.load("assets/icons/interaction_icon.png")
        self.interact_key = pygame.K_e
        self.interaction_area = pygame.Rect(x-TILE_SIZE, y-TILE_SIZE, width+(TILE_SIZE * 2), height+(TILE_SIZE * 2))
        self.x = x
        self.y = y
        self.show_icon = False
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def check_interaction(self, player_rect, keys):
        self.show_icon = self.interaction_area.colliderect(player_rect)
        if self.interaction_area.colliderect(player_rect) and keys[self.interact_key]:
            pygame.time.delay(200)
            return True
        return False

    def draw_interaction_elements(self, surface):
        screen_rect = pygame.Rect(
            world_to_screen((self.interaction_area.x, self.interaction_area.y)),
            (self.interaction_area.width, self.interaction_area.height)
        )

        #Debug area
        # pygame.draw.rect(surface, (255, 0, 0), screen_rect, 2)

        if self.show_icon:
            surface.blit(self.interact_icon, world_to_screen((self.x - 3, self.y - 35)))
    
    def interact(self):
        pass