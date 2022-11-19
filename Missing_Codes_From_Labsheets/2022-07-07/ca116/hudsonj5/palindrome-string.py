#!/usr/bin/env python3

w = input()
count = 0
i = 0
while i < len(w) and w[i] == w[len(w) - (i + 1)]:
    count = count + 1
    i = i + 1
if i < len(w):
    count = 0

if count == len(w):
    print("palindrome")
