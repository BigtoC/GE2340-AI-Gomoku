# coding=utf-8

import OnlineMatch.global_data as gb


def get_internet_move():

    w = gb.last_computer_x / 38
    h = gb.last_computer_y / 38

    return h * 15 + w
