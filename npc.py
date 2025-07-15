import pygame
from interactable import Interactable

from camera import world_to_screen

class NPC(Interactable):
    def __init__(self, name, image, x, y, npc_id, quest_id):
        super().__init__(x,y,32,32)
        self.image = pygame.image.load(image)
        self.name = name
        self.npc_id = npc_id
        self.quest_id = quest_id
        self.x_cord = x
        self.y_cord = y

    def draw(self, surface):
        surface.blit(self.image, world_to_screen((self.x_cord, self.y_cord)))

        #### DEBUG
        self.draw_interaction_elements(surface)

    def interact(self):
        print(f"Interaction with: {self.name}")
            

    def load_quest():
        pass

def load_npcs(npcs_data):
    return [NPC(npc['name'], npc['image'], npc['x'], npc['y'], npc['id'], npc['quest_id'] )for npc in npcs_data]

