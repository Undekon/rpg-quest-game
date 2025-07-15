import pygame
from camera import world_to_screen

class TileKind:
    def __init__(self, name, image, is_solid, id, type):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid
        self.id = id
        self.type = type

class Map:
    def __init__(self, map_file, tile_kinds, tile_size):
        self.tile_kinds = tile_kinds
        self.tile_size = tile_size

        #Load map file
        map_file = open(map_file, "r")
        map_data = map_file.read()
        map_file.close

        #Load objects file 
        # object_file = open(object_file, "r")
        # objects_data = object_file.read()
        # object_file.close()

        #Setup tiles from map data
        self.tiles = []
        for line in map_data.split("\n"):
            row = []
            for tile_number in line:
                row.append(int(tile_number))
            self.tiles.append(row)

        #Setup objects on map
        #----NPCS
        # self.objects = []
        # for line in objects_data.split("\n"):
        #     row = []
        #     for tile_number in line:
        #         #NPCS
        #         if tile_number >= 100 and tile_number < 200:
        #             row.append(int(tile_number))
        #         self.objects.append(row)
        

    def draw(self, surface):
        #Draw map
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size, y * self.tile_size)
                image = self.tile_kinds[tile].image
                surface.blit(image, world_to_screen(location))
        
        #Draw objects


def load_tile_kinds(tile_data):
    return [TileKind(tile["name"], tile['image'], tile['is_solid'], tile['id'], tile['type']) for tile in tile_data]