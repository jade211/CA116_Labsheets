#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip("\n")
    print(line)
    i = i + 1
