#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
   i = i + 1

if i < len(s):
   print(s[i], i)

#string so instead of N, it will be len(s)
#p would be that i is more than 0 and less than 9 to get number
#print s[i] which is digit and just i which is position.
