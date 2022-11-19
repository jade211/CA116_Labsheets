#!/usr/bin/env python3

import sys
files = sys.argv[1:]
total = 0

i = 0
while i < len(files):
    with open(files[i], "r") as f:
        nums1 = f.readlines()
    j = 0
    while j < len(nums1):
        total = total + int(nums1[j])
        j = j + 1
    i = i + 1

print(total)
