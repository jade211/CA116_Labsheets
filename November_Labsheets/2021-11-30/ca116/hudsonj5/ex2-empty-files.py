#!/usr/bin/env python3

import sys
files = sys.argv[1:]

i = 0
j = 0
while i < len(files):
   seperate = files[i].split()
   while j < len(seperate):
      with open(seperate[j]) as f:
         input = f.readlines()
         if len(input) == 0:
            print(seperate[j])
      j = j + 1
   i = i + 1



import sys
files = sys.argv[1:]
i = 0
j = 0
while i < len(files):
   seperate = files[i].split()
   while j < len(seperate):
      with open(seperate[j]) as f:
         input = f.readlines()
         if len(input) == 0:
            print(seperate[j])
      j = j + 1
   i = i + 1



#with open(seperate while i < len(seperate[i]):
  # input = f.readlines() if len(input) == 0:
    #  print(seperate[i])
 #  i = i + 1
