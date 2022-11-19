#!/usr/bin/env python3

smallest = int(input())

i = 0
while i < 10 - 1:
   m = int(input())
   if m < smallest and m > 0:
      smallest = m
   else:
      smallest = smallest
   i = i + 1

print(smallest)
