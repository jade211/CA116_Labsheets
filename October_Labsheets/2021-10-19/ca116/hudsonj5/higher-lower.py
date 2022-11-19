#!/usr/bin/env python3

first = int(input())
i = 0
while i < 5:
   n = int(input())
   if n > first:
      print("higher")
      first = n
   elif n < first:
      print("lower")
      first = n
   else:
      print("equal")
      first = n
   i = i + 1
