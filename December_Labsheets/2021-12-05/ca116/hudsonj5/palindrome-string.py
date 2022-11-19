#!/usr/bin/env python3

word = input()

j = len(word) - 1
i = 0
while i < len(word):
   #j = len(word) - i - 1
   while j < len(word):
      if word[i] == word[j]:
         print("palindrome")
         j = len(word) - i - 1
   i = i + 1





#i = 0
#while i < len(word) and word[0] != word[len(word) - 1]:
  # i = i + 1

#if i < len(word):
 #  print("palindrome")



# gets word backwards
# i = 0
# while i < len(s):
  # print(s[len(s) - i - 1])
  # i = i + 1
