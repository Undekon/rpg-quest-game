import pygame

camera = pygame.Rect(0,0,0,0)

def create_screen(width, height, title):
    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width, height))
    camera.width = width
    camera.height = height
    camera.x = 0
    camera.y = 0

    return screen

def update_camera(target, map_width, map_height, tile_size):
    camera.x = target.x_cord - camera.width//2
    camera.y = target.y_cord - camera.height//2

    block_camera(map_width, map_height, tile_size)

def world_to_screen(position):
    return (position[0]) - camera.x, position[1] - camera.y

def block_camera(map_width, map_height, tile_size):
    max_x = map_width * tile_size - camera.width
    max_y = map_height * tile_size - camera.height

    camera.x = max(0, min(camera.x, max_x))
    camera.y = max(0, min(camera.y, max_y))
