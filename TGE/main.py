import tkinter as tk
import Player
import Map
import TGE.Data.GameData as GameData
import Draw

p = Player.add_player()
Map.create_map()


win = tk.Tk()
# win.geometry("500x500")

text_screen = tk.Text(win, width=90, height=30)
text_screen.pack()
text_screen.configure(font=('TkFixedFont', 15, 'normal'))

def update_displayed_map(event=None):
    m = Draw.create_text_map(p, True)
    # tracks current location of player
    GameData.Map.CURRENTLOCATION = GameData.Map.MAP[p.x,p.y]
    # next to shop
    if GameData.Map.CURRENTLOCATION.name == 'SHOP':
        print('Enter shop?')

    text_screen.configure(state='normal')
    text_screen.delete(0.0, 'end')  # Clear existing content
    text_screen.insert('end', m)
    text_screen.configure(state='disabled')

update_displayed_map()

def move_left(event=None):
    if p.y > 0:
        p.y -= 1
        update_displayed_map()

def move_right(event=None):
    if p.y < GameData.Map.WIDTH-1:
        p.y += 1
        update_displayed_map()

def move_up(event=None):
    if p.x > 0:
        p.x -= 1
        update_displayed_map()

def move_down(event=None):
    if p.x < GameData.Map.HEIGHT-1:
        p.x += 1
        update_displayed_map()

text_screen.bind('<Up>', move_up)
text_screen.bind('<Down>', move_down)
text_screen.bind('<Left>', move_left)
text_screen.bind('<Right>', move_right)




win.mainloop()