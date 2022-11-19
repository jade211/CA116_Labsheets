#!/usr/bin/env python3

import sys
position = int(sys.argv [1]) #start at 1 because 0 is title. input from terminal.
                             # also made into an integer because < wont work.

s = input() # input from textfile.
a = []
b = []

i = 0
while i < len(s):
   if s[i] == ",":
      old_i = i
      b.append(old_i)
      a.append(a[i:b[position]])
   i = i + 1
print(a)
print(b)


#i = 0 # beginning, stays at 0
# goes to position and stops because loop stops at comma.
#while i < len(s) and s[i] != ",":
  # i = i + 1

#j = i + 1
#print(s[j])
#while j < len(s) and s[j] != ",":





#print(s[i:j])

# print(i,j,s[i:j]]) # prints position 0 (i), position (j) and word between(s[i:j])




# use of split.
# token = s.split(",")
# print(token[int(position[0])])
