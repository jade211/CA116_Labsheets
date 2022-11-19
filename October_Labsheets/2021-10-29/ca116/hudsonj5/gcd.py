#!/usr/bin/env python3

a = int(input())
b = int(input())

while b != 0:
   old_a = a
   a = b
   b = old_a % b

print(a)

# start with two positive integers
# keep going while b is not 0
# make a new variable to place value of a into
# make a = b
# to get the remainder, make b = to a modulus b
# because its in a loop this will give you old b as old a
