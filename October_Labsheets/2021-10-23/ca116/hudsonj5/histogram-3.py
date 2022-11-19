#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
   m = s
   stars = int(m[i]) * "*"
   print(stars)
   i = i + 1
