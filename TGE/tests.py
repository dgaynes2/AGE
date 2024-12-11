import unittest

from TGE.Data import GameData, IntroduceData, Bools
from TGE import Player, Shop
from TGE.Items import EquippableItems, ConsumableItems, Spells

p = Player.add_player()
s = Shop.Shop(p)
p.stats['MONEY'] = 10_000

def reset_gamedata():
    GameData.GAMEITEMS = {}
    p.inventory = {}
    s.stock = {}
    for bool_ in GameData.GAMESTATES:
        GameData.GAMESTATES[bool_] = True

class TestAddingData(unittest.TestCase):
    def test_add_weapon(self):
        reset_gamedata()
        result = {'sword': {'NAME': 'sword', 'POWER': 5, 'TYPE': 'EQUIPPABLE', 'SUBTYPE': 'WEAPON'}}
        IntroduceData.add_weapon_to_game('sword', 5)
        self.assertEqual(GameData.GAMEITEMS, result)

    def test_add_food(self):
        reset_gamedata()
        result = {'chili': {'NAME': 'chili', 'POWER': 5, 'TYPE': 'CONSUMABLE', 'SUBTYPE': 'FOOD'}}
        IntroduceData.add_food_to_game('chili', 5)
        self.assertEqual(GameData.GAMEITEMS, result)

    def test_add_fireball(self):
        reset_gamedata()
        result = {'fireball': {'NAME': 'fireball', 'POWER': 5, 'TYPE': 'SPELL', 'SUBTYPE': 'ATTACK'}}
        IntroduceData.add_attack_spell_to_game('fireball', 5)
        self.assertEqual(GameData.GAMEITEMS, result)

class TestGivingItemsToPlayer(unittest.TestCase):
    def test_give_weapon_to_player(self):
        reset_gamedata()
        IntroduceData.add_weapon_to_game('sword', 5)
        EquippableItems.give_weapon_to_player(p, 'sword', 1)
        result = {'sword': p.inventory['sword']}
        self.assertEqual(p.inventory, result)

    def test_give_food_to_player(self):
        reset_gamedata()
        IntroduceData.add_food_to_game('chili', 5)
        ConsumableItems.give_food_to_player(p, 'chili', 1)
        result = {'chili': p.inventory['chili']}
        self.assertEqual(p.inventory, result)

    def test_attack_spell_to_player(self):
        reset_gamedata()
        IntroduceData.add_attack_spell_to_game('fireball', 5)
        Spells.give_attack_spell_to_player(p, 'fireball', 1)
        result = {'fireball': p.inventory['fireball']}
        self.assertEqual(p.inventory, result)


class TestEquippingAndUnequippingItems(unittest.TestCase):
    def test_equip_weapon(self):
        reset_gamedata()
        result = {'WEAPON': 'sword', 'ARMOR': None, 'SHIELD': None}
        IntroduceData.add_weapon_to_game('sword', 5)
        EquippableItems.give_weapon_to_player(p, 'sword')
        p.equip_item('sword')
        self.assertEqual(p.equipped, result)

    def test_unequip_weapon(self):
        result = {'WEAPON': None, 'ARMOR': None, 'SHIELD': None}
        IntroduceData.add_weapon_to_game('sword', 5)
        EquippableItems.give_weapon_to_player(p, 'sword')
        p.equip_item('sword')
        p.unequip_item('WEAPON')
        self.assertEqual(p.equipped, result)

class TestShop(unittest.TestCase):
    def test_add_item_to_shop(self):
        reset_gamedata()
        result = {'sword': {'NAME': 'sword', 'TOBUY': 10, 'TOSELL': 5, 'QTY': 99}}
        IntroduceData.add_weapon_to_game('sword', 5)
        s.add_item_to_shop('sword', 10, 5, 99)
        self.assertEqual(s.stock, result)

    def test_buy_item(self):
        reset_gamedata()
        IntroduceData.add_weapon_to_game('sword', 5)
        s.add_item_to_shop('sword', 10, 5, 99)
        s.buy_item('sword', 5)
        result = 5
        self.assertEqual(p.inventory['sword'].inInventory, result)

    def test_buy_all(self):
        reset_gamedata()
        IntroduceData.add_weapon_to_game('sword', 5)
        s.add_item_to_shop('sword', 10, 5, 99)
        s.buy_all('sword')
        result = 99
        self.assertEqual(p.inventory['sword'].inInventory, result)

    def test_sell_item(self):
        reset_gamedata()
        IntroduceData.add_weapon_to_game('sword', 5)
        s.add_item_to_shop('sword', 10, 5, 99)
        s.buy_all('sword')
        s.sell_item('sword', 5)
        result = 94
        self.assertEqual(p.inventory['sword'].inInventory, result)

    def test_sell_all(self):
        reset_gamedata()
        IntroduceData.add_weapon_to_game('sword', 5)
        s.add_item_to_shop('sword', 10, 5, 99)
        s.buy_all('sword')
        s.sell_all('sword')
        result = {}
        self.assertEqual(p.inventory, result)

class TestStats(unittest.TestCase):
    def test_view_stat(self):
        result = 'HP: 10/10'
        self.assertEqual(p.view_stat('hp'), result)

    def test_add_stat(self):
        result = 'ANGER: 999/999'
        p.add_player_stat('anger', 999, True)
        self.assertEqual(p.view_stat('anger'), result)

    def test_change_stat(self):
        result = 'ANGER: 50/999'
        p.change_player_stat('anger', 50)
        self.assertEqual(p.view_stat('anger'), result)


    def test_remove_stat(self):
        result = 'ANGER is not a valid stat'
        p.remove_player_stat('anger')
        self.assertEqual(p.view_stat('anger'), result)

class TestBools(unittest.TestCase):
    def test_view_bool(self):
        result = False
        self.assertEqual(GameData.GAMESTATES['RUN'], result)

    def test_change_bool(self):
        result = False
        Bools.change_bool('RUN', False)
        self.assertEqual(GameData.GAMESTATES['RUN'], result)

    def test_add_bool(self):
        result = 'TEST: False'
        Bools.add_bool('test', False)
        self.assertEqual(Bools.view_game_bool('test'), result)

if __name__ == '__main__':
    unittest.main()