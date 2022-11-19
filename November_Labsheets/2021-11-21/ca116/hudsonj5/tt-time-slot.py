#!/usr/bin/env python3

lines = input()
a = []
b = []
c = []

while lines != "end":
   sections = lines.split()
   a.append(sections)
   lines = input()

i = 0
while i < len(a):
   time_version = int(a[i][1])
   together = (str(time_version) + ":00")
   b.append(together)
   time = int(a[i][1])
   length = int(a[i][2])
   if length >= 2:
      end = time + (length - 1)
   if length == 1:
      end = time
   end = str(end) + ":50"
   c.append(end)
   i = i + 1

i = 0
while i < len(a):
   if a[i][1] != b[i]:
      a[i][1] = b[i]
   if a[i][2] != c[i]:
      a[i][2] = c[i]
      print(" ".join(a[i]))
   i = i + 1
