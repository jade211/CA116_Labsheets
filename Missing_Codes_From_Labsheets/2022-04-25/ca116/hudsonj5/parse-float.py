#!/usr/bin/env python3

f = input()

i = 0
while i < len(f) and f[i] != ".":
    i = i + 1
if i < len(f):
    fract_part = f[i + 1:]
    int_part = f[: i]
print(int_part)
print(fract_part)
