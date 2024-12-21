"""This file contains the chests that can appear around the map"""

from Terrain import map_info

def add_chest_to_terrain_map(worldx: int, worldy: int, x: int, y: int):
    """Add a chest to the terrain"""

    map_info.WORLDMAP[worldx,worldy].location_map[x,y] = Chest([])


class Chest:
    def __init__(self,contents: list[str]):
        self.contents = contents

    def __repr__(self):
        return 'C'