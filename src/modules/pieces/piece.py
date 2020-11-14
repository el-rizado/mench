"""
define pieces that we need in game
amir1375mohseni
"""
# from random import randint


class Piece:
    """
    defining special move ranges of the pieces
    """
    BLUE_RANGE = list(range(1, 49))
    GREEN_RANGE = list(range(13, 49)) + list(range(1, 13))
    YELLOW_RANGE = list(range(25, 49)) + list(range(1, 25))
    RED_RANGE = list(range(37, 49)) + list(range(1, 37))

    def __init__(self, color):
        """
        define __init__ function for first of make instance
        """
        self.color = color
        self.through = 0
        self.place = 0
        self.final_flag = False
        self.in_game = False

    @property
    def play_range(self):
        if self.color == 'blue':
            return Piece.BLUE_RANGE
        elif self.color == 'green':
            return Piece.GREEN_RANGE
        elif self.color == 'yellow':
            return Piece.YELLOW_RANGE
        elif self.color == 'red':
            return Piece.RED_RANGE

    def start(self):
        """
        when dice random number is 6
        """
        self.through = 1
        self.in_game = True
        # if self.color == 'blue':
        #     self.place = 1
        # elif self.color == 'green':
        #     self.place = 13
        # elif self.color == 'yellow':
        #     self.place = 25
        # elif self.color == 'red':
        #     self.place = 37
        self.place = self.play_range[0]

    def final(self, final_number):
        """
        when piece finish the game
        """
        self.place = final_number
        self.final_flag = True
        self.through = 48

    def advance(self, number):
        """
        forward dice number times !
        """
        destination_index = Piece.index(self.play_range, self.place) + number
        try:
            destination = self.play_range[destination_index]
            self.place = destination
            self.through += number
        except IndexError:
            if destination_index <= 51:
                self.final(100 + (destination_index - 47))
            else:
                raise

    def remove(self):
        """
        remove piece from the game : piece place is same as another piece place
        """
        self.place = 0
        self.through = 0
        self.in_game = False

    @staticmethod
    def index(my_list, number):
        """
        return index of the number in the list
        """
        return my_list.index(number)


# p1 = Piece('red')
# print(p1.play_range)
# print(f"{p1.through} bits advanced")
# print(f"place : {p1.place}")
# print("---------------------------------------------")
# p1.start()
# for i in range(20):
#     print(f"step {i + 1}")
#     dice = randint(1, 6)
#     print(f"dice = {dice}")
#     p1.advance(dice)
#     print(f"{p1.through} bits advanced")
#     print(f"place : {p1.place}")
#     print("---------------------------------------------")
#     if p1.final_flag:
#         print("game finished !")
#         break
