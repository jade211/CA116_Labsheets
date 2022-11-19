#!/usr/bin/env python3

n = int(input())
m = int(input())

i = 0
while i < n:
   print(m)
   if m % 2 == 0:
      m = m // 2
   else:
      m = m * 3 + 1
   i = i + 1

#If n is even, divide it by 2 to give n / 2
#If n is odd, multiply it by 3  and add 1 to give = 3n + 1.$
#Then take n as the new starting number and repeat the process.
