import pygame
import random

from src.game.camera import world_to_screen
from src.map.enviroment_objects import Chest, Tree
from src.entities.npc import NPC

class TileKind:
    def __init__(self, name, image, is_solid, id, type):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid
        self.id = id
        self.type = type

class Map:
    def __init__(self, map_file, object_layer_file, tile_kinds, tile_size, object_list):
        self.tile_kinds = tile_kinds
        self.tile_size = tile_size
        self.object_list = object_list
        
        #Load map file (background)
        try:
            with open(map_file, 'r') as file:
                map_data = file.read()
                print("[Map]: Successfully loaded map file!") #DEBUG
        except Exception as e:
            print(f"[Map]: Can't load map file: {e}") #Debug

        #Load objects layer file 
        try:
            with open(object_layer_file, 'r') as file:
                objects_data = file.read()
                print("[Map]: Successfully loaded objects layer map file!") #DEBUG
        except Exception as e:
            print(f"[Map]: Can't load object layer map file: {e}") #Debug

        #Setup tiles from map data
        self.tiles = []
        for line in map_data.split("\n"):
            row = []
            for tile_number in line.strip().split(","):
                if tile_number != "":
                    tile_number = int(tile_number)
                    #set random grass tiles
                    if tile_number == 0:
                        if random.random() < 0.015:
                            tile_number = 5
                        elif random.random() < 0.02:
                            tile_number = 6
                        else:
                            tile_number = 0
                    row.append(int(tile_number))
            self.tiles.append(row)

        #Setup objects on map
        self.objects_on_map = self.load_objects(objects_data)
        
    def load_objects(self, objects_data):
        objects_on_map = []

        for y, row in enumerate(objects_data.split("\n")):
            for x, object_number in enumerate(row.strip().split(",")):
                if object_number != "" and object_number != 0:
                    object_id = int(object_number)
                    if object_id in self.object_list:
                        curr_obj_data = self.object_list[object_id]
                        tile_x = x * self.tile_size
                        tile_y = y * self.tile_size
                        #CHESTS
                        if curr_obj_data['type'] == 'chest':
                            chest = Chest(curr_obj_data['data']['chest_id'],
                                        curr_obj_data['data']['image'],
                                        curr_obj_data['data']['type'],
                                        curr_obj_data['data']['content'],
                                        tile_x,
                                        y * self.tile_size)
                            objects_on_map.append(chest)
                        #NPCs
                        if curr_obj_data['type'] == "npc":
                            npc = NPC(curr_obj_data['data']['name'],
                                      curr_obj_data['data']['image'],
                                      curr_obj_data['data']["id"],
                                      curr_obj_data['data']['quest_id'],
                                      tile_x,
                                      tile_y)
                            objects_on_map.append(npc)
                        #TREES
                        if curr_obj_data['type'] == 'tree':
                            tree = Tree(curr_obj_data['data']['tree_id'],
                                        curr_obj_data['data']['image'],
                                        tile_x,
                                        tile_y)
                            objects_on_map.append(tree)
                        #ROCKS
        return objects_on_map
        

    def draw(self, surface, player):
        #Draw map
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                    location = (x * self.tile_size, y * self.tile_size)
                    image = self.tile_kinds[tile].image
                    surface.blit(image, world_to_screen(location))
        
        player.draw(surface)
        #Draw objects
        for obj in self.objects_on_map:
            if isinstance(obj, NPC):
                continue
            obj.draw(surface)
        
        #Draw npcs at the end
        for obj in self.objects_on_map:
            if isinstance(obj, NPC):
                obj.draw(surface)

def load_tile_kinds(tile_data):
    return [TileKind(tile["name"], 
                     tile['image'], 
                     tile['is_solid'], 
                     tile['id'], tile['type']) for tile in tile_data]