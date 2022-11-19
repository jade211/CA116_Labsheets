#!/usr/bin/env python3

a = []

s = input()

while s != "end":
   a.append(s)
   s = input
print(a)

while s != "end":
   i = 0
   while i < len(a) and s != a[i]:
      if i > (len(a) - 1):
         a.append(s)
      i = i + 1
   s = input

j = 0
while j < len(a):
  # print(a[j])
   j = j + 1

#import sys

#words = sys.stdin.readlines()
#seen = []

#i = 0
#while i < len(words):
  # j = 0
 #  while j < len(seen) and seen[j] != words[i]:
   #   j = j + 1

  # if j == len(seen):
   #   seen.append(words[i])
   #   sys.stdout.write(words[i])
 #  i = i + 1
