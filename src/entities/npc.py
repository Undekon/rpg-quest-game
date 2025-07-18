import pygame
import json
from src.game.button import Button

from src.game.interactable import Interactable
from src.game.camera import world_to_screen
from src.game.quest_manager import QuestManager 

global player_reference

def set_player(player):
    global player_reference
    player_reference = player

class NPC(Interactable):
    def __init__(self, name, image, npc_id, quest_id, x=0, y=0):
        global player_reference
        self.image = pygame.image.load(image)
        self.name = name
        self.x_cord = x
        self.y_cord = y
        self.npc_id = npc_id
        self.is_solid = True
        self.is_completed = False
        self.quest_manager = QuestManager("data/quests.json")
        super().__init__(x, y, 32,32)
        #Quest
        self.quest_id = quest_id
        self.quest_data = self.quest_manager.get_quest(self.quest_id)

        #Dialogue panel
        self.visible_dialogue = False
        button_width = 100
        button_height = 40
        self.accept_button = Button(0,0, button_width, button_height, "Accept", self.accept_quest)
        self.decline_button = Button(0,0, button_width, button_height, "Decline", self.decline_quest)
        
    def draw(self, surface):
        surface.blit(self.image, world_to_screen((self.x, self.y)))
        self.draw_interaction_elements(surface)

        #Draw dialogue panel
        if self.visible_dialogue:
            panel_width = 300
            panel_height = 150
            screen_x, screen_y = world_to_screen((self.x_cord, self.y_cord))
            panel_x = screen_x - panel_width // 2 + self.image.get_width() // 2  
            panel_y = screen_y - panel_height - 40  

            pygame.draw.rect(surface, (50,50,70), (panel_x, panel_y, panel_width, panel_height))
            pygame.draw.rect(surface, (100,100,120), (panel_x, panel_y, panel_width, panel_height), 3)

            font = pygame.font.SysFont(None, 24)
            text_name = font.render(self.name, True, (255, 255, 255))
            text_greeting = font.render(self.quest_data['greeting'], True, (255, 255, 255))
            text_quest_description = font.render(self.quest_data['description'], True, (255, 255, 255))
            # text_quest_reward = font.render(self.quest_data['reward'], True, (255, 255, 255))

            surface.blit(text_name, (panel_x + 10, panel_y + 10))
            surface.blit(text_greeting, (panel_x + 10, panel_y + 44))
            surface.blit(text_quest_description, (panel_x + 10, panel_y + 78))
            # surface.blit(text_quest_reward, (panel_x + 10, panel_y + 112))

            #Buttons
            self.accept_button.rect.topleft = (panel_x + 20, panel_y + panel_height - 50)
            self.decline_button.rect.topleft = (panel_x + panel_width - 120, panel_y + panel_height - 50)

            #---update buttons
            mouse_pos = pygame.mouse.get_pos()
            self.accept_button.update(mouse_pos)
            self.decline_button.update(mouse_pos)

            self.accept_button.draw(surface)
            self.decline_button.draw(surface)

            #Handle clicks
            if pygame.mouse.get_pressed()[0]:
                if self.accept_button.is_hovered:
                    self.accept_button.action()
                elif self.decline_button.is_hovered:
                    self.decline_button.action()

    ###########Interaction and quests
    def accept_quest(self):
        self.quest_manager.accept_quest(self.quest_id)
        self.active_quest = True

        player_reference.add_quest(self.quest_data)
        
        self.visible_dialogue = False


    def decline_quest(self):
        self.visible_dialogue = False

    def interact(self):
        if not self.is_completed:
            self.toggle_dialogue()
            print(f"[NPC] Interaction with: {self.name}")
            # print(f"NPC {self.npc_id} quest data: {self.quest_data}")
        else:
            print("[NPC] Quest completed")

    def toggle_dialogue(self):
        self.visible_dialogue = not self.visible_dialogue
            

        




