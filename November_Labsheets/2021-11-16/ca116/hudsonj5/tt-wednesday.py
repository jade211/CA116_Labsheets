#!/usr/bin/env python3

s = input()
while s != "end":
   section = s.split()
   if section[0] == "3":
      print(" ".join(section[0:]))
   s = input()
