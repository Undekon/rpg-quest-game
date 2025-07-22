import pygame
import json

class Card:
    def __init__(self, card_id, name, image, description, dmg, mana, defense, heal):

        self.id = card_id
        self.name = name
        self.image = pygame.image.load(image)
        self.icon = pygame.transform.scale(self.image, (self.image.get_width() + 16, self.image.get_height() + 16))
        self.description = description
        self.dmg = dmg
        self.mana = mana
        self.defense = defense
        self.heal = heal

        self.is_hovered = False

    def draw(self, surface, position):
        surface.blit(self.image, position)

    def draw_hover_desc(self, surface, card_x, card_y):
        desc_panel = pygame.Surface((200,100), pygame.SRCALPHA)
        desc_panel.fill((50,50,50,200))
        desc_x = card_x
        desc_y = card_y - 110
        surface.blit(desc_panel, (desc_x, desc_y))

        font = pygame.font.SysFont(None, 24)
        lines = [self.name, 
                self.description,
                f"DMG: {self.dmg} | MANA: {self.mana}",
                f"DEF: {self.defense} | HEAL: {self.heal}"]
        for i, lane in enumerate(lines):
            text = font.render(lane, True, (255,255,255))
            surface.blit(text, (desc_x+10, desc_y+10+i*25))
        

def load_card_data(cards_data_file):
    try:
        with open(cards_data_file, 'r') as file:
            cards_data = json.load(file)
        print("[Cards]: Successfully loaded cards data!")
        return cards_data
    except Exception as e:
        print(f"[Cards]: Can't load cards data file: {e}")