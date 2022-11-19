#!/usr/bin/env python3

s = input()
i = 0
total = 0
first_musical_letter = 0

while i < len(s):
   if s[i] == "a" or s[i] == "b" or s[i] == "c" or s[i] == "d":
      if first_musical_letter == 0:
         first_musical_letter = 1
         total = s[i]
   if s[i] == "e" or s[i] == "f" or s[i] == "g":
      if first_musical_letter == 0:
         first_musical_letter = 1
         total = s[i]
   if s[i] == "a" and total == "a":
      print("a")
      total = s[i]
   elif s[i] == "b" and total == "b":
      print("b")
      total = s[i]
   elif s[i] == "c" and total == "c":
      print("c")
      total = s[i]
   elif s[i] == "d" and total == "d":
      print("d")
      total = s[i]
   elif s[i] == "e" and total == "e":
      print("e")
      total = s[i]
   elif s[i] == "f" and total == "f":
      print("f")
      total = s[i]
   elif s[i] == "g" and total == "g":
      print("g")
      total = s[i]
   i = i + 1
