#!/usr/bin/env python3

n = int(input())
hundreds = int(n // 100) % 10
tens = int(n // 10) % 10
units = (n % 10)
print(hundreds)
print(tens)
print(units)
