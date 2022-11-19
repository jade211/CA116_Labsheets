#!/usr/bin/env python3

n = 10
total = 0
i = 0

while i < n:
   if i % 2 == 0:
      total = (total + i)
   else:
      total = (total)
   i = i + 1

print(total)

# n = 10
# total = 0
# i = 0

# while i < n:
#  total = total + (i % 2) * i
#  i = i + 1

# print(total)
