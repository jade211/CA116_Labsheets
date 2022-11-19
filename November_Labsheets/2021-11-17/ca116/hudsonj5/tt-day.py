#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   section = s.split()
   a.append(section)
   s = input()

day = input()

i = 0
j = 0
while i < len(a) and j < len(section):
   if a[i]:
      while j < len(section):
         if day == section[j]:
             print(section[j:])
         j = j + 1
   i = i + 1
