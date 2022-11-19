#!/usr/bin/env python3

n = int(input())
fizz = 0
i = 0
while i < n:
   m = int(input())
   if m % 3 == 0 and m % 5 == 0:
       fizz = fizz + m
   i = i + 1
print(fizz)

