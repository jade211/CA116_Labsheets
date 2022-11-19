#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   position = i  # assume position is 0 first (with iterations will increase)
   j = i + 1
   while j < len(a):
      if a[j] < a[position]:
         position = j
      j = j + 1

   tmp = a[position]
   a[position] = a[i]
   a[i] = tmp
   print(a[i])

   i = i + 1
