#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
      j = j + 1
   if j < len(s):
      print(s[i:j], i)
   else:
      print(-1)

#p should be more than 0 less than 9 and end with " "
#after finding first digit, in if statement nname j as i
#create another while loop the opposide of the first to get full number
#loops goes from where digit begins (i)
#ie, loop stops when not a digit 0-9
