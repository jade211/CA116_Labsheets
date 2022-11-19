#!/usr/bin/env python3

import sys
args = sys.argv[1:]  # the [1:] removes the title.py first print

i = 0
while i < len(args):
   print(args[i])
   i = i + 1
