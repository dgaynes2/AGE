import random

from WorldMap import map_info


class Terrain:
    def __init__(self, name: str, visuals: list[str]):
        self.name = name
        self.x: int
        self.y: int
        self.visuals = visuals
        self.location_map = self.create_map()

    def __repr__(self):
        return self.name

    def create_map(self) -> dict:
        """Creates map for terrain"""

        can_choose = [i for i in self.visuals] + [' '] * 3
        return {
            (x,y): random.choice([i for i in can_choose])
            for x in range(map_info.TERRAINWIDTH+1) for y in range(map_info.TERRAINHEIGHT+1)
        }


def _add_terrain_to_world_map(name: str, visuals: list[str], coordinates: list[tuple[int, int]]):
    if type(coordinates) is list:
        for x,y in coordinates:
            map_info.WORLDMAP[x,y] = Terrain(name, visuals)
    else:
        print('COORDINATES MUST BE LIST OF TUPLES')

def add_field(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('FIELD',[','], coordinates=coords)

def add_cave(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('CAVE', [':'], coordinates=coords)

def add_woods(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('WOODS', ['|'], coordinates=coords)

def add_forest(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('FOREST', ['!'], coordinates=coords)

def add_lake(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('LAKE', ['~'], coordinates=coords)

def add_river(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('RIVER', ['/'], coordinates=coords)

def add_mountain(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('MOUNTAIN', ['^'], coordinates=coords)

def add_desert(coords: list[tuple[int, int]]):
    _add_terrain_to_world_map('DESERT', ['_'], coordinates=coords)


def _add_object_to_terrain_map(worldx: int, worldy: int, x: int, y: int, symbol: str):
    """Add an object, such as a building, chest, or barrier, to the terrain"""
    # TODO: Probably move this to a separate file

    map_info.WORLDMAP[worldx,worldy].map_info[x,y] = symbol

def add_building(worldx: int, worldy: int, x: int, y:int):
    # TODO: make this a class
    _add_object_to_terrain_map(worldx, worldy, x, y, symbol='B')

def add_shop_to_terrain_map(player: object, shop: object, worldx: int, worldy: int, x: int, y: int):
    """Add a shop to the terrain"""

    map_info.WORLDMAP[worldx, worldy].location_map[x, y] = shop
