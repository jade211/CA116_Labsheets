#!/usr/bin/env python3

import sys
words = sys.stdin.read().split()

dict = {
   ".": True,
   "?": True,
   "!": True
}

i = 0
while i < len(words):
   j = i
   while j < len(words) and words[j][len(words[j]) - 1] not in dict:
      j = j + 1  # this loop looks for.!? at end of word [j]
   j = j + 1
   print(" ".join(words[i:j]))  # prints start of line till j (where .!? is)
   i = j  # gets ready for next loop starting from ending of last
