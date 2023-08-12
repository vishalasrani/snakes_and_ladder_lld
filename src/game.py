import random

from src.board import Board
from src.dice import Dice
from src.player import Player
from queue import Queue


class Game:

    def __init__(self):
        self.player_list = Queue()
        self.board = None
        self.winner = None
        self.dice = None
        self.add_board()
        self.add_dices()
        self.add_players()

    def add_board(self):
        board_size = int(input("Enter Board Size: "))
        self.board = Board(board_size)

    def add_dices(self):
        total_dices = int(input("Enter total number of dices: "))
        self.dice = Dice(total_dices)

    def add_players(self):
        total_players = int(input("Enter total number of players: "))
        for index in range(total_players):
            player_name = input("Enter Player Name: ")
            player_email = input("Enter Player Email: ")
            self.player_list.put(Player(player_name, player_email))

    def start(self):
        while self.winner is None:
            player = self.find_player_turn()
            dice_number = self.dice.roll_dice()
            print("Player %s, current_position: %s, dice: %s" % (player.player_id, player.get_current_position(), dice_number))
            player_new_position = player.get_current_position() + dice_number
            print("Player %s, new_position: %s" % (player.player_id, player_new_position))
            player_new_position = self.check_jump(player_new_position)
            print("Player %s, new_position: %s" % (player.player_id, player_new_position))
            if player_new_position == self.board.board_size * self.board.board_size - 1:
                self.winner = player
            elif player_new_position > self.board.board_size * self.board.board_size - 1:
                continue
            else:
                player.set_current_position(player_new_position)
        print(self.winner)

    def find_player_turn(self):
        current_player = self.player_list.get()
        self.player_list.put(current_player)
        return current_player

    def check_jump(self, position):
        if position >= self.board.board_size * self.board.board_size - 1:
            return position

        cell = self.board.get_cell(position)
        if cell.get_jump() and cell.get_jump().get_jump_start() == position:
            jump = cell.get_jump()
            if jump.get_jump_start() > jump.get_jump_end():
                print("Jump done by Snake")
            else:
                print("Jump done by Ladder")
            return jump.get_jump_end()
        return position
