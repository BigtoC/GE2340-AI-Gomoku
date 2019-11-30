# coding=utf-8

from pyppeteer import launch
import asyncio
import nest_asyncio

import OnlineMatch.global_data as gb
import OnlineMatch.monitor_result as mon

nest_asyncio.apply()


async def start_computer_game():
    """
    Go to the match ready page
    :return: None
    """
    mon.print_time_and_msg("Setting up browser for web page...")
    url = gb.url

    gb.browser = await launch({
        "headless": False,
        "autoClose": False
    })
    page = await gb.browser.newPage()

    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(url, {'timeout': 10000 * 30})

    while not await page.J("#newgame"):
        mon.random_wait()
    mon.print_time_and_msg(f"Website is rendered!")

    # Select opponent
    # await page.click(gb.opponent_selector)
    # mon.print_time_and_msg(f"Selected opponent as {gb.opponent_choice}")
    # mon.random_wait()

    # Select color
    await page.click(gb.color_selectors[gb.start_color])
    mon.print_time_and_msg(f"Color selected as {gb.start_color}")
    mon.random_wait()

    # Select level
    await page.click(gb.level_selectors[gb.level_choice])
    mon.print_time_and_msg(f"Selected level {gb.level_choice}")
    mon.random_wait()

    # Uncheck 4 line warning
    await page.click("#cbWarn")
    mon.random_wait()

    # Click start
    start_btn_selector = "#btnPlay"
    await page.click(start_btn_selector)
    mon.print_time_and_msg(f"Clicked start button ")
    mon.random_wait()

    gb.page = page
    asyncio.get_event_loop().run_until_complete(get_img_position())


async def get_img_position():
    """
    Get the chessboard location
    :return: None
    """

    board_selector = "#grid"
    chessboard = await gb.page.J(board_selector)
    location = await chessboard.boundingBox()  # location is a dict
    mon.print_time_and_msg(f"Got chessboard location: {location}")
    gb.board_start_x = location['x']
    gb.board_start_y = location['y']
    gb.board_location = location


async def get_chessboard_img(who: str):
    """
    Get the screenshot of the chessboard
    :param: Who moved
    :return: None
    """

    captcha_option = {
        "path": f"Pictures/chessboard-{who}.png",
        "type": "png",
        "clip": gb.board_location
    }
    await gb.page.screenshot(captcha_option)
    mon.print_time_and_msg(f"Took screenshot chessboard-{who}.png")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(
        start_computer_game()
    )
    asyncio.get_event_loop().run_until_complete(
        get_chessboard_img("me")
    )

