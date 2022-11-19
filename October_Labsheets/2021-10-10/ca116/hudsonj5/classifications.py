#!/usr/bin/env python3

mark = int(input())

first = 70 <= mark
second = 50 <= mark and mark <= 69
third = 40 <= mark and mark <= 49
fail = mark < 40
print(first)
print(second)
print(third)
print(fail)
