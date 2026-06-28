import random as r

# Define class to represent die and roll
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return r.randint(1, self.sides)