#!/usr/bin/env python3

# p is to f.ind a capital letter "A" <= s[i] and s[i] <= "Z"
# assign j as taking i value (first letter of acronym)

s = input()

i = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i = i + 1
if i < len(s):
   j = i
   while j < len(s) and "A" <= s[j] and s[j] <= "Z":
      j = j + 1
   print(s[i:j], i)
