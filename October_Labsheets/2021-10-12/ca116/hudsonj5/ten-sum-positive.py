#!/usr/bin/env python3

i = 0
sum = 0
while i < 10:
   if int(input()) > 0:
      print(int(input()) + sum)
   else:
      print(sum + 0)
   i = i + 1
