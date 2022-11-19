#!/usr/bin/env python3

import sys
files = sys.argv[1:]

with open(files[0]) as f:
   lines1 = f.read()

with open(files[1]) as f:
   lines2 = f.read()

i = 0
while i < len(lines1) and i < len(lines2) and lines1[i] == lines2[i]:
   i = i + 1  # loop will keep going so long as all of this is true.

if i < len(lines1) or i < len(lines2):  # loop comes here if lines different
   lines = lines1[0:i]  # gives from start of input to error
   # print(lines)
   sentence = lines.split("\n")  # turns each line into a string
   #  print(sentence)
   print(len(sentence) - 1, len(sentence[len(sentence) - 1]))


# len of sentence line up till error gives line of error
# (minus 1 because 0 is included)
# gives position of error on error line
