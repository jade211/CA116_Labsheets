#!/usr/bin/env python3

import sys
integers = sys.stdin.readlines()

a = []

i = 0
while i < len(integers):
   if int(integers[i]) >= 100:
      a.append(integers[i])
   i = i + 1

if i < len(integers):
   print(a[0].rstrip())
else:
   print("none")
