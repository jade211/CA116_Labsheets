#!/usr/bin/env python3

n = int(input())
a = (n // 100)
b = (a % 100)

c = (b // 10)
d = (b % 10)
e = (d * 10)
print(c + e)
