#!/usr/bin/python3
#
# Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
#
# nelliplaatstopnparterretrapnpotstaalpillen is a palindrome
#

s = input("Please enter a string: ")

i = 0
j = len(s) - 1
while i <= j:
        a = s[i:i+1]
        b = s[j:j+1]  

        if a != b:
                break
        else:
                i += 1
                j -= 1

if a == b:
        print(s, "is a palindrome")
else:
        print(s, "is NOT a palindrome")
