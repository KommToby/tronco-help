# This program "spins the wheel" and keeps spinning until it gets a different number
from random import randint

x = randint(1, 23)
y = x
while x == y:
    print(y)
    y = randint(1, 23)
