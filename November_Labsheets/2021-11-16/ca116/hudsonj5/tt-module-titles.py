#!/usr/bin/env python3

s = input()
while s != "end":
   sections = s.split()
   print(" ".join(sections[5:]))
   s = input()
