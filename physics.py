import pygame

def check_collision(player, map):
    player_hitbox = pygame.Rect(player.x_cord, player.y_cord, player.width, player.height)

    for y, row in enumerate(map.tiles):
        for x, tile_id in enumerate(row):
            tile_kind = map.tile_kinds[tile_id]
            if tile_kind.is_solid:
                tile_rect = pygame.Rect(
                    x * map.tile_size,
                    y * map.tile_size,
                    map.tile_size,
                    map.tile_size
                )
                if player_hitbox.colliderect(tile_rect):
                    return True
    return False


