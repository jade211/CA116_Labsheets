#!/usr/bin/env python3

s = input()       # oellh to hello

i = 0
while i < len(s):
   first = (s[len(s) - 1])
   middle = (s[1:len(s) - 1])
   last = s[0]
   i = i + 1

print(first + middle + last)
