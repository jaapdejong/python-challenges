#!/usr/bin/python3
#
# Exercise 16
# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
#

from string import printable
from random import choice

def getRandomPassword():
        length = 10
        pw = ""
        for i in range(0, length):
                pw += choice(printable)
        return pw
        
def main():
        print(getRandomPassword())

main()
