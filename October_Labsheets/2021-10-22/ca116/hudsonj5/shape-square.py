#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   print("*" * n)
   while i < n - 2:
      print("*" + (n - 2) * " " + "*")
      i = i + 1
   i = i + 1
