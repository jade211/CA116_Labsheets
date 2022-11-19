#!/usr/bin/env python3

words = input()
seen = []

if words != "end":
   seen.append(words)  # words are inside seen list

while words != "end":  # begins linear search
   i = 0
   while i < len(seen) and words != seen[i]:  # if word is not same as seen[i]
      i = i + 1
   if i > (len(seen) - 1):  # if no duplicate, gets added to list
      seen.append(words)
   words = input()  # ends linear search with next word beginning next round

j = 0
while j < len(seen):  # if word is duplicated, skips above and comes here
   print(seen[j])  # prints duplicate found inside list
   j = j + 1
