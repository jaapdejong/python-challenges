#!/usr/bin/python3
#
# Exercise 15 (and Solution)
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#  My name is Michele
# Then I would see the string:
#  Michele is name My
# shown back to me.

def reverseList(a):
        b = ""
        for i in range(0, len(a)):
                b = a[i] + " " + b
        return b

user = input("Please enter a string with more than 1 word in it: ")
print(reverseList(user.split()))
