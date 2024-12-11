import random

from TGE.Data import GameData
import Terrains
import copy

def create_map():
    """Populates dictionary with cells containing randomly generated terrain instances"""
    GameData.Map.TERRAINS = set(i for i in Terrains.get_all_terrains())
    # print(GameData.Map.TERRAINS)
    for y in range(0, GameData.Map.WIDTH):
        for x in range(0, GameData.Map.HEIGHT):
            terrain = random.choice(Terrains.get_all_terrains())
            GameData.Map.MAP[x, y] = Terrains.get_instance(terrain, x, y)
    copy_map()


def view_cell(x: int, y: int) -> str:
    """View information of a specific map cell"""
    return GameData.Map.MAP[x,y]

def copy_map():
    """NEVER edit original map when moving player"""
    return copy.deepcopy(GameData.Map.MAP)