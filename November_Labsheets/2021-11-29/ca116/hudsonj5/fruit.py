#!/usr/bin/env python3

import sys
input = sys.stdin.readlines()

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

i = 0
while i < len(input):
   if input[i].rstrip() in fruit:
      sys.stdout.write(input[i])
   i = i + 1
