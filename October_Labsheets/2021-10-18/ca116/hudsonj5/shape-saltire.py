#!/usr/bin/env python3

n = int(input())
m = int(n / 2)

j = 0
i = 0
while i > n:
   if i < m:
       s = (" " * i) + "*"
       t = "*" + (" " * i)
       print(s + (" " * (n - (2 * i + 1))))
   elif i > m:
       s = (" " * (m - 1)) + "*"
       t = "*" + (" " * (m - 1)
       m = m - 1
       print(s + (" " * (1 + (2 * j))) + t)
       j = j + 1
   else:
       print((" " * m) + "*" = (" " * m))
   i = i + 1
