import pygame
from settings import *
from .card import Card

class Inventory:
    def __init__(self, gold, exp):
        self.visible = False  
        #ITEMS
        self.items = []      
        self.deck = []
        self.gold = gold
        self.exp = exp

        #Eq panel setup
        self.panel_width = 600
        self.panel_height = 400
        self.panel_x = (WINDOW_WIDTH - self.panel_width)//2
        self.panel_y = (WINDOW_HEIGHT - self.panel_height)//2
        self.font = pygame.font.SysFont(None, 24)
        self.max_cards_row = 5
        
        #Cards
        self.card_icon_width = CARD_ICON_WIDTH
        self.card_icon_height = CARD_ICON_HEIGT
        self.card_icon_margin = 20

        #Test cards
        # self.test_card = [
        #     Card(0, "basic_attack", "assets/cards/attack_card.png", "Basic sword attack", 4, 4, 0, 0),
        #     Card(1, "basic_defense", "assets/cards/defense_card.png", "Basic shield defense", 0, 4, 4, 0),
        #     Card(2, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
        #     Card(3, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
        #     Card(4, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
        #     Card(5, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
        #     Card(6, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
        #     Card(7, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
        #     Card(8, "basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0)
        # ]
        # for card in self.test_card:
        #     self.items.append(card)

    def add_item(self, new_item):
        # card_data = None
        # for card in CARD_DATA:
        #     if new_item["card_id"] == card['id']:
        #         card_data = card
        #         new_card = Card(
        #             card_data["id"],
        #             card_data['name'],
        #             card_data['image'],
        #             card_data['description'],
        #             card_data['dmg'],
        #             card_data['mana'],
        #             card_data['defense'],
        #             card_data['heal']
        #         ) 
        self.items.append(new_item)
        # print(f"[Inventory]: Added {new_card} to player inventory.")

    def add_deck_card(self, card, max_cards):
        pass
        
    def toggle(self):
        self.visible = not self.visible
        print(f"[Inventory]: Cards: {self.items}")
        
    def draw(self, surface):
        if self.visible == False:
            return

        #Draw inventory panel
        background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        background.fill((0,0,0, 180))
        surface.blit(background, (0,0))

        #Titles
        eq_title = self.font.render("Equipment", True, (255,255,255))
        deck_title = self.font.render("Deck", True, (255,255,255))
        gold_text = self.font.render(f"Gold: {self.gold}", True, (255,255,255))

        pygame.draw.rect(surface, (50,50,70), (self.panel_x, self.panel_y, self.panel_width, self.panel_height))
        pygame.draw.rect(surface, (100,100,120), (self.panel_x, self.panel_y, self.panel_width, self.panel_height), 3)
        
        surface.blit(eq_title, (self.panel_x + 10, self.panel_y + 10))
        surface.blit(gold_text, (self.panel_x + 150, self.panel_y + 10))

        #RIGHT SIDE - deck section
        #Draw deck
        deck_x = self.panel_x + self.panel_width - 100
        deck_y = self.panel_y + 50
        surface.blit(deck_title, (deck_x- 20, deck_y - 30))

        for i in range(DECK_SLOTS):
            slot_x = deck_x - 20
            slot_y = deck_y + i * (self.card_icon_width + self.card_icon_margin)

            pygame.draw.rect(surface, (70,70,90), (slot_x, slot_y, self.card_icon_width, self.card_icon_height), 2)
        
        mouse_pos = pygame.mouse.get_pos()
        #LEFT SIDE - inventory section
        cards_start_x = self.panel_x + 20
        cards_start_y = self.panel_y + 50
        cards_per_row = self.max_cards_row
        
        for i, card in enumerate(self.items):
            row = i // cards_per_row 
            col = i % cards_per_row   
            
            card_x = cards_start_x + col * (self.card_icon_width + self.card_icon_margin)
            card_y = cards_start_y + row * (self.card_icon_height + self.card_icon_margin)
            
            surface.blit(card.icon, (card_x, card_y))
            #Draw slot frame
            pygame.draw.rect(surface, (100,100,120), (card_x, card_y, self.card_icon_width, self.card_icon_height), 1)

            #Draw card description
            card_rect = pygame.Rect(card_x, card_y, self.card_icon_width, self.card_icon_height)
            card.is_hovered = card_rect.collidepoint(mouse_pos)
            if card.is_hovered:
                card.draw_hover_desc(surface, card_x, card_y)
