#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   if i < n // 2:
      j = i
      print(j * " " + "*" + (n - i * 2 - 2) * " " + "*")
   elif i == n // 2:
      print((n // 2) * " " + "*")
   else:
      j = n - i - 1
      print(j * " " + "*" + (n - j * 2 - 2) * " " + "*")
   i = i + 1
