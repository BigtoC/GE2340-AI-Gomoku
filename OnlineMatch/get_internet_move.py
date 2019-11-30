# coding=utf-8

import OnlineMatch.global_data as gb

width_height_coord = [-1, -1]


def set_move():
    global width_height_coord

    width = gb.last_computer_x
    height = gb.last_computer_y

    width_height_coord = [width, height]
