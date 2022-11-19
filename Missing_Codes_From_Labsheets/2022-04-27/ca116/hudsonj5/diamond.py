#!/usr/bin/env python3

import sys
n = int(sys.argv[1])

i = 0
while i < n:
   j = i * 2 + 1
   if n < j:
      j = 2 * n - j   # X
   print(" " * ((n - j) // 2) + "*" * j)
   i = i + 1
