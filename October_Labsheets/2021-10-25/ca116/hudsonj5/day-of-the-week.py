#!/usr/bin/env python3

month = int(input()) - 1
day = int(input()) - 1

print((month * 30 + day) % 7 + 1)
