#!/usr/bin/env python3

import sys
n = int(sys.stdin.readline())
prev = 1
curr = 0

i = 0
while i < n:
   old_curr = curr
   curr = prev + curr
   prev = old_curr
   if n == prev + curr:
      print("yes")
   else:
      print("no")
   i = i + 1


