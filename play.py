import gameclass
from get_Game_attributes import get_Game_attributes
from checkwinner import checkwinner

game = get_Game_attributes()
game.select_and_place(game.token1)