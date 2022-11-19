#!/usr/bin/env python3
n = 10
total = 0

i = 0
while i < n:
   digit = int(input())
   if digit >= 0:
      total = total + (digit % 10)
   elif digit < 0:
      total = total + (digit % - 10)
   i = i + 1

print(total)
