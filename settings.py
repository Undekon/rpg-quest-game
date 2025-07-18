#WINDOW SETTINGS
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 1200

#GAME
FPS = 60

#APPERANCE
# FONT = 

#PLAYER
PLAYER_SPEED = 3
PLAYER_IMAGE = "assets/sprites/player.png"
INVENTORY_SLOTS = 10
DECK_SLOTS = 5

#MAP
MAP_WIDTH = 64
MAP_HEIGHT = 64

#TILES
TILE_SIZE = 32
TILE_DATA = [
    {"name": "grass1", "image": "assets/sprites/grass1.png", "is_solid": False, "id": 0, "type": 'map'},
    {"name": "path", "image": "assets/sprites/path.png", "is_solid": False, "id": 1, "type": 'map'},
    {"name": "water", "image": "assets/sprites/water.png", "is_solid": True, "id": 2, "type": 'map'},
    {"name": "barrier", "image": "assets/sprites/barrier.png", "is_solid": True, "id": 3, "type": 'map'},
    {"name": "bush", "image": "assets/sprites/bush.png", "is_solid": False, "id": 4, "type": 'map'},
    {"name": "grass_flowers1", "image": "assets/sprites/grass2.png", "is_solid": False, "id": 5, "type": 'map'},
    {"name": "grass2", "image": "assets/sprites/grass3.png", "is_solid": False, "id": 6, "type": 'map'},
]

#OBJECTS
#---NPC LIST
NPC_DATA = [
    {"name": "Bob", "image": "assets/sprites/npc_test.png", "id": 0, "quest_id": 0},
    {"name": "Jess", "image": "assets/sprites/npc_test.png", "id": 1, "quest_id": 1},
    {"name": "Anna", "image": "assets/sprites/npc_test.png", "id": 2, "quest_id": 2},
    {"name": "John", "image": "assets/sprites/npc_test.png", "id": 3, "quest_id": 3},
    {"name": "Karen", "image": "assets/sprites/npc_test.png", "id": 4, "quest_id": 4},
    {"name": "Warrior", "image": "assets/sprites/npc_test.png", "id": 5, "quest_id": 5},
    {"name": "Orc", "image": "assets/sprites/orc_warrior.png", "id": 6, "quest_id": 5}
]

#---CHESTS
CHEST_DATA = [
    {"chest_id": 0, 
     "image": "assets/sprites/chest.png",""
     "type": "regular", 
     "content": ["sword"]},
    {"chest_id": 1, 
     "image": "assets/sprites/chest.png",
     "type": "epic", 
     "content": ["potion"]}
]

#---ENEMIES
TREES = [
    {'tree_id': 1, "image": "assets/sprites/tree1.png"},
    {'tree_id': 2, "image": "assets/sprites/tree2.png"}
]

#---GENERAL
OBJECT_LIST = {
    1: {"type": "chest", "data": CHEST_DATA[0]},
    2: {'type': 'npc', 'data': NPC_DATA[0]},
    3: {'type': 'npc', 'data': NPC_DATA[1]},
    4: {'type': 'tree', 'data': TREES[0]},
    5: {'type': 'tree', 'data': TREES[1]},
    6: {'type': 'npc', 'data': NPC_DATA[2]},
    7: {'type': 'npc', 'data': NPC_DATA[3]},
    8: {'type': 'npc', 'data': NPC_DATA[4]},
    9: {'type': 'npc', 'data': NPC_DATA[5]},
    10: {'type': 'npc', 'data': NPC_DATA[6]},
}

#CARDS
CARD_WIDTH = 64
CARD_HEIGHT = 48

CARD_DATA = [
    {"id": 0, "name": "basic_attack", "image": 'assets/cards/attack_card.png', "description": 'Basic attack card', "dmg": 4, 'mana': 4, 'defense': 0, 'heal': 0},
    {"id": 1, "name": "basic_defense", "image": 'assets/cards/defense_card.png', "description": 'Basic defense card', "dmg": 0, 'mana': 4, 'defense': 4, 'heal': 0},
    {"id": 2, "name": "basic_heal", "image": 'assets/cards/heal_card.png', "description": 'Basic heal card', "dmg": 0, 'mana': 4, 'defense': 0, 'heal': 4}
]