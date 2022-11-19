#!/usr/bin/env python3

import sys
dict = {}

with open("translation.txt") as f:
   words = f.readline()  # takes one line at a time ie one eins
   while words:
      word = words.split()  # splits words with " " inbetween into strings
      dict[word[0]] = word[1]  # adds to dictionary (made w1 = w2 to transl
      words = f.readline()  # next line (next two words ie two drei

number = sys.stdin.readlines()  # takes one no. at time ie 1

i = 0
while i < len(number):
   print(dict[number[i].rstrip()])
   i = i + 1
