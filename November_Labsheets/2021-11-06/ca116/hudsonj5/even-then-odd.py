#!/usr/bin/env python3

s = input()
a = []
b = []
c = []

while s != "end":
   s = int(s)
   a.append(s)
   s = input()

i = 0
while i < len(a):
   if a[i] % 2 == 0:
      evens = a[i]
      b.append(evens)
   elif a[i] % 2 == 1:
      odds = a[i]
      c.append(odds)
   i = i + 1

i = 0
while i < len(b):
   print(b[i])
   i = i + 1

i = 0
while i < len(c):
   print(c[i])
   i = i + 1
