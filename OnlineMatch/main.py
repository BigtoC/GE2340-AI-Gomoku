# coding=utf-8

import asyncio
import nest_asyncio

import OnlineMatch.global_data as gb
import OnlineMatch.monitor_result as mon
import OnlineMatch.get_chessboard as chess


def config_match():
    user_color = input("Please choose your color (Black[b] / White[w]):")
    gb.start_color = user_color

    user_level = input("Please choose game level you want to play (1 ~ 4):")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(
        chess.start_computer_game()
    )
    # ToDo: Take a screenshot after every movement
    # chessboard-me.png VS chessboard-opp.png
