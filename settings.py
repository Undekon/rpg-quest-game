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
INVENTORY_SLOTS = 20
DECK_SLOTS = 10
EXP_PER_LEVEL = 30
HEALTH_PER_LEVEL = 10
STAMINA_PER_LEVEL = 5
MANA_PER_LEVEL = 10

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

#CARDS
CARD_ICON_HEIGT = 128
CARD_ICON_WIDTH = 96

#CARD_HEIGHT = 192
#CARD_WIDTH = 128

CARD_DATA = [
    #Attack
    {"id": 0, "type": "attack", "name": "Sword Slash", "image": 'assets/cards/attack_card1.png', "description": 'Basic melee attack', "dmg": 10, 'mana': 2, 'defense': 0, 'heal': 0},
    {"id": 1, "type": "attack","name": "Arrow Shot", "image": 'assets/cards/attack_card2.png', "description": 'Fast, ranged attack', "dmg": 8, 'mana': 1, 'defense': 0, 'heal': 0},
    {"id": 2, "type": "attack","name": "Hammer Strike", "image": 'assets/cards/attack_card3.png', "description": 'Slow but strong attack', "dmg": 14, 'mana': 4, 'defense': 0, 'heal': 0},
    #Defense
    {"id": 10, "type": "defense","name": "Dodge", "image": 'assets/cards/attack_card.png', "description": 'Evadesa the attack', "dmg": 0, 'mana': 2, 'defense': 8, 'heal': 0},
    {"id": 11, "type": "defense","name": "Wooden Shield", "image": 'assets/cards/attack_card.png', "description": 'Basic defense', "dmg": 0, 'mana': 2, 'defense': 10, 'heal': 0},
    {"id": 12, "type": "defense","name": "Stone Wall", "image": 'assets/cards/attack_card.png', "description": 'High and strong defense', "dmg": 0, 'mana': 4, 'defense': 12, 'heal': 0},
    #HP
    {"id": 20, "type": "hp","name": "Herbal Brew", "image": 'assets/cards/heal_card.png', "description": 'Small health restoration', "dmg": 0, 'mana': 2, 'defense': 0, 'heal': 5},
    {"id": 21, "type": "hp","name": "Elixir of Life", "image": 'assets/cards/heal_card.png', "description": 'Heals by the magic', "dmg": 0, 'mana': 4, 'defense': 0, 'heal': 8},
    {"id": 22, "type": "hp","name": "Priest's Prayer", "image": 'assets/cards/heal_card.png', "description": 'Strong healing', "dmg": 0, 'mana': 3, 'defense': 0, 'heal': 10},
    #Mana
    {"id": 30, "type": "mana","name": "Focus Herbs", "image": 'assets/cards/heal_card.png', "description": 'Basic defense card', "dmg": 0, 'mana': 0, 'defense': 4, 'heal': 5},
    {"id": 31, "type": "mana","name": "Meditation", "image": 'assets/cards/heal_card.png', "description": 'Basic heal card', "dmg": 0, 'mana': 1, 'defense': 0, 'heal': 8},
    {"id": 32, "type": "mana","name": "Mana Crystal", "image": 'assets/cards/heal_card.png', "description": 'Basic heal card', "dmg": 0, 'mana': 2, 'defense': 0, 'heal': 10},
    #Special cards
    # {"id": 40, "name": "Elixir of Life", "image": 'assets/cards/heal_card.png', "description": 'Basic heal card', "dmg": 0, 'mana': 4, 'defense': 0, 'heal': 4},
    # {"id": 41, "name": "Elixir of Life", "image": 'assets/cards/heal_card.png', "description": 'Basic heal card', "dmg": 0, 'mana': 4, 'defense': 0, 'heal': 4},
    # {"id": 42, "name": "Elixir of Life", "image": 'assets/cards/heal_card.png', "description": 'Basic heal card', "dmg": 0, 'mana': 4, 'defense': 0, 'heal': 4}
]

 

#OBJECTS
#---NPC LIST
NPC_DATA = [
    {"name": "Bob", "image": "assets/sprites/npc_test.png", "id": 0, "quest_id": 0},
    {"name": "Jess", "image": "assets/sprites/npc_test.png", "id": 1, "quest_id": 1},
    {"name": "Anna", "image": "assets/sprites/npc_test.png", "id": 2, "quest_id": 2},
    {"name": "John", "image": "assets/sprites/npc_test.png", "id": 3, "quest_id": 3},
    {"name": "Karen", "image": "assets/sprites/npc_test.png", "id": 4, "quest_id": 4},
    {"name": "Warrior", "image": "assets/sprites/npc_test.png", "id": 5, "quest_id": 5}
]

#---ENEMIES
ENEMY_DATA = [
    {"id": 0, "name": "Orc", "image": "assets/sprites/orc_warrior.png", "lvl": 1, "hp": 100, "mana": 100}
]
#TREES
TREES = [
    {'tree_id': 1, "image": "assets/sprites/tree1.png"},
    {'tree_id': 2, "image": "assets/sprites/tree2.png"}
]

#CHESTS
CHEST_DATA = [
    {"chest_id": 0, 
     "image": "assets/sprites/chest.png",""
     "type": "regular", 
     "content": [{"card_id": 1}, {"card_id": 2}]},
    {"chest_id": 1, 
     "image": "assets/sprites/chest.png",
     "type": "epic", 
     "content": ["potion"]}
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
    9: {'type': 'enemy', 'data': ENEMY_DATA[0]},
}
