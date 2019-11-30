# coding=utf-8

import time
import random
from _datetime import datetime
import OnlineMatch.global_data as gb
from bs4 import BeautifulSoup as Bs
import re


def random_wait():
    """
    Randomly wait some time
    :return: None
    """
    wait_time = random.uniform(0.5, 1.5)
    time.sleep(wait_time)


def print_time_and_msg(msg: str):
    """
    Print the progress message with time
    :param msg: The message that is needed to print
    :return: None
    """
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime(f'[%H:%M:%S:%m] - {msg}')
    print(readable_time)


async def is_my_turn() -> bool:
    """
    Check if this is my turn
    :return: True is my turn, False is not
    """
    my_turn = False
    my_turn_html = 'You to play'

    source = Bs(await gb.page.content(), 'lxml').prettify()

    if my_turn_html in source:
        my_turn = True

    return my_turn


async def match_result() -> bool:
    """
    Get the winner and check if the match ended
    :return: True is match ended, False is not
    """
    is_end = False
    winner = ""

    source = Bs(await gb.page.content(), 'lxml').prettify()

    if "won" in source:
        is_end = True

    return is_end


async def print_result():
    """
    Print the winner
    :return: None
    """
    source = Bs(await gb.page.content(), 'lxml').prettify()
    with open('source.html') as f:
        f.write(source)
        f.close()
    win_regex = re.compile(r'<div id="mess" class="message" style="left: 185px; top: 550px;">(\S+) has won.</div>')
    try:
        winner = re.findall(win_regex, source)[0]
        print_time_and_msg(f"CHECKMATE! {winner} wins!")
    except IndexError:
        pass


def test_placement():
    placement = int(random.uniform(0, 15))
    while placement % 38 != 0:
        placement = int(random.uniform(0, 15))
    return placement


if __name__ == '__main__':
    print(len("") > 0)

