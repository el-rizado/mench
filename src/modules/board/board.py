"""
define board of the game
Amir Hossein Mohseni Fard
"""


class Board:
    def __init__(self):
        self.bits_number = dict()
        for i in range(1, 49):
            self.bits_number[i] = None

