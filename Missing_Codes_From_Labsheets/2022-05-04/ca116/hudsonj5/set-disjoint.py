#!/usr/bin/env python3

import sys
# files = sys.argv[1:]
with open("a.txt", "r") as f:
    words1 = f.readlines()
with open("b.txt", "r") as g:
    words2 = g.readlines()
count = 0
i = 0
while i < len(words1):
    word = words1[i].strip()
    j = 0
    while j < len(words2):
        wordmatch = words2[j].strip()
        if word == wordmatch:
            count = count + 1
        j = j + 1
    i = i + 1

if count == 0:
    print("disjoint")
if count > 0:
    print("intersecting")
