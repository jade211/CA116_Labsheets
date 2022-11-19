#!/usr/bin/env python3

import sys
files = sys.argv[1:]
a = []

i = 0
while i < len(files):
   path = files[i].split("/")  # file split up into strings
   head = path[0]  # empty space
   j = 1
   while j < len(path):
      if path[j] == ".." and len(a) > 0:
         a.pop()  # removes .. from line
      elif path[j] == ".":
         pass
      else:
         a.append(path[j])
      j = j + 1
   pathway = head + "/" + ("/".join(a))
   print(pathway)
   i = i + 1
