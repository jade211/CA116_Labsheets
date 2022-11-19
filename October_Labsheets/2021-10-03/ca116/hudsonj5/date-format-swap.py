#!/usr/bin/env python3

n = int(input())
a = (n % 10000)
b = (a // 100)
beginning = (b * 10000)
middle = ((n // 10000) * 100)
end = (n % 100)
print(beginning + middle + end)
