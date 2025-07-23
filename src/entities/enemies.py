import pygame
import random

from settings import *
from src.game.interactable import Interactable
from src.game.camera import world_to_screen
from src.game.card import Card


class Enemy(Interactable):
    def __init__(self, enemy_id, name, image, lvl, health, mana, x=0, y=0):
        super().__init__(x, y, 32, 32)
        self.id = enemy_id
        self.name = name
        self.image = pygame.image.load(image)
        
        self.is_alive = True
        self.is_solid = True
        #stats
        self.lvl = lvl
        self.health = health + (self.lvl - 1) * 10
        self.mana = mana
        self.deck = []
        self.create_deck()
    
    def draw(self, surface):
        font = pygame.font.SysFont(None, 24)
        
        surface.blit(self.image, world_to_screen((self.x, self.y)))
        self.draw_interaction_elements(surface)

        #Draw enemy lvl above the sprite
        lvl_text = font.render(f"{self.lvl}", True, (255,255,255))
        surface.blit(lvl_text, world_to_screen((self.x, self.y - 35)))

    def create_deck(self):
        #Creates random deck with 3 attack cards, 3 defense cards, 1 hp card, 1 mana card, 2 special cards
        selected_cards = []
        attack_cards = []
        defense_cards = []
        hp_cards = []
        mana_cards = []
        special_cards = []

        for card in CARD_DATA:
            if card['type'] == 'attack':
                attack_cards.append(card)
            elif card['type'] == 'defense':
                defense_cards.append(card)
            elif card['type'] == 'hp':
                hp_cards.append(card)
            elif card['type'] == 'mana':
                mana_cards.append(card)

        #Take random cards
        for _ in range(3):
            if attack_cards:
                selected_cards.append(random.choice(attack_cards))
            if defense_cards:
                selected_cards.append(random.choice(defense_cards))
        
        for _ in range(1):
            if hp_cards:
                selected_cards.append(random.choice(hp_cards))
            if mana_cards:
                selected_cards.append(random.choice(mana_cards))

        #Create cards objects in enemy deck
        if selected_cards:
            for card in selected_cards:
                card_obj = Card(
                                card["id"],
                                card['type'],
                                card['name'],
                                card['image'],
                                card['description'],
                                card['dmg'],
                                card['mana'],
                                card['defense'],
                                card['heal']
                )
                self.deck.append(card_obj) 
                
    def interact(self):
        #Interaction with enemy will start combat minigame player vs enemy
        print(f'[Enemy]: Interaction with {self.name}. Combat starts. Enemy deck: {[card.name for card in self.deck]}') #DEBUG

