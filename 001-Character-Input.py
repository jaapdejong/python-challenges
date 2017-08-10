#!/usr/bin/python3
#
# Exercise 1
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#

name = input("Please enter your name: ")
age = input("Please enter your age: ")

import datetime
now = datetime.datetime.now()

print("Hi", name, "you will become a centenarian in", int(now.year) - int(age) + 100)
