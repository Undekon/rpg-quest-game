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

    def draw(self, surface, position):
        surface.blit(self.image, position)

def load_card_data(cards_data_file):
    try:
        with open(cards_data_file, 'r') as file:
            cards_data = json.load(file)
        print("[Cards]: Successfully loaded cards data!")
        return cards_data
    except Exception as e:
        print(f"[Cards]: Can't load cards data file: {e}")



