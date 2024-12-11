from TGE.Data import GameData


def view_game_bool(name: str):
    name = str(name).upper()
    if name in GameData.GAMESTATES:
        return f'{name}: {GameData.GAMESTATES[name]}'

def change_bool(name: str, state: bool):
    """Change bool to opposite state"""

    name = str(name).upper()
    if name in {i for i in GameData.GAMESTATES.keys()}:
        GameData.GAMESTATES[name] = state

def add_bool(name: str, starting_state: bool = True):
    """Add new bool to game data"""

    name = str(name).upper()
    if name not in GameData.GAMESTATES.keys():
        GameData.GAMESTATES[name] = starting_state
