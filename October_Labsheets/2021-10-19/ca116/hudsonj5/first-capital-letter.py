#!/usr/bin/env python3

i = 0
f = input()
empty = ""

while i < len(f) and not ("A" <= empty <= "Z"):
   empty = f[i]
   i = i + 1
print(i - 1)
