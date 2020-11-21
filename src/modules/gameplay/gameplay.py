"""
gameplay of the game
Amir Hossein Mohseni Fard
"""

from src.modules.pieces.piece import Piece
from src.modules.players.player import Player
from src.modules.board.board import Board
import sys


class GamePlay:
    def __init__(self, *args):
        self.board = Board()
        self.colors = ['blue', 'green', 'yellow', 'red']
        self.players = list()
        self.turn_count = 0
        self.finish = False
        self.valid_players = True
        for player in args:
            try:
                self.colors.remove(player.color)
                self.players.append(player)
            except ValueError:
                print("players cannot choose same color !")
                self.valid_players = False
                sys.exit()

        if 2 <= len(args) <= 4 and self.valid_players:
            self.play()

    def turn(self):
        try:
            player = self.players[self.turn_count]
            player.do_play()
            self.turn_count += 1
        except IndexError:
            self.turn_count = 0

    def play(self):
        while not self.finish:
            for player in self.players:
                if not player.win():
                    break
            self.turn()



player1 = Player('amir', 'red')
player2 = Player('ali', 'blue')
game_play = GamePlay(player1, player2)
print(f"{}")
print(game_play.players[1])
