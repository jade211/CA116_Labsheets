#!/usr/bin/env python3

n = int(input())

i = 0
while i < n - 2:
   print("*" * n)
   print("*" + (n - 2) * " " + "*")
   print("*" * n)
   i = i + 1
