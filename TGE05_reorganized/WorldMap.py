import copy
from dataclasses import dataclass

@dataclass
class map_info:
    WORLDMAP = {}
    CURRENTLOCATION = [0,0]
    TERRAINWIDTH = 80
    TERRAINHEIGHT = 25
    TERRAINS = []
    IMPASSABLE = ('#','B','$')


def get_cell_width():
    """Base width of each cell off length of largest terrain name.
    +2 adds space on either side of word for aesthetics"""

    return max([len(i.name) for i in map_info.WORLDMAP.values()]) + 2

def create_world_map(player_on_map:str, show_player: bool = False):
    """Shows world map with current player location (if wanted)"""

    cell_width = get_cell_width()

    map_ = copy.deepcopy(map_info.WORLDMAP)
    row_count = max(i[1] for i in map_.keys())
    col_count = max(i[0] for i in map_.keys())

    # separates each row of locations
    separator = f"*{'-' * (cell_width * (col_count+1) + col_count)}*"

    map_rows = [separator]

    # places first letter of player name on world map at current location
    if show_player:
        map_[map_info.CURRENTLOCATION[0], map_info.CURRENTLOCATION[1]] = player_on_map

    # draw world map
    for row in range(row_count+1):
        locations = "|".join(
            f"{map_[col,row].name}".center(cell_width," ")
            if (col,row) in map_.keys()
            and map_[col,row] != player_on_map
            else f"{player_on_map}".center(cell_width," ")
            if [col, row] == map_info.CURRENTLOCATION
            else f"".center(cell_width," ")
            for col in range(col_count+1)
        )

        map_rows.append(f'|{locations}|')
        map_rows.append(separator)

    return "\n".join(map_rows)

def add_world_border(symbol: str = '#'):
    """Adds border around world edge to prevent player from leaving map"""

    maxworldx = max([i[0] for i in map_info.WORLDMAP.keys()])
    maxworldy = max([i[1] for i in map_info.WORLDMAP.keys()])
    location_w = map_info.TERRAINWIDTH
    location_h = map_info.TERRAINHEIGHT

    for terrain in map_info.WORLDMAP.keys():
        if terrain[0] == 0:
            for i in range(location_h):
                map_info.WORLDMAP[terrain].location_map[0,i] = symbol

        if terrain[0] == maxworldx:
            for i in range(location_h):
                map_info.WORLDMAP[terrain].location_map[location_w - 1,i] = symbol

        if terrain[1] == 0:
            for i in range(location_w):
                map_info.WORLDMAP[terrain].location_map[i,0] = symbol

        if terrain[1] == maxworldy:
            for i in range(location_w):
                map_info.WORLDMAP[terrain].location_map[i, location_h - 1] = symbol
