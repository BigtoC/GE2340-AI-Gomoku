# coding=utf-8

page = None
browser = None
url = "https://www.coolmathgames.com/0-chess"

game_type = {
    "r": "https://chess.coolmath-games.com/setup/hook",  # Random
    "c": "https://chess.coolmath-games.com/setup/ai",  # Computer
    "f": "https://chess.coolmath-games.com/setup/friend"  # Friend
}
game_choice = "c"
game_url = game_type[game_choice]

level_selectors = {
    1: "#config_level > group > div:nth-child(1)",
    2: "#config_level > group > div:nth-child(2)",
    3: "#config_level > group > div:nth-child(3)",
    4: "#config_level > group > div:nth-child(4)",
    5: "#config_level > group > div:nth-child(5)",
    6: "#config_level > group > div:nth-child(6)",
    7: "#config_level > group > div:nth-child(7)",
    8: "#config_level > group > div:nth-child(8)"
}
level_choice = 1
level_selector = level_selectors[level_choice]

color_selectors = {
    "w": "#hooks_wrap > div > form > div.color_submits > group > div:nth-child(2)",  # White
    "b": "#hooks_wrap > div > form > div.color_submits > group > div:nth-child(3)"  # Black
}
start_color = "w"
color_selector = color_selectors[start_color]

winner = ""
