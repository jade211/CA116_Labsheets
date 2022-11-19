#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()  # reads in input

seen = {}  # all the words seen so far

i = 0
while i < len(input):
   word = input[i].rstrip()
   if word not in seen:
      (seen)[word] = False
      print(seen[word])
   i = i + 1
