import pygame

from src.game.interactable import Interactable
from src.game.camera import world_to_screen
from settings import TILE_SIZE
from src.game.button import Button
from settings import *
from src.game.card import Card

class Chest(Interactable):
    def __init__(self, chest_id, image, type, content, x=0, y=0):
        self.image = pygame.image.load(image)
        self.id = chest_id
        self.type = type
        self.content = content
        self.content_cards = self.create_cards()
        self.is_solid = True
        self.x_cord = x
        self.y_cord = y
        super().__init__(x,y, 32, 32)
        self.interacting_player = None

        #Content panel
        self.visible_panel = False
        self.panel_width = 300
        self.panel_height = 200
        screen_x, screen_y = world_to_screen((self.x_cord, self.y_cord)) 
        self.panel_x = screen_x - self.panel_width //2 + self.image.get_width() //2
        self.panel_y = screen_y - self.panel_height - 40

        #Buttons
        self.button_width = 100
        self.button_height = 40
        self.take_button = Button(0,0, self.button_width, self.button_height, "Take", self.take_items)
        self.close_button = Button(0,0, self.button_width, self.button_height, "Close", self.close)

    def create_cards(self):
        #Create cards objects in chest
        cards = []
        for item in self.content:
            for card in CARD_DATA:
                if item['card_id'] == card['id']:
                    card_data = card
                    temp_card = Card(
                                card_data["id"],
                                card_data['name'],
                                card_data['image'],
                                card_data['description'],
                                card_data['dmg'],
                                card_data['mana'],
                                card_data['defense'],
                                card_data['heal']
                            ) 
                    cards.append(temp_card)
        return cards

    def interact(self, player):
        #Show chest panel when player interacts
        self.interacting_player = player
        self.toggle_panel()
        print(f"[Chest]: Interaction with chest: {self.id}, content: {self.content}") #DEBUG

    def draw(self, surface):
            surface.blit(self.image, world_to_screen((self.x, self.y)))
            self.draw_interaction_elements(surface)

            #Draw GUI
            if self.visible_panel:
                pygame.draw.rect(surface, (50, 50, 70), (self.panel_x, self.panel_y, self.panel_width, self.panel_height))
                pygame.draw.rect(surface, (100, 100, 120), (self.panel_x, self.panel_y, self.panel_width, self.panel_height), 2)

                #Draw buttons
                self.take_button.rect.topleft = (self.panel_x + 20, self.panel_y + self.panel_height - 50)
                self.close_button.rect.topleft = (self.panel_x + self.panel_width - 120, self.panel_y + self.panel_height - 50)
                self.take_button.draw(surface)
                self.close_button.draw(surface)

                mouse_pos = pygame.mouse.get_pos()
                self.take_button.update(mouse_pos)
                self.close_button.update(mouse_pos)

                #Draw cards icons
                icon_start_x = self.panel_x + 20
                icon_start_y = self.panel_y + 50
                icon_margin = 20
                for i, card in enumerate(self.content_cards):
                    icon_x = icon_start_x + i * (CARD_ICON_WIDTH + icon_margin)
                    icon_y = icon_start_y
                    surface.blit(card.icon, (icon_x, icon_y))

                    card_rect = pygame.Rect(icon_x, icon_y, CARD_ICON_WIDTH, CARD_ICON_HEIGT)
                    card.is_hovered = card_rect.collidepoint(mouse_pos)
                    if card.is_hovered:
                        card.draw_hover_desc(surface, icon_x, icon_y)

    def toggle_panel(self):
         self.visible_panel = not self.visible_panel

    def take_items(self):
        if self.interacting_player and self.content:
            for item in self.content_cards:
                self.interacting_player.inventory.add_item(item)
            self.content = []
            self.close()
    
    def close(self):
        self.visible_panel = False
        self.interacting_player = None

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
