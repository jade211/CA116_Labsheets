#!/usr/bin/env python3

first = int(input())

if first != 0:
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
