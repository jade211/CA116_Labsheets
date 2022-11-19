#!/usr/bin/env python3

import sys

german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()
english = "one two three four five six seven eight nine ten".split()
translate = {}

i = 0
while i < len(german):
    translate[english[i]] = german[i]
    i = i + 1
s = sys.stdin.readline().strip()

i = 0
while 0 < len(s):
    if s in translate:
        print(translate[s])
    s = sys.stdin.readline().strip()
