#!/usr/bin/env python3

import sys
args = sys.argv[1:]  # the [1:] removes the title.py first print
total = 0

i = 0
while i < len(args):
   args = sys.argv[1:]
   integers = int(args[i])
   total = integers + total
   i = i + 1

print(total)
