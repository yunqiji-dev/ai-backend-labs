# Example 1
import random

coin = random.choice(["heads", "tails"])
print(coin)


# Example 2
from random import choice

coin = choice(["heads", "tails"])
print(coin)


# Example 3
import random

number = random.randint(1, 10)
print(number)


# Example 4
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
