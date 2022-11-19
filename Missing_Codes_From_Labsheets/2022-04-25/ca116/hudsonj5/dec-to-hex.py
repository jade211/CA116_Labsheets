#!/usr/bin/env python3

num = int(input())
hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

result = ""
base = 16
while 0 != num:
    hexadecimal = num % base
    result = str(hex[hexadecimal]) + result
    num = num // base
print(result)
