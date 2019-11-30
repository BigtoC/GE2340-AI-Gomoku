from __future__ import print_function
from game_board import Board, Game
from mcts_pure import MCTSPlayer as MCTS_pure
from mcts_alphaZero import MCTSPlayer
from policy_value_net_tensorlayer import PolicyValueNet
import time
from os import path
import os
from collections import defaultdict

import get_internet_move as internet

class Human(object):
    """
    human player
    """
    def __init__(self):
        self.player = None

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board,is_selfplay=False,print_probs_value=0):
        # no use params in the func : is_selfplay,print_probs_value
        # just to stay the same with AI's API
        try:
            width = internet.width_height_coord[0]
            height = internet.width_height_coord[1]

            location = width + height * 15
            
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            print("invalid move")
            move,_ = self.get_action(board)
        return move,None

    def __str__(self):
        return "Human {}".format(self.player)

def run(start_player=0,is_shown=1):
    # run a gomoku game with AI
    # you can set
    # human vs AI or AI vs AI
    n = 5
    width, height = 15, 15
    model_file = 'model_15_15_5/best_policy.model'
    p = os.getcwd()
    model_file = path.join(p,model_file)

    board = Board(width=width, height=height, n_in_row=n)
    game = Game(board)

    mcts_player = MCTS_pure(5,400)

    best_policy = PolicyValueNet(board_width=width,board_height=height,block=19,init_model=model_file,cuda=True)

    # alpha_zero vs alpha_zero

    # best_policy.save_numpy(best_policy.network_all_params)
    # best_policy.load_numpy(best_policy.network_oppo_all_params)
    alpha_zero_player = MCTSPlayer(policy_value_function=best_policy.policy_value_fn_random,
                                   action_fc=best_policy.action_fc_test,
                                   evaluation_fc=best_policy.evaluation_fc2_test,
                                   c_puct=5,
                                   n_playout=400,
                                   is_selfplay=False)

    # alpha_zero_player_oppo = MCTSPlayer(policy_value_function=best_policy.policy_value_fn_random,
    #                                     action_fc=best_policy.action_fc_test_oppo,
    #                                     evaluation_fc=best_policy.evaluation_fc2_test_oppo,
    #                                     c_puct=5,
    #                                     n_playout=400,
    #                                     is_selfplay=False)

    # human / Internet player, input your move in the format: 2,3
    # set start_player=0 for human first
    # play in termianl without GUI

    human = Human()
    win = game.start_play(human, alpha_zero_player, start_player=start_player, is_shown=is_shown,print_prob=True)
    print(win)
    # return win

    # play in GUI
    # game.start_play_with_UI(alpha_zero_player)


if __name__ == '__main__':
    run(start_player=0,is_shown=True)