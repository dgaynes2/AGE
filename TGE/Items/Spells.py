from TGE.Data import GameData


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
    player.inventory[name] = AttackSpell(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_defense_spell_to_player(player: object, name: str, qty: int = 1):
    """Creates defense spell in player inventory"""
    player.inventory[name] = DefenseSpell(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty

def give_healing_spell_to_player(player: object, name: str, qty: int = 1):
    """Creates healing spell in player inventory"""
    player.inventory[name] = HealingSpell(GameData.GAMEITEMS[name]['NAME'], GameData.GAMEITEMS[name]['POWER'])
    player.inventory[name].inInventory = qty