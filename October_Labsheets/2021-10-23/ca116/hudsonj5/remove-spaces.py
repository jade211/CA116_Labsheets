#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
   if i == " ":
      i = ("")
      i = i + 1

print(s[0:len(s)])
