#!/usr/bin/python3
#
# Exercise 11
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.
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

def is_prime(a):
        if a == 1: return False
        for i in range(2, a // 2):
                if a % i == 0: return False
        return True

number = get_integer()
if is_prime(number):
        print(number, "is a prime!")
else:
        print(number, "is NOT a prime")
