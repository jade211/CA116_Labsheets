#!/usr/bin/env python3

first = int(input())
n = int(input())

while n != 0:
   if n > first:
      print("higher")
      first = n
   elif n < first:
      print("lower")
      first = n
   else:
      print("equal")
      first = n
   n = int(input())
