import random as r

# Define class to represent die and roll
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return r.randint(1, self.sides)
    
# 6 sided die
print ("6 sided die rolls:")
d6 = Die()
for i in range(10):
    d6.roll()
