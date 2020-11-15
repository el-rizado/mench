"""
define players that we need in game
Amir Hossein Mohseni Fard
"""
from ..pieces.piece import Piece
from random import randint


class Player:
    def __init__(self, username, color):
        self.username = username
        self.color = color
        self.pieces = Player.generate_four_pieces(self.color)
        self.current_dice = None
        self.current_piece = None

    @staticmethod
    def generate_four_pieces(color):
        pieces_list = list()
        for i in range(4):
            pieces_list.append(Piece(color))
        return pieces_list

    def win(self):
        finished = 0
        for piece in self.pieces:
            if piece.final_flag is True:
                finished += 1
        if finished == 4:
            return True

    def all_pieces_out(self):
        out = 0
        for piece in self.pieces:
            if piece.in_game is False:
                out += 1
        if out == 4:
            return True

    def roll_dice(self):
        self.current_dice = randint(1, 6)

    def which_piece(self, place):
        for piece in self.pieces:
            if piece.place == place:
                self.current_piece = piece
                break

    # def do_play(self, piece):
    #     if len(self.pieces_out_game) == 4:
    #         if self.current_dice != 6:
    #             print("You can move only for 6 !")
    #         else:
    #             new_piece = choice(self.pieces_out_game)
    #             new_piece.start()
    #             self.do_play(piece)
    #             # print("start")
    #     else:
    #         if self.current_dice == 6:
    #             piece.advance(self.current_dice)
    #             self.do_play(piece)
    #         else:
    #             piece.advance(self.current_dice)
    #     self.current_dice = None

    def do_play(self):
        self.roll_dice()
        if self.all_pieces_out():
            if self.current_dice != 6:
                print("next turn")


player1 = Player('amir', 'red')
print(f"{player1.username} is {player1.color}")
print("-------------------------------------------------------")
for p in player1.pieces:
    print(f"piece {p.color} bits through is : {p.through}")
    print(f"piece {p.color} place is : {p.place}")
print("-------------------------------------------------------")
for _ in range(2):
    player1.do_play()
