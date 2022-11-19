#!/usr/bin/env python3

import sys
file = sys.argv[1]
input = sys.argv[2:]

# print(file)
# print(input)

with open(file, "w") as f:
   i = 0
   while i < len(input):
      (f.write(input[i] + "\n"))
      i = i + 1
