import pygame

from camera import *
from settings import MAP_HEIGHT, MAP_WIDTH, TILE_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from physics import check_collision, check_collisions_with_objects

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

        self.hitbox = 0 

        #Stats
        self.health = 100
        self.stamina = 100
        self.mana = 100

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
    
    def draw(self, surface):
        if self.direction == 0:
            self.image = self.org_image
        if self.direction == 1:
            self.image = pygame.transform.flip(self.org_image, True, False)

        
        surface.blit(self.image, world_to_screen((self.x_cord, self.y_cord)))

    def draw_hud(self, surface):
        bar_width = 100
        bar_height = 10

        #HP
        pygame.draw.rect(surface, (50,50,50), (WINDOW_WIDTH-200, WINDOW_HEIGHT-200, bar_width, bar_height))
        pygame.draw.rect(surface, (255, 70, 76), (WINDOW_WIDTH-200, WINDOW_HEIGHT-200, self.health, bar_height))

        #STAMINA
        pygame.draw.rect(surface, (50,50,50), (WINDOW_WIDTH-200, WINDOW_HEIGHT-185, bar_width, bar_height))
        pygame.draw.rect(surface, (255, 255, 0), (WINDOW_WIDTH-200, WINDOW_HEIGHT-185, self.stamina, bar_height))

        #MANA
        pygame.draw.rect(surface, (50,50,50), (WINDOW_WIDTH-200, WINDOW_HEIGHT-170, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 0, 255), (WINDOW_WIDTH-200, WINDOW_HEIGHT-170, self.mana, bar_height))

    def take_dmg(self, dmg_value):
        self.health -= dmg_value

    def handle_interaction(self, interactables, keys):
        for object in interactables:
            if object.check_interaction(self.player_rect, keys):
                object.interact()
                break


    
