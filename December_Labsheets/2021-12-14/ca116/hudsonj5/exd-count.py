#!/usr/bin/env python3


import sys
n = (sys.argv[1])
numbers = 0

i = 0
while i < int(n):
   if numbers[i] ** numbers[i] < int(n):
      print(numbers[i])
   i = i + 1
