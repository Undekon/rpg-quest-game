import pygame
from src.game.interactable import Interactable
from src.game.camera import world_to_screen
from settings import TILE_SIZE

class Chest(Interactable):
    def __init__(self, chest_id, image, type, content, x=0, y=0):
        self.image = pygame.image.load(image)
        self.id = chest_id
        self.type = type
        self.content = content
        self.is_solid = True
        self.x_cord = x
        self.y_cord = y
        super().__init__(x,y, 32, 32)

        #Content panel
        self.visible_panel = False
        self.panel_width = 300
        self.panel_height = 150
        screen_x, screen_y = world_to_screen((self.x_cord, self.y_cord)) 
        self.panel_x = screen_x - self.panel_width //2 + self.image.get_width() //2
        self.panel_y = screen_y - self.panel_height - 40

    def interact(self):
        self.toggle_panel()
        print(f"[Chest]: Interaction with chest: {self.id}, content: {self.content}")

    def draw(self, surface):
            surface.blit(self.image, world_to_screen((self.x, self.y)))
            self.draw_interaction_elements(surface)

            #Draw GUI
            if self.visible_panel:
                 pygame.draw.rect(surface, (50, 50, 70), (self.panel_x, self.panel_y, self.panel_width, self.panel_height))
                 pygame.draw.rect(surface, (100, 100, 120), (self.panel_x, self.panel_y, self.panel_width, self.panel_height), 2)

    def toggle_panel(self):
         self.visible_panel = not self.visible_panel

    def take_items(self):
        temp_content = self.content
        self.content.clear()
        return temp_content

class Doors(Interactable):
     pass

class Tree:
    def __init__(self, tree_id, image, x = 0, y = 0):
        self.image = pygame.image.load(image)
        self.id = tree_id
        self.is_solid = True
        self.x_cord = x - 16
        self.y_cord = y - (96-32)
        self.width = 64
        self.height = 96

        hitbox_width = TILE_SIZE//2
        hitbox_height = TILE_SIZE
        self.rect = pygame.Rect(x + 8, y, hitbox_width, hitbox_height)

    def draw(self, surface):
        surface.blit(self.image, world_to_screen((self.x_cord, self.y_cord)))
        
        # DEBUG 
        pygame.draw.rect(surface, (255, 0, 0), 
                         pygame.Rect(world_to_screen((self.rect.x, self.rect.y)), 
                         (self.rect.width, self.rect.height)), 1)

class Rock:
     pass
