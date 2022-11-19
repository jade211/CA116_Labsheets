#!/usr/bin/env python3

n = int(input()) #5
m = int(input()) # 11

i = 0
while i < n:
   if m % 2 == 0:
      print(m / 2)
   elif m % 2 == 1:
      print(m * 3 + 1)
      i = i + 1

#If n is even, divide it by 2 to give n / 2
#If n is odd, multiply it by 3  and add 1 to give = 3n + 1.$
#Then take n as the new starting number and repeat the process.

#i = 0
#while i < N:
   # Do something.
#      i = i + 1
