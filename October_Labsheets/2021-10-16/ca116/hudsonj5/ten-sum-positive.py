#!/usr/bin/env python3

n = 10
sum = 0

i = 0
while i < n:
   m = int(input())
   if m >= 0:
      sum = m + sum
   else:
      sum = sum
   i = i + 1

print(sum)
