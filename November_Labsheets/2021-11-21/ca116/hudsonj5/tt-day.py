#!/usr/bin/env python3

lines = input()
a = []

while lines != "end":
   sections = lines.split()
   a.append(sections)
   lines = input()

day = input()

i = 0
while i < len(a):
   if a[i][0] == day:  # position a[i] which is the full  line, and [0]
      print(" ".join(a[i]))   # which is the start of the section in the line.
   i = i + 1
