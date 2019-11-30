# coding=utf-8

import asyncio
import nest_asyncio

import OnlineMatch.global_data as gb
import OnlineMatch.monitor_result as mon
import OnlineMatch.get_chessboard as chess
import OnlineMatch.move_chess as move


def config_match():
    user_color = input("Please choose your color (Black[b] / White[w]):")
    gb.start_color = user_color

    user_level = input("Please choose game level you want to play (1 ~ 4):")
    gb.level_choice = user_level


if __name__ == '__main__':
    config_match()
    mon.random_wait()

    asyncio.get_event_loop().run_until_complete(
        chess.start_computer_game()
    )

    while not mon.match_result():
        if mon.is_my_turn():
            move.move()
            chess.get_chessboard_img("me")
        elif not mon.is_my_turn():
            chess.get_chessboard_img("opp")

    # ToDo: Take a screenshot after every movement
    # chessboard-me.png VS chessboard-opp.png
