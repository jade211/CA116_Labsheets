#!/usr/bin/env python3

import sys

position = int(sys.argv[1])

data = input()
headers = []
n = len(data)

i = 0
while i < n:
    if data[i] == ",":
        headers.append(data[:i])
        data = data[i + 1:]
        i = 0
        n = len(data)
    i = i + 1
headers.append(data)
print(headers[position])
