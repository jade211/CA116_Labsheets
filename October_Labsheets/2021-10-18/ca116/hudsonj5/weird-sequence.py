#!/usr/bin/env python3

n = int(input())
m = 0

i = 0
while i < n:
    print(m)
    m = -m + (m % 2) * 2 - 1
    i = i + 1

#x = x - x * 2 + ((x % 2) * 2 - 1)
