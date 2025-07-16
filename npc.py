import pygame
from interactable import Interactable

from camera import world_to_screen

class NPC(Interactable):
    def __init__(self, name, image, npc_id, quest_id, x=0, y=0):
        self.image = pygame.image.load(image)
        self.name = name
        self.npc_id = npc_id
        self.quest_id = quest_id

        self.is_solid = True
        super().__init__(x, y, 32,32)
        
    def draw(self, surface):
        surface.blit(self.image, world_to_screen((self.x, self.y)))

        #### DEBUG
        self.draw_interaction_elements(surface)

    def interact(self):
        print(f"Interaction with: {self.name}")

    def load_quest():
        pass


