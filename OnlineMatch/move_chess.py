# coding=utf-8

import cv2
import imutils
from skimage.measure import compare_ssim
import math


def get_opponent_move() -> dict:
    """
    get opponent movement by examining screenshots
    :return:
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

    movement = {}

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img_me, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img_opp, (x, y), (x + w, y + h), (0, 0, 255), 2)

        col = math.ceil(x / 64)
        row = math.ceil(y / 64)

        is_chess = find_chess((x, y, w, h))


    cv2.imshow("Diff", img_opp)
    cv2.imwrite("Pictures/diff.png", img_opp)
    cv2.imwrite("Pictures/img_opp_gray.png", img_opp_gray)
    cv2.waitKey(0)

    # round(x)


def find_chess(coord: tuple) -> bool:
    (x, y, w, h) = coord
    x_start = int(x / 64)
    y_start = int(y / 64)
    x_end = x_start + 64
    y_end = y_start + 64


    return True



if __name__ == '__main__':
    get_opponent_move()

