#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

total = 0
i = 0
while i < len(a):
   if a[i] != "":
      total = total + 1
   else:
      total = total
   i = i + 1

print(total)
