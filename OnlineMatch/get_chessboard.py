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
    await page.goto(gb.game_url, {'timeout': 10000 * 30})

    # Select level
    await page.click(gb.level_selector)
    mon.print_time_and_msg(f"Selected level {gb.level_choice}")
    mon.random_wait()

    # Select color
    await page.click(gb.color_selector)
    mon.print_time_and_msg(f"Color selected as {gb.start_color}")
    mon.random_wait()

    # Click start
    start_btn_selector = "#hooks_wrap > div > form > div.color_submits > button"
    await page.click(start_btn_selector)
    mon.print_time_and_msg(f"Clicked start button ")
    mon.random_wait()

    gb.page = page


async def get_img_position() -> dict:
    """
    Get the chessboard location
    :return: Location tuple
    """
    board_selector = "#lichess > div.round.cg-512 > div.top > div > div.lichess_board_wrap > div > div > div"

    while not await gb.page.J("#lichess > div.round.cg-512 > div.top > div > div.lichess_ground > div.table_wrap"):
        mon.random_wait()

    chessboard = await gb.page.J(board_selector)
    location = await chessboard.boundingBox()  # location is a dict
    mon.print_time_and_msg(f"Got chessboard location: {location}")
    return location


async def get_chessboard_img(who: str):
    """
    Get the screenshot of the chessboard
    :param: Who moved
    :return: None
    """
    board_location = asyncio.get_event_loop().run_until_complete(get_img_position())

    captcha_option = {
        "path": f"Pictures/chessboard-{who}.png",
        "type": "png",
        "clip": board_location
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

