#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and (s[i] <= "0" or "9" <= s[i]):
    i = i + 1

j = i
if i < len(s):
    while j < len(s) and ("0" <= s[j] or s[j] >= "9"):
        j = j + 1

k = j
if j < len(s):
    while k < len(s) and ("0" > s[k] or s[k] > "9"):
        k = k + 1

o = k
if k < len(s):
    while o < len(s) and ("0" <= s[o] or s[o] >= "9"):
        o = o + 1
if k < len(s):
    print(s[k:o], k)
