import yaml
import monitor_result as mon

width_height_coord = [-1, -1]


def set_move(move):

    height = move // 15
    width = move % 15

    with open("../steps.yaml") as f:
        movement = yaml.safe_load(f)
        a = movement["AlphaZero"]
        f.close()

    with open("../steps.yaml", 'w') as nf:
        movement.update({"Internet": {"width": width, "height": height}})
        print(movement)
        yaml.safe_dump(movement, nf)
        nf.close()


def get_move():
    while not opponent_moved():
        mon.random_wait()
    global width_height_coord
    with open("../steps.yaml") as f:
        movement = yaml.safe_load(f)
        width_height_coord = [movement["Internet"]["width"], movement["Internet"]["height"]]
        f.close()


def opponent_moved() -> bool:
    new_movement = True
    with open("../steps.yaml") as f:
        movement = yaml.safe_load(f)
        # print(movement["AlphaZero"])
        width = movement["AlphaZero"]["width"]
        height = movement["AlphaZero"]["height"]
        # print(width, height)

        if width == width_height_coord[0] and height == width_height_coord[1]:
            new_movement = False
        else:
            new_movement = True

        return new_movement


if __name__ == '__main__':
    # get_move()
    print(width_height_coord)
    set_move(35)
    print(width_height_coord)
