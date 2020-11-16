"""
define players that we need in game
Amir Hossein Mohseni Fard
"""
from src.modules.pieces.piece import Piece
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

    def all_pieces_in(self):
        in_game = 0
        for piece in self.pieces:
            if piece.in_game is True:
                in_game += 1
        if in_game == 4:
            return True

    def roll_dice(self):
        self.current_dice = randint(1, 6)

    def choose_piece(self, place):
        for piece in self.pieces:
            if piece.place == place:
                self.current_piece = piece
                break

    def possible_piece(self, place):
        for piece in self.pieces:
            if piece.place == place:
                return True

    def move_with_six(self, dice_number):
        if self.all_pieces_in():
            while True:
                place = int(input("enter place of your selected piece : "))
                if self.possible_piece(place) and place < 100:
                    self.choose_piece(place)
                    break
            self.current_piece.advance(dice_number)
            self.current_dice = None
            self.current_piece = None
        else:
            self.current_piece = list(filter(lambda piece: piece.in_game is False, self.pieces))[0]
            self.current_piece.start()
            self.current_dice = None
            self.current_piece = None

    def move_with_number(self, dice_number):
        if self.all_pieces_out():
            print("next turn")
            self.current_dice = None
        else:
            while True:
                place = int(input("enter place of your selected piece : "))
                if self.possible_piece(place) and place != 0 and place < 100:
                    self.choose_piece(place)
                    break
            self.current_piece.advance(dice_number)
            self.current_dice = None
            self.current_piece = None

    def do_play(self):
        self.roll_dice()
        print(self.current_dice)
        if self.current_dice == 6:
            self.move_with_six(6)
            self.do_play()
        else:
            self.move_with_number(self.current_dice)


# player1 = Player('amir', 'red')
# print(f"{player1.username} is {player1.color}")
# print("-------------------------------------------------------")
# for piece in player1.pieces:
#     print(piece.place)
# print("-------------------------------------------------------")
# player1.do_play()

