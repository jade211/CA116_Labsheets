#!/usr/bin/env python3

lines = input()
#a = []

while lines != "end":
   sections = lines.split()
   time = int(sections[2])
   if time > 1:
      print(" ".join(sections[:]))
   lines = input()
