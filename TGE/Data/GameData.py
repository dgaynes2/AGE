"""This file stores all game information"""

from dataclasses import dataclass

@dataclass
class Map:
    MAP = {}
    WIDTH = 8
    HEIGHT = 12
    CURRENTLOCATION = None
    TERRAINS = {}
    # TODO: each terrain should have name, mobs, mob spawn rates, findable resources, chance of spawning

GAMESTATES = {
    'RUN': True, # is game running
    'INSHOP': True, # is player in shop
    'BYSHOP': True, # is player next to shop
    'INBATTLE': True, # is player in battle
    'CANMOVE': True, # can player move
    'MAGIC': True, # is magic usable
    'UPGRADE': True, # can items be upgraded
    'CANFASTTRAVEL': False # can fast travel from this location
}

GAMEITEMS = {}