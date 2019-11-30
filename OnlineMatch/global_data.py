# coding=utf-8

page = None
browser = None
url = "https://dkmgames.com/Gomoku/gomoku.htm"

# game_opponent = {
#     "h": "#radio-choice-1",  # Friend
#     "c": "#radio-choice-2"  # Computer
# }
# opponent_choice = "h"
# opponent_selector = game_opponent[opponent_choice]

color_selectors = {
    "b": "#color > option:nth-child(1)",  # Black
    "w": "#color > option:nth-child(2)"  # White
}
start_color = "w"
color_selector = color_selectors[start_color]

level_selectors = {
    1: "#difficulty > option:nth-child(1)",  # Baby
    2: "#difficulty > option:nth-child(2)",  # Bright
    3: "#difficulty > option:nth-child(3)",  # Brainy
    4: "#difficulty > option:nth-child(4)"   # Best
}
level_choice = 3
level_selector = level_selectors[level_choice]

board_start_x = -1
board_start_y = -1
board_location = None

last_place_x = 76
last_place_y = 76
last_computer_x = 228
last_computer_y = 228

winner = ""
