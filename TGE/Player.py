from TGE.Data import GameData


class Player:
    def __init__(self, name: str = 'Player', hp: int = 10, strength: int = 1, defense: int = 1):
        self.x = 0
        self.y = 0
        self.stats = {
            'NAME': name,
            'HP': hp,
            'MAXHP': hp,
            'STRENGTH': strength,
            'DEFENSE': defense,
            'X': self.x,
            'Y': self.y,
            # todo: add MP if magic bool True
        }

        self.equipped = {
            'WEAPON': None,
            'ARMOR': None,
            'SHIELD': None,
        }

        self.inventory = {}

    def __repr__(self):
        return self.stats['NAME']

    def equip_item(self, name: str):
        to_increase = {'WEAPON': 'STRENGTH', 'ARMOR': 'DEFENSE', 'SHIELD': 'DEFENSE'}
        equippable = {i for i in self.inventory if GameData.GAMEITEMS[i]['TYPE'] == 'EQUIPPABLE'}

        power = GameData.GAMEITEMS[name]['POWER']
        subtype_ = GameData.GAMEITEMS[name]['SUBTYPE']
        self.stats[to_increase[subtype_]] += power
        self.inventory[name].inInventory -= 1
        self.equipped[subtype_] = name

    def unequip_item(self, slot: str):
        to_decrease = {'WEAPON': 'STRENGTH', 'ARMOR': 'DEFENSE', 'SHIELD': 'DEFENSE'}

        subtype_ = GameData.GAMEITEMS[self.equipped[slot]]['SUBTYPE']
        power = GameData.GAMEITEMS[self.equipped[subtype_]]['POWER']

        self.stats[to_decrease[subtype_]] -= power
        self.inventory[self.equipped[slot]].inInventory += 1
        self.equipped[subtype_] = None

    # stats

    def view_stat(self, stat: str) -> str:
        """Check value of player stat
        Returns X/maxX if maxX present"""

        s = str(stat).upper()
        if s in set(self.stats.keys()):
            if f'MAX{s}' in set(self.stats.keys()):
                return f'{s}: {self.stats[s]}/{self.stats[f"MAX{s}"]}'
            return f'{s}: {self.stats[s]}'

        else:
            return f'{s} is not a valid stat'

    def view_stats(self) -> str:
        """Get list of all stats is use by player"""

        longest_stat_name = max(
            [
                len(str(i))
                for i in self.stats.keys()
                if self.stats[i] is not None
                   and not i.startswith('MAX')
            ]
        ) + 2  # +2 for aesthetics

        stats_output = []
        for stat in self.stats:
            if self.stats[stat] is not None and not stat.upper().startswith('MAX'):
                spacing = longest_stat_name - len(stat)
                if f'MAX{stat}' in set(self.stats.keys()):
                    stats_output.append(
                        f"{stat}:{' ' * spacing}{self.stats[stat]}/{self.stats[f'MAX{stat}']}"
                    )
                else:
                    stats_output.append(
                        f"{stat}:{' ' * spacing}{self.stats[stat]}"
                    )
        return "\n".join(stats_output)

    def add_player_stat(self, name: str, value: int, hasMaxValue: bool = False):
        # TODO: Remember to account for max values when healing
        """Add new player stat"""

        self.stats[str(name.upper())] = value

        if hasMaxValue:
            self.stats[f"MAX{str(name.upper())}"] = value

    def change_player_stat(self, name, newValue):
        """Change value of existing stat"""

        s = str(name).upper()
        if s in set(self.stats.keys()):
            self.stats[s] = newValue
        else:
            return f"{s} is not a valid stat"

    def remove_player_stat(self, name):
        s = str(name.upper())
        if s in set(self.stats.keys()):
            del self.stats[s]
        else:
            return f"{s} is not a valid stat"


def add_player(name: str = 'Player', hp: int = 10, strength: int = 1, defense: int = 1) -> Player:
    """Create player character"""

    return Player(name, hp, strength, defense)
