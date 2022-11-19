#!/usr/bin/env python3

import sys
file = sys.stdin.readlines()  # reads one line at a time

i = 0
while i < len(file):
   files = file[i].split("/")  # splits input up by "/"
   print(files[-1].rstrip())  # removes second string (-1) and removes
   i = i + 1                  # extra line after each line
