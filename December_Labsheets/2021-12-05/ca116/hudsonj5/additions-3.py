#!/usr/bin/env python3

j = 0
total = 0

while total != 1000:  # overall stops at 1000 loop
   line = input()
   i = 0
   while i < len(line) and line[i] != "+":  # if total is not 1000, will
      i = i + 1  # come down here and stop when it reaches the +
   start_digit = int(line[0:i])
   end_digit = int(line[i + 1:])
   total = start_digit + end_digit
   print(start_digit + end_digit)
   j = j + 1
