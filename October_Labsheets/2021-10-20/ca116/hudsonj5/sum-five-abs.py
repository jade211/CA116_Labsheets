#!/usr/bin/env python3

total = 0

i = 0
while i < 5:
   n = int(input())
   if n < 0:
      total = total + - n
   else:
      total = total + n
   i = i + 1

print(total)

#absolute values is the distance of the number from 0 - minus doesnt matter
#+4 is the same as -4 in distance
