#!/usr/bin/env python3

import sys
n = sys.stdin.readline()
s = sys.stdin.readlines()
plot = []

print("|")
i = 0
while i < int(n): 
   plot.append([" "] * int(n))
   i = i + 1
   
i = 0
while i < len(s):
   points = s[i].split()
   print(int(points[i]) * " " + "*")
   i = i + 1
print("|")
   

