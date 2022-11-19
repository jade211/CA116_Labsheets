#!/usr/bin/env python3

total_positive = 0
total_negative = 0

n = int(input())

while n != 0:
   if 0 < n:
      total_positive = total_positive + n
   else:
      total_negative = total_negative + n
   n = int(input())

print(total_negative, total_positive)
