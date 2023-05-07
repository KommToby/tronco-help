# This program "spins the wheel" and keeps spinning until it gets a different number
from random import randint

# make x a number between 1 and 23
x = randint(1, 23)
# make y equal to x
y = x
while x == y: # while x and y are the same
    print(y) # print y
    y = randint(1, 23) # make y a new random number (if it is the same as before, it will do this again)
