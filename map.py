import pygame
from camera import world_to_screen

class TileKind:
    def __init__(self, name, image, is_solid, id):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid
        self.id = id

class Map:
    def __init__(self, map_file, tile_kinds, tile_size):
        self.tile_kinds = tile_kinds
        self.tile_size = tile_size

        #Load map file
        file = open(map_file, "r")
        data = file.read()
        file.close

        #Setup tiles from map data
        self.tiles = []
        for line in data.split("\n"):
            row = []
            for tile_number in line:
                row.append(int(tile_number))
            self.tiles.append(row)

        #Setup objects on map
        #----NPCS
        

    def draw(self, surface):
        #Draw map
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size, y * self.tile_size)
                image = self.tile_kinds[tile].image
                surface.blit(image, world_to_screen(location))
        
        #Draw NPCs

def load_tile_kinds(tile_data):
    return [TileKind(tile["name"], tile['image'], tile['is_solid'], tile['id']) for tile in tile_data]