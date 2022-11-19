#!/usr/bin/env python3

line = input()

total = 0

i = 0
j = 0  # gets used as beginning of number
while i < len(line):
   while i < len(line) and line[i] != "+":  # stops when it reaches a plus
      i = i + 1
   total = total + int(line[j:i])  # after it reaches a plus it adds to total
   i = i + 1
   j = i  # moves j up to position right before last plus (start of next digit)

print(total)
