# coding=utf-8

import cv2
import imutils
from skimage.measure import compare_ssim
import math
import pysnooper
import random

import OnlineMatch.global_data as gb
import OnlineMatch.monitor_result as mon
import OnlineMatch.internet_export_move as im


# @pysnooper.snoop()
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
        # 231 229 73 39
        (x, y, w, h) = cv2.boundingRect(c)
        const_b = 38

        if w < 35 or h < 35:
            continue
        if abs(x - gb.last_place_x) < 5 and abs(y - gb.last_place_y) < 5:
            continue
        elif w >= 35 * 2:
            for i in range(round(w / 37)):
                tmp_x = 38 * i + x
                if abs(tmp_x - gb.last_computer_x) < 5:
                    continue
                new_x = tmp_x
                col, row = cal_coord(cv2, img_me, img_opp, new_x, y, const_b, const_b)
        elif h >= 35 * 2:
            for i in range(round(h / 37)):
                tmp_y = 38 * i + x
                if abs(tmp_y - gb.last_computer_y) < 5:
                    continue
                new_y = tmp_y
                col, row = cal_coord(cv2, img_me, img_opp, x, new_y, const_b, const_b)
        else:
            col, row = cal_coord(cv2, img_me, img_opp, x, y, const_b, const_b)

    # cv2.imshow("Diff", img_opp)
    cv2.imwrite("Pictures/diff.png", img_opp)
    # cv2.waitKey(0)

    mon.print_time_and_msg(f"Opponent placed on [{col}, {row}]")

    return col, row


def cal_coord(cv2, img_me, img_opp, x, y, w, h):
    cv2.rectangle(img_me, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(img_opp, (x, y), (x + w, y + h), (0, 0, 255), 2)

    gb.last_computer_x = x
    gb.last_computer_y = y
    col = math.ceil(x / 37)
    row = math.ceil(y / 37)

    return col, row


async def move():
    col, row = int(random.uniform(0, 15)), int(random.uniform(0, 15))

    while col == gb.last_computer_x and row == gb.last_computer_y \
            or col == gb.last_place_x and row == gb.last_place_y:
        col, row = mon.test_placement() * 38, mon.test_placement() * 38

    place_x = gb.board_start_x + 38 * col
    gb.last_place_x = place_x
    place_y = gb.board_start_y + 38 * row
    gb.last_place_y = place_y
    await gb.page.mouse.click(place_x + 1, place_y + 1)

    mon.print_time_and_msg(f"I placed on [{col}, {row}]")


if __name__ == '__main__':
    get_opponent_move()
