#!/usr/bin/python3
#
# Exercise 14 (and Solution)
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#

a = [1, 1, 2, 5, 1, 3, 6, 5, 2, 1]

def removeDuplicatesFromList(l):
        return list(set(l))

print(a)
print(removeDuplicatesFromList(a))
