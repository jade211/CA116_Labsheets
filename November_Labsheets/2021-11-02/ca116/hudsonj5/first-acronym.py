#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and s[j] != " " and s[j] != ",":
      j = j + 1
   if j < len(s):
      print(s[i:j], i)
   else:
      print("")

#p is to find a capital letter "A" <= s[i] and s[i] <= "Z"
#assign j as taking i value (first letter of acronym)
