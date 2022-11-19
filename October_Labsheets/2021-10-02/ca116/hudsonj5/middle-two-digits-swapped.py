#!/usr/bin/env python3

n = int(input())
a = (n // 100)
b = (a % 100)
c = (b // 10)
d = (c // 2)
print(d * 10 + 6)
