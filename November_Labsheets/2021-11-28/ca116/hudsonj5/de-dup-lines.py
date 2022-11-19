#!/usr/bin/env python3

s = input()

words = []
seen = []

i = 0
while s != "end":
   if s != "end":
      words.append(s)
   i = i + 1


i = 0
while i < len(words):
   j = 0
   while j < len(seen) and seen[j] != words[i]:
      j = j + 1

   if j == len(seen):
      seen.append(words[i])
      print(seen[i])
   i = i + 1
