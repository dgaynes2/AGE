from TGE.Data import GameData
import Map


def get_cell_width():
    """Base width of each cell off length of largest terrain name.
    +2 adds space on either side of word for aesthetics"""

    return max([len(i) for i in GameData.Map.TERRAINS]) + 2


def create_text_map(player: object, show_player: bool = False):
    """Print map to terminal"""

    #  "+ Data.Map.WIDTH - 1" -> adds blank spaces on either side of words for aesthetics
    cell_width = get_cell_width()
    # line between row of locations
    separator = f"*{'-' * (cell_width * GameData.Map.WIDTH + GameData.Map.WIDTH - 1)}*"

    map_rows = [separator]
    map_ = Map.copy_map()
    if show_player:
        map_[(player.x,player.y)] = player

    for row in range(GameData.Map.HEIGHT):
        locations = "|".join(
            f"{map_[(row, col)]}".center(cell_width, " ")
            for col in range(GameData.Map.WIDTH)
        )
    # for col in range(0, GameData.Map.WIDTH):
    #     locations = "|".join(
    #         f"{map_[(row, col)]}".center(cell_width, " ")
    #         for row in range(GameData.Map.HEIGHT)
    #     )
        map_rows.append(f'|{locations}|')
        map_rows.append(separator)
    return "\n".join(map_rows)