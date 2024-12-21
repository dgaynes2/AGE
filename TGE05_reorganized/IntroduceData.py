"""All functions here allow user to add different types of items to the game data."""


GAMEITEMS = {}


def _add_item_to_game_data(name: str, power: int, type_: str, subtype_: str):
    """Adds a dict to game data that can be used to make class objects as needed"""

    if name not in GAMEITEMS:
        GAMEITEMS[name] = {'NAME': name, 'POWER': power, 'TYPE': type_, 'SUBTYPE': subtype_}
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

class ConsumableItem:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.type_ = 'CONSUMABLE'
        self.inInventory = 0

    def __repr__(self):
        return self.name


class Food(ConsumableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'FOOD'

class HealingPotion(ConsumableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'HPOTION'

class MagicPotion(ConsumableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'MPOTION'

class Projectile(ConsumableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'PROJECTILE'


def give_food_to_player(player: object, name: str, qty: int = 1):
    """Creates food object in player inventory"""
    player.inventory[name] = Food(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_healing_potion_to_player(player: object, name: str, qty: int = 1):
    """Creates hp+ object in player inventory"""
    player.inventory[name] = HealingPotion(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_magic_potion_to_player(player: object, name: str, qty: int = 1):
    """Creates mp+ object in player inventory"""
    player.inventory[name] = MagicPotion(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_projectile_to_player(player: object, name: str, qty: int = 1):
    """Creates projectile object in player inventory"""
    player.inventory[name] = Projectile(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty


class EquippableItem:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.type_ = 'EQUIPPABLE'
        self.inInventory = 0

    def __repr__(self):
        return self.name


class Weapon(EquippableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'WEAPON'

class Armor(EquippableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'ARMOR'

class Shield(EquippableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'SHIELD'

class Staff(EquippableItem):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'STAFF'


def give_weapon_to_player(player: object, name: str, qty: int = 1):
    """Creates weapon object in player inventory"""
    player.inventory[name] = Weapon(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_armor_to_player(player: object, name: str, qty: int = 1):
    """Creates armor object in player inventory"""
    player.inventory[name] = Armor(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_shield_to_player(player: object, name: str, qty: int = 1):
    """Creates shield object in player inventory"""
    player.inventory[name] = Shield(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_staff_to_player(player: object, name: str, qty: int = 1):
    """Creates staff object in player inventory"""
    player.inventory[name] = Staff(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty


class Spell:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.type_ = 'SPELL'
        self.inInventory = 0 # TODO: Shouldn't have this

    def __repr__(self):
        return self.name


class AttackSpell(Spell):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'ATTACK'

class DefenseSpell(Spell):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'DEFENSE'

class HealingSpell(Spell):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.subtype_ = 'HEALING'


def give_attack_spell_to_player(player: object, name: str, qty: int = 1):
    """Creates attack spell object in player inventory"""
    player.inventory[name] = AttackSpell(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_defense_spell_to_player(player: object, name: str, qty: int = 1):
    """Creates defense spell in player inventory"""
    player.inventory[name] = DefenseSpell(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_healing_spell_to_player(player: object, name: str, qty: int = 1):
    """Creates healing spell in player inventory"""
    player.inventory[name] = HealingSpell(GAMEITEMS[name]['NAME'], GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty