import random


class Dice:

    def __init__(self, total_dices):
        self.total_dices = total_dices

    def roll_dice(self):
        total_increment = 0
        used_diced = 0
        for dice in range(self.total_dices):
            total_increment += random.randint(1, 6)
        return total_increment