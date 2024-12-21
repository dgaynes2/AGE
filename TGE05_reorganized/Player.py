import Bools
import IntroduceData


class Player:
    def __init__(
        self, name: str = "Player", hp: int = 10, strength: int = 1, defense: int = 1
    ):
        self.x = 19
        self.y = 9
        self.stats = {
            "NAME": name,
            "HP": hp,
            "MAXHP": hp,
            "STRENGTH": strength,
            "DEFENSE": defense,
        }

        self.equipped = {
            "WEAPON": None,
            "ARMOR": None,
            "SHIELD": None,
        }

        self.inventory = {}

        self._can_use_magic()

    def __repr__(self):
        return self.stats["NAME"]

    # setup

    def _can_use_magic(self):
        """Adds stats for magic if applicable"""

        if Bools.GAMESTATES["MAGIC"]:
            self.stats["MP"] = 0
            self.stats["MAXMP"] = 0

    def equip_item(self, name: str):
        """Equips item to player and adjusts stats accordingly"""

        to_increase = {"WEAPON": "STRENGTH", "ARMOR": "DEFENSE", "SHIELD": "DEFENSE"}
        equippable = {
            i
            for i in self.inventory
            if IntroduceData.GAMEITEMS[i]["TYPE"] == "EQUIPPABLE"
        }

        power = IntroduceData.GAMEITEMS[name]["POWER"]
        subtype_ = IntroduceData.GAMEITEMS[name]["SUBTYPE"]
        self.stats[to_increase[subtype_]] += power
        self.inventory[name].inInventory -= 1
        self.equipped[subtype_] = name

    def unequip_item(self, slot: str):
        """Unequips item from player and adjusts stats accordingly"""

        to_decrease = {"WEAPON": "STRENGTH", "ARMOR": "DEFENSE", "SHIELD": "DEFENSE"}

        subtype_ = IntroduceData.GAMEITEMS[self.equipped[slot]]["SUBTYPE"]
        power = IntroduceData.GAMEITEMS[self.equipped[subtype_]]["POWER"]

        self.stats[to_decrease[subtype_]] -= power
        self.inventory[self.equipped[slot]].inInventory += 1
        self.equipped[subtype_] = None

    def view_stat(self, stat: str) -> str:
        """Check value of player stat
        Returns X/maxX if maxX present"""

        s = str(stat).upper()
        if s in set(self.stats.keys()):
            if f"MAX{s}" in set(self.stats.keys()):
                return f'{s}: {self.stats[s]}/{self.stats[f"MAX{s}"]}'
            return f"{s}: {self.stats[s]}"

        else:
            return f"{s} is not a valid stat"

    def view_stats(self) -> str:
        """Get list of all stats in use by player"""

        longest_stat_name = (
            max(
                [
                    len(str(i))
                    for i in self.stats.keys()
                    if self.stats[i] is not None and not i.startswith("MAX")
                ]
            )
            + 2
        )  # +2 for aesthetics

        stats_output = []
        for stat in self.stats:
            if self.stats[stat] is not None and not stat.upper().startswith("MAX"):
                spacing = longest_stat_name - len(stat)
                if f"MAX{stat}" in set(self.stats.keys()):
                    stats_output.append(
                        f"{stat}:{' ' * spacing}{self.stats[stat]}/{self.stats[f'MAX{stat}']}"
                    )
                else:
                    stats_output.append(f"{stat}:{' ' * spacing}{self.stats[stat]}")
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
        """Remove stat from player"""

        s = str(name.upper())
        if s in set(self.stats.keys()):
            del self.stats[s]
        else:
            return f"{s} is not a valid stat"


def add_player(
    name: str = "Player", hp: int = 10, strength: int = 1, defense: int = 1
) -> Player:
    """Create player character"""

    return Player(name, hp, strength, defense)
