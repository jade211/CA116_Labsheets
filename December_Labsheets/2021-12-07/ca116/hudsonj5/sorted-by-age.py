#!/usr/bin/env python3

a = []  # list for dates
b = []  # list for names

s = input()
while s != "end":
   s2 = s[9:]  # all the names
   b.append(s2)  # added to list b
   s = s[6:8] + s[3:5] + s[0:2]  # year,month and datee
   a.append(s)  # added year month and date to list a
   s = input()

i = 0
while i < len(a):
   p = i
   j = i
   while j < len(a):
      if a[j] < a[p]:
         p = j  # p becomes the smallest number position
      j = j + 1
   tmp = a[p]  # puts smallest position in tmp holding
   a[p] = a[i]  # moves first number into position where smallest WAS
   a[i] = tmp  # smallest now in a[i] (first place)

   tmp2 = b[p]  # position of smallest dates name now in temp holding
   b[p] = b[i]  # first numbers name is moved to old smallest position
   b[i] = tmp2  # smallest name now in b[i] (first place)
   i = i + 1

i = 0
while i < (len(a) and len(b)):
   print(b[i])  # prints name
   i = i + 1
