#!/usr/bin/python3

# Link : http://inventwithpython.com/chapter4.html

__author__ = 'phonbopit'

import random

guessesTaken = 0

print('Hello! What \'s your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

while guessesTaken < 6:
    print('Taken a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        break

if guess == number:
    # guessesTaken = str(guessesTaken)
    # print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    print('Good job, {}! You guessed my number in {} guesses!'.format(myName, guessesTaken))

if guess != number:
    number = str(number)
    print('Game Over!!!!!')

