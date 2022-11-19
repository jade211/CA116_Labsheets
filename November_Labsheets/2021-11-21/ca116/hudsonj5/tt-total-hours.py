#!/usr/bin/env python3

s = input()
a = []
total = 0
while s != "end":
   section = s.split()
   time = int(section[2])
   a.append(time)
   s = input()

i = 0
while i < len(a):
   total = a[i] + total
   i = i + 1

print(total)
