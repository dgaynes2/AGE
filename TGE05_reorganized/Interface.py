import copy
import tkinter as tk
import WorldMap
import Bools
import Shop
import Chest


def copy_map(to_copy):
    return copy.deepcopy(to_copy)

class Interface:
    def __init__(self, map_info, player, shop, player_on_map: str = 'P'):
        self.map_info = map_info # WorldMap.map_info
        self.current_coords = self.map_info.CURRENTLOCATION
        self.player = player
        self.player_on_map = player_on_map
        self.shop = shop

        self.win = tk.Tk()
        self.text_screen = tk.Text(self.win, width = self.map_info.TERRAINWIDTH, height = self.map_info.TERRAINHEIGHT)
        self.text_screen.pack()

        self.update_displayed_map(self.current_coords)

    def update_displayed_map(self, map_coords: list[int]):
        """Updates display to reflect screen changes and player movements"""

        # create updated map
        map_copy = copy_map(self.map_info.WORLDMAP[*map_coords].location_map)
        map_copy[(self.player.x, self.player.y)] = self.player_on_map[0]

        rows = []
        for y in range(max([i[1] for i in map_copy.keys()])):
            row = [
                str(map_copy.get((x,y))) for x in
                range(max([i[0] for i in map_copy.keys()]))
            ]
            rows.append(''.join(row))

        # print map to gui
        self.text_screen.configure(state='normal')
        self.text_screen.delete(0.0, 'end')
        self.text_screen.insert(0.0, '\n'.join(rows))
        self.text_screen.configure(state='disabled')

        # controls
        self.text_screen.bind("<Left>", lambda x: self.move_player('LEFT'))
        self.text_screen.bind("<a>", lambda x: self.move_player('LEFT'))

        self.text_screen.bind("<Right>", lambda x: self.move_player('RIGHT'))
        self.text_screen.bind("<d>", lambda x: self.move_player('RIGHT'))

        self.text_screen.bind("<Up>", lambda x: self.move_player('UP'))
        self.text_screen.bind("<w>", lambda x: self.move_player('UP'))

        self.text_screen.bind("<Down>", lambda x: self.move_player('DOWN'))
        self.text_screen.bind("<s>", lambda x: self.move_player('DOWN'))

        self.text_screen.bind("<m>", self.show_world_map)
        self.text_screen.bind("<p>", self.show_player_info)

    def check_surroundings(self):
        """Check the surroundings for interactive objects like chests or shops."""

        # Clear any previous bindings for the <Return> key
        self.text_screen.unbind("<Return>")

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in directions:
            dx = self.player.x + d[0]
            dy = self.player.y + d[1]
            if 0 <= dx < self.map_info.TERRAINWIDTH - 1 and 0 <= dy < self.map_info.TERRAINHEIGHT - 1:
                surrounding_object = self.map_info.WORLDMAP[*self.map_info.CURRENTLOCATION].location_map[dx,dy]

                if isinstance(surrounding_object, Chest.Chest):
                    print('Press "Enter" to open chest')
                    break

                elif isinstance(surrounding_object, Shop.Shop):
                    Bools.change_bool('BYSHOP',True)
                    print('Press "Enter" to enter shop')
                    self.text_screen.bind("<Return>", self.enter_shop)
                    return

        # Reset game states if no interactive objects are found
        Bools.change_bool('BYSHOP',False)
        Bools.change_bool('INSHOP',False)


    def move_player(self, direction: str, event=None):
        """Moves player icon on map"""

        directions = {
            'UP': (0,-1),
            'DOWN': (0,1),
            'LEFT': (-1,0),
            'RIGHT': (1,0),
        }
        dx, dy = directions[direction]

        Bools.change_bool('VIEWMAP',False)
        Bools.change_bool('VIEWPINFO',False)

        curr_loc = self.map_info.WORLDMAP[*self.map_info.CURRENTLOCATION]

        new_x = self.player.x + dx
        new_y = self.player.y + dy

        if direction in {'LEFT', 'RIGHT'}:
            if 0 <= new_x < self.map_info.TERRAINWIDTH:
                new_location = curr_loc.location_map[new_x, self.player.y]
                if (
                        type(new_location) is str and new_location not in self.map_info.IMPASSABLE
                        # and
                        # new_location is not isinstance(new_location, Chest.Chest)
                ):
                    self.player.x = new_x
            else:
                self.player.x = 0 if direction == 'RIGHT' else self.map_info.TERRAINWIDTH - 1
                self.current_coords[0] += 1 if direction == 'RIGHT' else -1

        elif direction in {'UP', 'DOWN'}:
            if 0 <= new_y < self.map_info.TERRAINHEIGHT:
                new_location = curr_loc.location_map[self.player.x, new_y]
                if (
                        type(new_location) is str and new_location not in self.map_info.IMPASSABLE
                        # and
                        # new_location is not isinstance(new_location, Chest.Chest)
                ):
                    self.player.y = new_y
            else:
                self.player.y = 0 if direction == 'DOWN' else self.map_info.TERRAINHEIGHT - 1
                self.current_coords[1] += 1 if direction == 'DOWN' else -1

        # Checks if player can interact with anything aroudn them
        self.check_surroundings()

        self.update_displayed_map(self.current_coords)

    def show_world_map(self, event=None):
        """Toggles between world map and local map"""

        if not Bools.GAMESTATES['VIEWMAP']:
            Bools.change_bool('VIEWPINFO',False)
            Bools.change_bool('INSHOP',False)
            self.text_screen.configure(state='normal')
            self.text_screen.delete(0.0, 'end')
            self.text_screen.insert(0.0, WorldMap.create_world_map(self.player_on_map[0],True))
            self.text_screen.configure(state='disabled')
        else:
            self.text_screen.update()
            self.update_displayed_map(self.current_coords)
        Bools.GAMESTATES['VIEWMAP'] = not Bools.GAMESTATES['VIEWMAP']

    def show_player_info(self, event=None):
        """Toggles between player info and local map"""

        if not Bools.GAMESTATES['VIEWPINFO']:
            Bools.change_bool('VIEWMAP',False)
            Bools.change_bool('INSHOP',False)
            self.text_screen.configure(state='normal')
            self.text_screen.delete(0.0, 'end')
            self.text_screen.insert(0.0, self.player.view_stats())
            self.text_screen.configure(state='disabled')
        else:
            self.text_screen.update()
            self.update_displayed_map(self.current_coords)
        Bools.GAMESTATES['VIEWPINFO'] = not Bools.GAMESTATES['VIEWPINFO']

    def enter_shop(self, event=None):
        """Toggles between shop and local map"""

        if Bools.GAMESTATES['BYSHOP']:
            if not Bools.GAMESTATES['INSHOP']:
                Bools.change_bool('VIEWMAP',False)
                Bools.change_bool('VIEWPINFO',False)
                self.text_screen.configure(state='normal')
                self.text_screen.delete(0.0, 'end')
                self.text_screen.insert(0.0, self.shop.view_shop())
                self.text_screen.configure(state='disabled')
            else:
                self.text_screen.update()
                self.update_displayed_map(self.current_coords)
            Bools.GAMESTATES['INSHOP'] = not Bools.GAMESTATES['INSHOP']



    def run(self):
        self.win.mainloop()