#!/usr/bin/env python3

a = []

s = input()

while s != "end":
   a.append(s)
   s = input()

i = 0
while i <= 9:  # numbers only range from 0 to 9
   j = 0  # takes input digit by digit
   n = 0  # amount of times to multiply * by
   while j < len(a):
      if str(i) == a[j]:  # goes from 0-9 and counts how many times no. occurs
         n = n + 1  # eg,if 0 == a[j] 3 times, n will be 3 (+1 each time)
      j = j + 1
   print(i, ("*" * n))
   i = i + 1
