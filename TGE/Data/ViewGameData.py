import IntroduceData
import GameData
from TGE import Player

p = Player.add_player()

def view_game_bools() -> str:
    """Get list of all bools in the game and their status"""

    longest_bool_name = max(
        len(str(i))
        for i in GameData.GAMESTATES.keys()
    ) + 2  # + 2 for aesthetics

    bool_output = []
    for bool_ in GameData.GAMESTATES:
        spacing = longest_bool_name - len(bool_)
        bool_output.append(
            f'{bool_}:{" " * spacing}{GameData.GAMESTATES[bool_]}'
        )
    return "\n".join(bool_output)

def view_item(name: str) -> str:
    """Get list of all bools in the game and their status"""

    if name in GameData.GAMEITEMS.keys():
        longest_stat_name = max(
            len(str(i))
            for i in GameData.GAMEITEMS[name].keys()
        ) + 2  # + 2 for aesthetics

        stat_output = []
        for stat in GameData.GAMEITEMS[name]:
            spacing = longest_stat_name - len(stat)
            stat_output.append(
                f'{stat}:{" " * spacing}{GameData.GAMEITEMS[name][stat]}'
            )
        return "\n".join(stat_output)

    else:
        print(f'{name} DOES NOT EXIST')

def view_player_inventory(player: object) -> str:
    """View player inventory"""

    longest_item_name = max(
        len(str(i))
        for i in player.inventory.keys()
    ) + 2  # + 2 for aesthetics

    item_output = [f"{player.stats['NAME'].upper()}'S INVENTORY"]
    for item in player.inventory:
        spacing = longest_item_name - len(item)
        item_output.append(
            f'{player.inventory[item]}:{" " * spacing}{player.inventory[item].inInventory}'
        )
    return "\n".join(item_output)

def view_player_equipped(player: object) -> str:
    """View player inventory"""

    longest_item_name = max(
        len(str(i))
        for i in player.equipped.keys()
    ) + 2  # + 2 for aesthetics

    item_output = [f"{player.stats['NAME'].upper()}'S EQUIPPED ITEMS"]
    for item in player.equipped:
        spacing = longest_item_name - len(item)
        item_output.append(
            f'{item}:{" " * spacing}{player.equipped[item]}'
        )
    return "\n".join(item_output)

def view_game_items():
    # make look nicer
    # add sort-by feature to sort by any key
    for i in GameData.GAMEITEMS:
        print(f'{i} - {GameData.GAMEITEMS[i]}')


IntroduceData.add_weapon_to_game('sword', 5)
IntroduceData.add_weapon_to_game('axe', 511)
IntroduceData.add_weapon_to_game('flail', 15)
IntroduceData.add_weapon_to_game('fists', 50)
IntroduceData.add_armor_to_game('helmet', 4)
# EquippableItems.give_weapon_to_player(p,'sword')
# EquippableItems.give_weapon_to_player(p,'axe', 3)
# EquippableItems.give_weapon_to_player(p,'flail', 15)
# EquippableItems.give_weapon_to_player(p,'fists', 2)
# EquippableItems.give_weapon_to_player(p, 'helmet')
# p.equip_item('sword')
# p.equip_item('helmet')
# print(view_player_equipped(p))