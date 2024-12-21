"""This file handles all gamestates used by the game"""

GAMESTATES = {
    "RUN": True,  # is game running
    "INSHOP": False,  # is player in shop
    "BYSHOP": False,  # is player next to shop
    "INBATTLE": True,  # is player in battle
    "CANMOVE": True,  # can player move
    "MAGIC": False,  # is magic usable
    "UPGRADE": True,  # can items be upgraded
    "CANFASTTRAVEL": False,  # can fast travel from this location
    "VIEWMAP": False,  # is player viewing world map
    "VIEWPINFO": False,  # is player view player info
    "NEXTTOBUILDING": False,  # is player next to building
    "BYCHEST": False,  # is player next to chest
}


def change_bool(name: str, state: bool):
    """Change bool state"""

    name = str(name).upper()
    if name in {i for i in GAMESTATES.keys()}:
        GAMESTATES[name] = state


def add_bool(name: str, starting_state: bool = True):
    """Add new bool to GAMESTATES"""

    name = str(name).upper()
    if name not in GAMESTATES.keys():
        GAMESTATES[name] = starting_state


def view_game_bool(name: str) -> str:
    """Get boolean value for chosen key in GAMESTATES"""

    name = str(name).upper()
    return (
        f"{name}: {GAMESTATES[name]}"
        if name in GAMESTATES
        else f"{name} IS NOT A VALID BOOL"
    )


def view_all_game_bools() -> str:
    """Returns list of all GAMESTATES and current values"""

    max_length = max(len(key) for key in GAMESTATES.keys())

    all_bools = [
        f'{key.upper()}:{" " * (max_length-len(key.upper()) + 2)}{value}'
        for key, value in GAMESTATES.items()
    ]
    return "\n".join(all_bools)
