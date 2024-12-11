from TGE.Data import GameData, IntroduceData
from Items import Spells, EquippableItems, ConsumableItems


def create_correct_instance(player: object, name: str, qty: int):
    """Chooses which instance to make for purchased item"""

    can_make = {
        'EQUIPPABLE': {
            'WEAPON': EquippableItems.give_weapon_to_player,
            'ARMOR': EquippableItems.give_armor_to_player,
            'SHIELD': EquippableItems.give_shield_to_player,
            'STAFF': EquippableItems.give_staff_to_player,
        },
        'CONSUMABLE': {
            'FOOD': ConsumableItems.give_food_to_player,
            'HPOTION': ConsumableItems.give_healing_potion_to_player,
            'MPOTION': ConsumableItems.give_magic_potion_to_player,
            'PROJECTILE': ConsumableItems.give_projectile_to_player,
        },
        'SPELL': {
            'ATTACK': Spells.give_attack_spell_to_player,
            'DEFENSE': Spells.give_defense_spell_to_player,
            'HEALING': Spells.give_healing_spell_to_player,
        }
    }
    dict_entry = GameData.GAMEITEMS[name]
    item_type = dict_entry['TYPE']
    item_subtype = dict_entry['SUBTYPE']
    return can_make[item_type][item_subtype](player, name, qty)


class Shop:
    def __init__(self, player: object):
        """Stock reads from dicts in GameData.GAMEITEMS.
        dict -> instance on purchase"""
        self.stock = {}
        self.player = player

        self._give_player_money_stat()

    def _give_player_money_stat(self):
        """Gives player MONEY stat when shop instance created"""

        if 'MONEY' not in self.player.stats:
            self.player.stats['MONEY'] = 0

    def add_item_to_shop(self, name: str, toBuy: int, toSell: int, quantity: int = 1):
        if name not in GameData.GAMEITEMS:
            return f'{name} NOT IN GAME FILES'
        else:
            if name not in self.stock.keys():
                self.stock[name] = {'NAME': name, 'TOBUY': toBuy, 'TOSELL': toSell, 'QTY': 0}
            self.stock[name]['QTY'] += quantity

    def buy_item(self, name: str, qty: int = 1):
        if qty <= 0:
            print('INVALID QUANTITY')
            return

        if name in self.stock:
            if self.stock[name]['QTY'] >= qty:
                # reduce cost from player money
                cost = self.stock[name]['TOBUY'] * qty
                if self.player.stats['MONEY'] >= cost:
                    self.player.stats['MONEY'] -= cost
                    # create if instance if none else increment
                    if name not in self.player.inventory:
                        create_correct_instance(self.player, name, qty)
                    else:
                        self.player.inventory[name].inInventory += 1

                    # remove from stock quantity
                    self.stock[name]['QTY'] -= qty
                    # if self.stock[name]['QTY'] == 0:
                    #     del self.stock[name]
                else:
                    print('INSUFFICIENT FUNDS')
            else:
                print('NOT ENOUGH STOCK')
        else:
            print('OUT OF STOCK')

    def buy_all(self, name: str):
        """Buys as many of item n as possible with available currency"""

        if name in self.stock.keys():
            while (
                name in self.stock.keys()
                and self.stock[name]['QTY'] > 0
                and self.player.stats['MONEY'] >= self.stock[name]['TOBUY']
            ):
                self.buy_item(name)

    def sell_item(self, name: str, qty: int = 1):
        if name in self.player.inventory.keys():
            if self.player.inventory[name].inInventory >= qty:
                if name in self.stock.keys():
                    earn = self.stock[name]['TOSELL']
                    # money to player
                    self.player.stats['MONEY'] += earn
                    # adjust player and shop inventories
                    self.stock[name]['QTY'] += qty
                    self.player.inventory[name].inInventory -= qty
                    if self.player.inventory[name].inInventory == 0:
                        del self.player.inventory[name]
                else:
                    print(f'CANNOT SELL {name} HERE')
            else:
                print('INSUFFICIENT INVENTORY')
        else:
            print(f'{name} NOT IN PLAYER INVENTORY')

    def sell_all(self, name: str):
        if name in self.player.inventory.keys():
            while (
                name in self.player.inventory.keys()
                and self.player.inventory[name].inInventory > 0
            ):
                self.sell_item(name, 1)
        IntroduceData.remove_item_from_player(self.player, name)

    def view_shop(self):
        """View table of all items in shop"""

        # get maximum widths required for each column
        max_lengths = {
            'name': 0,
            'buy': 0,
            'sell': 0,
            'qty': 0,
            'type': 0
        }
        to_search = [(k,v) for k,v in self.stock.items() if v['QTY'] > 0]
        for name, data in to_search:
            max_lengths['name'] = max([max_lengths['name'], len(name), len('NAME')])
            max_lengths['buy'] = max([max_lengths['buy'], len(str(data['TOBUY'])), len('BUY')])
            max_lengths['sell'] = max([max_lengths['sell'], len(str(data['TOSELL'])), len('SELL')])
            max_lengths['qty'] = max([max_lengths['qty'], len(str(data['QTY'])), len('QTY')])
            max_lengths['type'] = max([max_lengths['type'], len(
                GameData.GAMEITEMS[name]['SUBTYPE']), len('TYPE')])

        # build formatted output
        shop_stock = []
        for name, data in self.stock.items():
            nspacing = max_lengths['name'] - len(name)
            pspacing = max_lengths['buy'] - len(str(data['TOBUY']))
            sspacing = max_lengths['sell'] - len(str(data['TOSELL']))
            qspacing = max_lengths['qty'] - len(str(data['QTY']))
            tspacing = max_lengths['type'] - len(
                GameData.GAMEITEMS[name]['SUBTYPE'])

            shop_stock.append(
                f"| {name}{' ' * nspacing} |"
                f" {data['TOBUY']}{' ' * pspacing} |"
                f" {data['TOSELL']}{' ' * sspacing} |"
                f" {data['QTY']}{' ' * qspacing} |"
                f" {GameData.GAMEITEMS[name]['SUBTYPE']}{' ' * tspacing} |"
            )

        # headers
        header = (f"| {'NAME'.center(max_lengths['name'])} |"
                  f" {'BUY'.center(max_lengths['buy'])} |"
                  f" {'SELL'.center(max_lengths['sell'])} |"
                  f" {'QTY'.center(max_lengths['qty'])} |"
                  f" {'TYPE'.center(max_lengths['type'])} |")
        shop_stock.insert(0, header)

        return "\n".join(shop_stock)
