import WorldMap
import Terrain
import Player
import Interface
import IntroduceData
import Shop
import Chest



player = Player.add_player()

IntroduceData.add_weapon_to_game('sword',99)

shop = Shop.Shop(player)
shop.add_item_to_shop('sword',50,99,1)

Terrain.add_field([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])
Terrain.add_river([(0,3),(1,3),(1,4)])
Terrain.add_mountain([(2,3),(2,4),(3,3),(4,2),(5,2)])
Terrain.add_cave([(0,4),(3,2)])
Terrain.add_woods([(3,0),(4,0),(3,1)])
Terrain.add_forest([(5,0),(4,1),(5,1)])
Terrain.add_desert([(4,3),(5,3),(3,4),(4,4)])
Terrain.add_lake([(5,4)])
Terrain.add_shop_to_terrain_map(player,shop,0,0,20,10)
Chest.add_chest_to_terrain_map(0,0,10,20)

WorldMap.add_world_border()
interface = Interface.Interface(WorldMap.map_info, player, shop)
interface.run()