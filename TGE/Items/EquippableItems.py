from TGE.Data import GameData


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
    player.inventory[name] = Weapon(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_armor_to_player(player: object, name: str, qty: int = 1):
    """Creates armor object in player inventory"""
    player.inventory[name] = Armor(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_shield_to_player(player: object, name: str, qty: int = 1):
    """Creates shield object in player inventory"""
    player.inventory[name] = Shield(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_staff_to_player(player: object, name: str, qty: int = 1):
    """Creates staff object in player inventory"""
    player.inventory[name] = Staff(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty
