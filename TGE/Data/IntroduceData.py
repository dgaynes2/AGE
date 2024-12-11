"""All functions here allow user to add different types of items to the game data."""

from TGE.Data import GameData


def _add_item_to_game_data(name: str, power: int, type_: str, subtype_: str):
    """Adds a dict to game data that can be used to make class objects as needed"""

    if name not in GameData.GAMEITEMS:
        GameData.GAMEITEMS[name] = {'NAME': name, 'POWER': power, 'TYPE': type_, 'SUBTYPE': subtype_}
        # 'sword' : {'NAME': 'sword', 'POWER': 5, 'TYPE': 'EQUIPPABLE', 'SUBTYPE': 'WEAPON'}


def add_weapon_to_game(name: str, power: int):
    """Creates data dict for weapon object"""
    _add_item_to_game_data(name, power, 'EQUIPPABLE', 'WEAPON')

def add_armor_to_game(name: str, power: int):
    """Creates data dict for armor object"""
    _add_item_to_game_data(name, power, 'EQUIPPABLE', 'ARMOR')

def add_shield_to_game(name: str, power: int):
    """Creates data dict for shield object"""
    _add_item_to_game_data(name, power, 'EQUIPPABLE', 'SHIELD')

def add_staff_to_game(name: str, power: int):
    """Creates data dict for staff object"""
    _add_item_to_game_data(name, power, 'EQUIPPABLE', 'STAFF')


def add_food_to_game(name: str, power: int):
    """Creates data dict for food object"""
    _add_item_to_game_data(name, power, 'CONSUMABLE', 'FOOD')

def add_healing_potion_to_game(name: str, power: int):
    """Creates data dict for healing potion object"""
    _add_item_to_game_data(name, power, 'CONSUMABLE', 'HPOTION')

def add_magic_potion_to_game(name: str, power: int):
    """Creates data dict for magic potion object"""
    _add_item_to_game_data(name, power, 'CONSUMABLE', 'MPOTION')

def add_projectile_to_game(name: str, power: int):
    """Creates data dict for projectile object"""
    _add_item_to_game_data(name, power, 'CONSUMABLE', 'PROJECTILE')


def add_attack_spell_to_game(name: str, power: int):
    """Creates data dict for spell object"""
    _add_item_to_game_data(name, power, 'SPELL', 'ATTACK')

def add_defense_spell_to_game(name: str, power: int):
    """Creates data dict for spell object"""
    _add_item_to_game_data(name, power, 'SPELL', 'DEFENSE')

def add_healing_spell_to_game(name: str, power: int):
    """Creates data dict for spell object"""
    _add_item_to_game_data(name, power, 'SPELL', 'HEALING')


def remove_item_from_player(player: object, name: str):
    """Removes item from player inventory"""
    if name in player.inventory.keys():
        del player.inventory[name]