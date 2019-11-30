width_height_coord = [-1, -1]


def set_move(move):
    global width_height_coord
    height = move // 15
    width = move % 15
    width_height_coord = [width, height]
