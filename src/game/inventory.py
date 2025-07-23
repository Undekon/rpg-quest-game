import pygame
from settings import *
from .card import Card

class Inventory:
    def __init__(self):
        self.visible = False  
        #ITEMS
        self.items = []      
        self.deck = []
        self.gold = 0

        #Eq panel setup
        self.panel_width = 1000
        self.panel_height = 800
        self.panel_x = (WINDOW_WIDTH - self.panel_width)//2
        self.panel_y = (WINDOW_HEIGHT - self.panel_height)//2
        self.font = pygame.font.SysFont(None, 24)
        self.max_cards_row = 5
        
        #Cards
        self.card_icon_width = CARD_ICON_WIDTH
        self.card_icon_height = CARD_ICON_HEIGT
        self.card_icon_margin = 20

        #Test cards
        self.test_card = [
            Card(0, "attack", "basic_attack", "assets/cards/attack_card.png", "Basic sword attack", 4, 4, 0, 0),
            Card(1, "attack","basic_defense", "assets/cards/shield_card.png", "Basic shield defense", 0, 4, 4, 0),
            Card(2, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
            Card(3, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
            Card(4, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
            Card(5, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
            Card(6, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
            Card(7, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0),
            Card(8, "attack","basic_defense", "assets/cards/heal_card.png", "Basic shield defense", 0, 4, 0, 0)
        ]
        for card in self.test_card:
            self.items.append(card)

    def add_item(self, new_item):
        self.items.append(new_item)

    def add_gold(self, ammount):
        self.gold += ammount
        print(f"[Inventory]: Gained {ammount} gold.")
  
    def toggle(self):
        self.visible = not self.visible
        print(f"[Inventory]: Cards: {[card.name for card in self.items]}")
        
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
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

        ##################################RIGHT SIDE - deck section
        #Draw deck
        deck_x = self.panel_x + self.panel_width - 300
        deck_y = self.panel_y + 50
        surface.blit(deck_title, (deck_x + 100, deck_y - 30))

        #Draw deck slots in 2 collumns
        for i in range(DECK_SLOTS//2):
            for j in range(2):
                deck_slot_x = deck_x + j * (self.card_icon_width + self.card_icon_margin + 20)
                deck_slot_y = deck_y + i * (self.card_icon_height + self.card_icon_margin)
                pygame.draw.rect(surface, (70,70,90), (deck_slot_x, deck_slot_y, self.card_icon_width, self.card_icon_height), 2)

        #Draw cards in deck
        if self.deck:
            for i, card in enumerate(self.deck):
                row = i//2
                col = i%2

                card_x = deck_x + col * (self.card_icon_width + self.card_icon_margin + 20)
                card_y = deck_y + row * (self.card_icon_height + self.card_icon_margin)
                surface.blit(card.icon, (card_x, card_y))

                # Check if card in deck is hovered
                card_rect = pygame.Rect(card_x, card_y, self.card_icon_width, self.card_icon_height)
                card.is_hovered = card_rect.collidepoint(mouse_pos)
                
                # Remove cards from deck
                if card.is_hovered:
                    pygame.draw.rect(surface, (200,70,70), (card_x, card_y, self.card_icon_width, self.card_icon_height), 3)
                    if pygame.mouse.get_pressed()[0]:
                        pygame.time.delay(100)
                        self.deck.remove(card)
                        self.items.append(card)


        ##################################LEFT SIDE - inventory section
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

            #Select cards to deck
            if card.is_hovered:
                pygame.draw.rect(surface, (70,70,150), (card_x, card_y, self.card_icon_width, self.card_icon_height), 3)
                if pygame.mouse.get_pressed()[0]:
                    if card not in self.deck and len(self.deck) <= DECK_SLOTS-1:
                        pygame.time.delay(100)
                        self.items.remove(card)
                        self.deck.append(card)

