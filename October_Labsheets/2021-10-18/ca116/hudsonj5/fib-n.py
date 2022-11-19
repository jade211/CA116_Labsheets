#!/usr/bin/env python3

n = int(input())
i = 0
previous = 1
current = 0
while i < n:
   print(current)
   old_current = current
   current = previous + current
   previous = old_current
   i = i + 1
