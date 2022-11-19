#!/usr/bin/env python3

import sys
file = sys.argv[1]
input = sys.argv[2:]

print(file)
print(input)


i = 0
while i < len(input):
    with open(file, "w") as f:
        (f.write(input[i]))
    i = i + 1