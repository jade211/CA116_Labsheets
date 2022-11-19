#!/usr/bin/env python3

a = []

s = input()
while s != "end":
   a.append(int(s))
   s = input()  # this loop puts all input into a list

i = 0
while i < len(a):
   j = i
   p = i
   while j < len(a):
      if a[j] < a[p]:  # asking if 0 < 0 in first go. After first, p = largest
         p = j  # p is now the largest ane keeps updating.
      j = j + 1
   tmp = a[p]  # largest placed into temp holding
   a[p] = a[i]  # replaces p with position of largest value
   a[i] = tmp  # places largets value into a[i]
   i = i + 1

print(a[len(a) // 2])  # prints out median
