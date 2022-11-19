#!/usr/bin/env python3

import sys
files = sys.argv[1:]
total = 0

j = 0
i = 0
while i < len(files):
   file = files[i]
   with open(file) as f:
      input = "".join(f.readlines()).rstrip("\n")
      input = input.split("\n")

   while j < len(input):
      if not ("a" <= input[i] and "z" >= input[i]) and input[i] != "" and input[i] != " ":
         total = total + int(input[i])
      j = j + 1
   j = 0
   input = []
   i = i + 1

#total = f + y
print(total)
