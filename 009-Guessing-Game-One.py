#!/usr/bin/python3
#
# Exercise 9
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#

from random import randint
computer = randint(1, 9)

while True:
        player = int(input("Please enter a number between 1 and 9: "))
        if player == computer:
                print("Found!!")
                break
        elif player < computer:
                print("Too low")
        else:
                print("Too high")