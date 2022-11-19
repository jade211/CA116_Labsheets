#!/usr/bin/env python3

s = input()
new_s = ""

i = 0
while i < len(s):
    if s[i] != " ":
        new_s = new_s + s[i]
    i = i + 1
print(new_s)
