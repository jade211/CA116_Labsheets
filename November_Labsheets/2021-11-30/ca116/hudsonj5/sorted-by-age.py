#!/usr/bin/env python3

a = []
b = []
p = 0
j = 0

s = input()
while s != "end":
   s2 = s[9:]  # all the names
   b.append(s2)  # added to list a
   s = s[6:8] + s[3:5] + s[0:2]  # year,month and datee
   a.append(s)  # added year month and date to list a
   s = input()

i = 0
while i < len(a):
   p = i
   j = i
   while j < len(a):
      if a[j] < a[p]:
         p = j  # p becomes the smallest number
      j = j + 1
   tmp = a[p]  # puts smallest in tmp holding
   a[p] = a[i]  # position of smallest put in a[p]
   a[i] = tmp  # smallest now in a[i] (first place)

   tmp2 = b[p]  # position of smallest dates name now in temp holding
   b[p] = b[i]  # smallest name moved into b[i]
   b[i] = tmp2  # smallest name now in b[i] (first place)
   i = i + 1

i = 0
while i < (len(a) and len(b)):
   print(b[i])  # prints line
   i = i + 1
