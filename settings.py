#WINDOW SETTINGS
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

#GAME
FPS = 60

#PLAYER
PLAYER_SPEED = 3
PLAYER_IMAGE = "assets/sprites/player.png"

#TILES
TILE_SIZE = 32
TILE_DATA = [
    {"name": "grass", "image": "assets/sprites/grass.png", "is_solid": False, "id": 0},
    {"name": "path", "image": "assets/sprites/path.png", "is_solid": False, "id": 1},
    {"name": "water", "image": "assets/sprites/water.png", "is_solid": True, "id": 2},
    {"name": "barrier", "image": "assets/sprites/barrier.png", "is_solid": True, "id": 3},
    {"name": "chest", "image": "assets/sprites/chest.png", "is_solid": True, "id": 4},
]

#MAP
MAP_WIDTH = 64
MAP_HEIGHT = 64

#OBJECTS
#---NPC LIST
NPC_DATA = [
    {"name": "Bob", "image": "assets/sprites/npc_test.png", "x": 150, "y": 150, "id": 1, "quest_id": 1},
    {"name": "Jess", "image": "assets/sprites/npc_test.png", "x": 150, "y": 500, "id": 2, "quest_id": 2}
]
#---CHESTS

#---ENEMIES

