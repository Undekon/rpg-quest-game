import pygame
from interactable import Interactable
from camera import world_to_screen
from settings import TILE_SIZE

class Chest(Interactable):
    def __init__(self, chest_id, image, type, content, x=0, y=0):
        self.image = pygame.image.load(image)
        self.id = chest_id
        self.type = type
        self.content = content
        self.is_solid = True

        super().__init__(x,y, 32, 32)

    def interact(self):
        print(f"Interaction with chest: {self.id}, content: {self.content}")

    def draw(self, surface):
            surface.blit(self.image, world_to_screen((self.x, self.y)))

            #### DEBUG
            self.draw_interaction_elements(surface)

class Doors(Interactable):
     pass

class Tree:
    def __init__(self, tree_id, image, x = 0, y = 0):
        self.image = pygame.image.load(image)
        self.id = tree_id
        self.is_solid = True
        self.x_cord = x
        self.y_cord = y - (96-32)
        self.width = 64
        self.height = 96

        hitbox_width = TILE_SIZE
        hitbox_height = TILE_SIZE
        self.rect = pygame.Rect(x + (self.width - hitbox_width)//2,
                                y , 
                                hitbox_width, hitbox_height)

    def draw(self, surface):
        surface.blit(self.image, world_to_screen((self.x_cord, self.y_cord)))
        
        # DEBUG 
        pygame.draw.rect(surface, (255, 0, 0), 
                         pygame.Rect(world_to_screen((self.rect.x, self.rect.y)), 
                         (self.rect.width, self.rect.height)), 1)
class Rock:
     pass
