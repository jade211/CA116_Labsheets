#!/usr/bin/env python3

a = []

with open("a.txt") as f:
   a += f.read().split()

with open("b.txt") as f:
   a += f.read().split()

d = {}

i = 0
while i < len(a):
   d[a[i]] = True
   i = i + 1

for key in d:
   print(key)
