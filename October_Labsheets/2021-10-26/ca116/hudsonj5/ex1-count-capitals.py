#!/usr/bin/env python3

s = input()
total_true = 0
total_false = 0

i = 0
while i < len(s):
   if "A" <= s[i] and s[i] <= "Z":
      total_true = total_true + 1
   else:
      total_false = total_false + 1
   i = i + 1

print(total_true)


#"A" <= s[i] and s[i] <= "Z"
