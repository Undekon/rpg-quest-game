import pygame
from settings import *

class Inventory:
    def __init__(self):
        self.visible = False  
        self.items = []      
        self.deck = []

        self.panel_width = 600
        self.panel_height = 400
        self.panel_x = (WINDOW_WIDTH - self.panel_width)//2
        self.panel_y = (WINDOW_HEIGHT - self.panel_height)//2
        
    def toggle(self):
        self.visible = not self.visible
        
    def draw(self, surface):
        if self.visible == False:
            return

        #Draw inventory panel
        background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        background.fill((0,0,0, 180))
        surface.blit(background, (0,0))

        pygame.draw.rect(surface, (50,50,70), (self.panel_x, self.panel_y, self.panel_width, self.panel_height))
        pygame.draw.rect(surface, (100,100,120), (self.panel_x, self.panel_y, self.panel_width, self.panel_height), 3)
        
        
