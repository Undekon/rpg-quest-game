import pygame

from src.game.camera import *
from settings import MAP_HEIGHT, MAP_WIDTH, TILE_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from src.game.physics import check_collision, check_collisions_with_objects
from src.game.interactable import Interactable
from src.game.inventory import Inventory
from src.map.enviroment_objects import Chest

class Player:
    def __init__(self, image, speed):
        self.org_image = pygame.image.load(image)
        self.image = self.org_image
        self.width = self.org_image.get_width()
        self.height = self.org_image.get_height()
        self.x_cord = 0
        self.y_cord = 0
        self.speed = speed
        self.direction = 0 #0 - right, 1 - left
        self.player_rect = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

        #Stats
        self.health = 100
        self.stamina = 100
        self.mana = 100
        self.exp = 0
        self.gold = 10

        self.inventory = Inventory(self.gold, self.exp)

        #Quests
        self.active_quests = []
        self.max_active_quests = 5

    def handle_movement(self, keys, map, collision_objects):
        old_x = self.x_cord
        old_y = self.y_cord

        #update player rect
        self.player_rect.x = self.x_cord
        self.player_rect.y = self.y_cord

        #Running
        if keys[pygame.K_LSHIFT] and self.stamina > 0:
            speed = self.speed * 2
            self.stamina -= 1
        else:
            speed = self.speed
            if self.stamina < 100:
                self.stamina += 0.5

        if keys[pygame.K_w]:
            self.y_cord -= speed
        if keys[pygame.K_s]:
            self.y_cord += speed
        if keys[pygame.K_a]:
            self.x_cord -= speed
            self.direction = 1
        if keys[pygame.K_d]:
            self.x_cord += speed
            self.direction = 0

        #check for collisions
        if check_collision(self, map) or check_collisions_with_objects(self, collision_objects):
            self.x_cord = old_x
            self.y_cord = old_y

        #Player map movement limits
        self.x_cord = max(0, min(self.x_cord, MAP_WIDTH * TILE_SIZE - self.org_image.get_width()))
        self.y_cord = max(0, min(self.y_cord, MAP_HEIGHT * TILE_SIZE - self.org_image.get_height()))

        #update camera
        update_camera(self, MAP_WIDTH, MAP_HEIGHT, TILE_SIZE)

        #Show inventory
        if keys[pygame.K_i]:
            self.inventory.toggle()
            pygame.time.delay(200)
    
    def draw(self, surface):
        if self.direction == 0:
            self.image = self.org_image
        if self.direction == 1:
            self.image = pygame.transform.flip(self.org_image, True, False)

        surface.blit(self.image, world_to_screen((self.x_cord, self.y_cord)))

    def draw_hud(self, surface):
        bar_width = 100
        bar_height = 10

        hud_panel_width = 150
        hud_panel_height = 60
        hud_x = 0
        hud_y = WINDOW_HEIGHT - hud_panel_height

        pygame.draw.rect(surface, (50,50,70), (hud_x, hud_y, hud_panel_width, hud_panel_height))
        pygame.draw.rect(surface, (100,100,120), (hud_x, hud_y, hud_panel_width, hud_panel_height), 2)
        #HP
        pygame.draw.rect(surface, (50,50,50), (hud_x + 10, hud_y + 10, bar_width, bar_height))
        pygame.draw.rect(surface, (255, 70, 76), (hud_x + 10, hud_y + 10, self.health, bar_height))

        #STAMINA
        pygame.draw.rect(surface, (50,50,50), (hud_x + 10, hud_y + 25, bar_width, bar_height))
        pygame.draw.rect(surface, (255, 255, 0), (hud_x + 10, hud_y + 25, self.stamina, bar_height))

        #MANA
        pygame.draw.rect(surface, (50,50,50), (hud_x + 10, hud_y + 40, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 0, 255), (hud_x + 10, hud_y + 40, self.mana, bar_height))

        #DRAW ACTIVE QUESTS
        font = pygame.font.SysFont(None, 24)
        quests_title = font.render("Active Quests:", True, (255,255,255))
        if self.active_quests:
            surface.blit(quests_title, (50, 50))

            for i, quest in enumerate(self.active_quests):
                quest_text = font.render(f"- {quest['description']}", True, (255,255,255))
                surface.blit(quest_text, (50, 80 + i * 30))

    def take_dmg(self, dmg_value):
        self.health -= dmg_value

    def handle_interaction(self, interactables, keys):
        for object in interactables:
            if isinstance(object, Interactable):
                if object.check_interaction(self.player_rect, keys):
                    if isinstance(object, Chest):
                        object.interact(self)
                    else:
                        object.interact()

    #Handle quests
    def add_quest(self, quest_data):
        if quest_data not in self.active_quests:
            self.active_quests.append(quest_data)
            print(f"[PlayerQuests]: Added new quest: {quest_data['id'], quest_data['description']}")
            print(f"[Player]: Active quests: {self.active_quests}")