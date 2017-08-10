#!/usr/bin/python3
#
# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#

number = int(input("Please enter a number: "))

if number % 2 == 0:
        print(number, "is even")
else:
        print(number, "is odd")
