#!/usr/bin/env python3

n = int(input())
i = 0
previous = 1
current = 0
while i < n:
   print(current)
   previous = current + previous
   current = previous - current
   i = current
