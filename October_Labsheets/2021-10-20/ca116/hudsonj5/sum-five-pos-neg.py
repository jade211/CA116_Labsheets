#!/usr/bin/env python3

total_positive = 0
total_negative = 0
i = 0
while i < 5:
   n = int(input())
   if 0 < n:
      total_positive = total_positive + n
   else:
      total_negative = total_negative + n
   i = i + 1

print(total_negative, total_positive)
