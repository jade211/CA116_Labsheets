#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   s = int(s)
   a.append(s)
   s = input()

n = int(input())

i = 0
while i < len(a):
   p = i
   j = n
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   i = i + 1

print(p)
