#!/usr/bin/env python3

month = int(input())
day = int(input())
day -= 1
month -= 1

print(((month * 30) + day) % 7 + 1)
