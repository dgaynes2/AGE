from TGE.Data import GameData


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
    player.inventory[name] = Food(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_healing_potion_to_player(player: object, name: str, qty: int = 1):
    """Creates hp+ object in player inventory"""
    player.inventory[name] = HealingPotion(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_magic_potion_to_player(player: object, name: str, qty: int = 1):
    """Creates mp+ object in player inventory"""
    player.inventory[name] = MagicPotion(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_projectile_to_player(player: object, name: str, qty: int = 1):
    """Creates projectile object in player inventory"""
    player.inventory[name] = Projectile(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty