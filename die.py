'''This defines the die object'''
import random


class Die:
    def __init__(self, sides=6):
        if sides > 1:
            self.Sides = sides
        else:
            self.Sides = 6

    def Roll(self):
        return random.randint(1, self.Sides)
