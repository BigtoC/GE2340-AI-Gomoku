# coding=utf-8

import cv2
import imutils
from skimage.measure import compare_ssim
import math
import numpy as np
import collections

import OnlineMatch.global_data as gb
import OnlineMatch.monitor_result as mon


def get_opponent_move() -> tuple:
    """
    get opponent movement by examining screenshots
    :return: opponent's chess coordinate
    :reference: https://www.jianshu.com/p/eb5026288d88,
                https://blog.csdn.net/hjxu2016/article/details/77833984
    """
    img_me = cv2.imread("Pictures/chessboard-me.png")
    img_opp = cv2.imread("Pictures/chessboard-opp.png")

    img_me_gray = cv2.cvtColor(img_me, cv2.COLOR_BGR2GRAY)
    img_opp_gray = cv2.cvtColor(img_opp, cv2.COLOR_BGR2GRAY)

    score, diff = compare_ssim(img_me_gray, img_opp_gray, full=True)
    diff = (diff * 255).astype("uint8")
    # print(f"SSIM: {score}")

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    col = -1
    row = -1

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if x == gb.last_place_x and y == gb.last_place_y:
            continue
        else:
            cv2.rectangle(img_me, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(img_opp, (x, y), (x + w, y + h), (0, 0, 255), 2)

            gb.last_computer_x = x
            gb.last_computer_y = y
            col = math.ceil(x / 38)
            row = math.ceil(y / 38)

    cv2.imshow("Diff", img_opp)
    cv2.imwrite("Pictures/diff.png", img_opp)
    cv2.waitKey(0)

    return col, row


async def move():
    place_x = gb.board_start_x + 38 * 2
    gb.last_place_x = place_x
    place_y = gb.board_start_y + 38 * 2
    gb.last_place_y = place_y
    gb.page.mouse.click(place_x, place_y)


if __name__ == '__main__':
    get_opponent_move()

