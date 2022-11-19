#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
total = 0

i = 0
while i < len(s):
   m = int(s[i])
   total = total + m
   i = i + 1

print(total)
