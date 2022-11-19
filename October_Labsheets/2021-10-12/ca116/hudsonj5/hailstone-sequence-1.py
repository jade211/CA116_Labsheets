#!/usr/bin/env python3

n = int(input())
m = int(input())
i = m
while i < n:
   if n % 2 == 0:
      print(n / 2)
   elif n % 2 == 1:
      print(n * 3 + 1)
      i = i + 1
