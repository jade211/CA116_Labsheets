#!/usr/bin/env python3

import sys
einstein = sys.stdin.read().split()
status = {}

i = 0
while i < len(einstein):
   seperate = einstein[i].split(".")
   # print(seperate) will print out line as 3 strings seperated by "."
   full_task_name = ".".join(seperate[:2])
   result = seperate[2]
   # print(full_task_name) will print "blah.py" connected back up again
   # print(result) will print out either the incorrect or the correct
   status[full_task_name] = result == "correct"
   i = i + 1

for full_task_name in status:
   if status[full_task_name]:
      print(full_task_name)
