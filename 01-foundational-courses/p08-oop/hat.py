# Example 1
"""
class Hat:
    def sort(self, name):
        print(name, "is in", "some house")


hat = Hat()
hat.sort("Harry")
"""


# Example 2
"""import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)


hat = Hat()
hat.sort("Harry")"""


# Example 3
import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


Hat.sort("Harry")