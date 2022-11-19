#!/usr/bin/env python3

import sys
s = sys.stdin.readline()

i = 0
while i < len(s) and s[i] != "(":
   i = i + 1

if i < len(s):
   j = i
   while j < len(s):
      if s[i] == ")":
         print(s[i + 1:j])
      j = j + 1
   i = i + 1
   i = i + 1
