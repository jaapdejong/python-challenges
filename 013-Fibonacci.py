#!/usr/bin/python3
#
# Exercise 13
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
#

def get_integer(help_text = "", start = 0, end = 0):
        if help_text == "":
                if start == end:
                        help_text = "Please enter a number: "
                else:
                        help_text = "Please enter a number between " + str(start) + " and " + str(end) + ": "
        while True:
                number = int(input(help_text))
                if start == end or (number >= start and number <= end):
                        break
        return number

def fibonnaci(n):
        if n < 2: return n
        return fibonnaci(n - 1) + fibonnaci(n - 2)

number = get_integer(help_text = "Please enter the number of Ficonnaci numbers to create: ")
for i in range(1, number + 1):
        print(fibonnaci(i), end="")
        if i != number: print(end=", ")
        else: print()
