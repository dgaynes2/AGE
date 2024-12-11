import ast

from TGE.Data import GameData


class Terrain:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.mobs = {} # add any mobs that can spaw in this terrain
        self.has_player = False # is player currently here
        self.weight = 1

    def __str__(self):
        return self.name


def add_terrain_to_game_data(name: str, weight: int = 1):
    GameData.Map.TERRAINS[name] = {'NAME': name, 'WEIGHT': weight}

def _add_terrain_to_map(name: str, x: int, y: int, mobs: set):
    return Terrain(name, x, y)






class Field(Terrain):
    def __init__(self, x: int, y: int, name: str = 'FIELD'):
        super().__init__(name, x, y)

class Mountain(Terrain):
    def __init__(self, x: int, y: int, name: str = 'MOUNTAIN'):
        super().__init__(name, x, y)

class Cave(Terrain):
    def __init__(self, x: int, y: int, name: str = 'CAVE'):
        super().__init__(name, x, y)

class Forest(Terrain):
    def __init__(self, x: int, y: int, name: str = 'FOREST'):
        super().__init__(name, x, y)

class Lake(Terrain):
    def __init__(self, x: int, y: int, name: str = 'LAKE'):
        super().__init__(name, x, y)

class Town(Terrain):
    def __init__(self, x: int, y: int, name: str = 'TOWN'):
        super().__init__(name, x, y)

class Swamp(Terrain):
    def __init__(self, x: int, y: int, name: str = 'SWAMP'):
        super().__init__(name, x, y)

class Ruins(Terrain):
    def __init__(self, x: int, y: int, name: str = 'RUINS'):
        super().__init__(name, x, y)

class River(Terrain):
    def __init__(self, x: int, y: int, name: str = 'RIVER'):
        super().__init__(name, x, y)

class Desert(Terrain):
    def __init__(self, x: int, y: int, name: str = 'DESERT'):
        super().__init__(name, x, y)

class Shop(Terrain):
    def __init__(self, x: int, y: int, name: str = 'SHOP'):
        super().__init__(name, x, y)




def get_all_terrains() -> list[str]:
    """Extracts all classes inheriting from Terrain in this file.
    Either this or manually add new terrains to a list
    """

    with open(__file__, "r", encoding='utf-8') as file:
        tree = ast.parse(file.read())

    class_names = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
        and node.name != 'Terrain'
    ]
    return class_names


def get_instance(name: str, *args, **kwargs) -> object:
    """Turns string into class instance"""

    # Access the class by its name from the globals() dictionary
    class_object = globals()[name]
    return class_object(*args, **kwargs)