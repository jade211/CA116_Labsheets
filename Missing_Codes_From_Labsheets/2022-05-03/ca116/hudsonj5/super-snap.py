#!/usr/bin/env python3

import sys

d = {}
words = sys.stdin.readlines()
final = []

i = 0
while i < len(words):
    words[i] = words[i].strip()
    if words[i] not in d:
        d[words[i]] = 0
    if words[i] in d:
        d[words[i]] = d[words[i]] + 1
    i = i + 1

j = 0
while j < len(words):
    if words[j] in d:
        if d[words[j]] > 1:
            final.append(words[j])
    j = j + 1
if final:
    print("snap: " + final[0])
