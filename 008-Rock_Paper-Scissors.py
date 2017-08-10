#!/usr/bin/python3
#
# Exercise 8
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock
#

attributes = ["Rock", "Scissors", "Paper"]

from random import randint
number = randint(0, len(attributes) - 1)
computer = attributes[number]

number = int(input("Please enter a number between 1 and 3: ")) - 1
if number < 0 or number > 2:
        print("Really?? You're a loser!")
else:
        player = attributes[number]

        print("Computer =", computer, "vs player =", player)

        if player == computer:
                print("No winner or loser!")
        elif (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
                print("You win!")
        else:
                print("You loose!")
