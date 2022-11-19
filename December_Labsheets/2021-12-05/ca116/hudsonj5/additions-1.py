#!/usr/bin/env python3

i = 0
while i < 10:
   line = input()
   j = 0
   while j < len(line) and ("0" <= line[j] and line[j] <= "9"):
      j = j + 1  # will keep going so long as input is numbers (will stop at +)
   print(int(line[:j]) + int(line[j:]))  # adds pre + and after +
   i = i + 1
